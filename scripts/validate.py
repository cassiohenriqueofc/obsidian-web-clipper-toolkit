"""Validate demo templates, local links, site inventory, and common privacy leaks."""
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from common import ROOT, project_files, EXCLUDED_DIRS

errors = []
files = project_files()
policy = json.loads((ROOT / '.privacy-policy.json').read_text(encoding='utf-8'))
approved_emails = set(policy['public_emails'])
valid_types = {'text', 'multitext', 'number', 'checkbox', 'date', 'datetime'}
templates = sorted((ROOT / 'templates').glob('*.json'))
if len(templates) != 3:
    errors.append('Expected three general templates')
for path in templates:
    try:
        t = json.loads(path.read_text(encoding='utf-8'))
        for field in ['schemaVersion', 'name', 'behavior', 'noteContentFormat', 'properties', 'noteNameFormat', 'path']:
            assert field in t, f'missing {field}'
        assert t['schemaVersion'] == '0.1.0'
        assert t['behavior'] == 'create'
        assert t['vault'] == 'Demo Vault' and t['path'] == 'clippings'
        assert len({p['name'] for p in t['properties']}) == len(t['properties'])
        assert all(p['type'] in valid_types and isinstance(p['value'], str) for p in t['properties'])
        assert '{{content|replace:' in t['noteContentFormat']
        assert 'set sourceTicks = content|replace:' in t['noteContentFormat']
        assert not re.search(r'^>[ \t]*>', t['noteContentFormat'], re.M), 'authored nested callout'
        prompt_count = len(re.findall(r'\{\{"', t['noteContentFormat']))
        expected = 6 if path.name.startswith('01') else 4 if path.name.startswith('02') else 0
        assert prompt_count == expected, (prompt_count, expected)
        if expected:
            assert 'SOURCE EVIDENCE' in t['context']
            assert 'slice:0,24000' in t['context']
        else:
            assert not t['context']
    except (AssertionError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'{path.relative_to(ROOT)}: {exc}')

patterns = [
    ('credential token', re.compile(r'\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})')),
    ('nonempty credential assignment', re.compile(r'(?i)["\']?(?:api[_-]?key|access[_-]?token|password)["\']?\s*[:=]\s*["\'](?!DEMO|YOUR_|<|\[REDACTED)([^"\'\n]{8,})["\']')),
    ('personal Windows home', re.compile(r'(?i)[A-Z]:[\\/]+Users[\\/]+(?!Public\b|Default\b|Demo\b|User\b|YOUR_|<)[\w.-]+')),
    ('personal Unix home', re.compile(r'/(?:Users|home)/(?!demo\b|user\b|YOUR_|<)[A-Za-z0-9_.-]+')),
]
def check_link(origin, href):
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith('#'):
        return
    raw = unquote(parsed.path)
    if not raw:
        return
    dest = (origin.parent / raw).resolve()
    if not dest.is_relative_to(ROOT):
        errors.append(f'{origin.relative_to(ROOT)}: link leaves project: {href}')
    elif not dest.exists():
        errors.append(f'{origin.relative_to(ROOT)}: broken link: {href}')

class Links(HTMLParser):
    def __init__(self, origin):
        super().__init__(); self.origin = origin
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {'href', 'src'} and value:
                check_link(self.origin, value)

for path in files:
    rel = path.relative_to(ROOT)
    if path.is_symlink():
        errors.append(f'Symlinks are not allowed in release: {rel}')
    if path.name.startswith('.env') or re.search(r'obsidian-web-clipper-settings|settings-export', path.name, re.I):
        errors.append(f'Forbidden private export: {rel}')
    if path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico'}:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'Unexpected binary file: {rel}'); continue
    for label, pattern in patterns:
        if pattern.search(text):
            errors.append(f'{rel}: possible {label}; inspect privately (value suppressed)')
    for email in re.findall(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text):
        if email not in approved_emails and not email.endswith(('.invalid', '@example.com')):
            errors.append(f'{rel}: unapproved email; inspect privately (value suppressed)')
    if path.suffix == '.json':
        try: json.loads(text)
        except ValueError: errors.append(f'{rel}: invalid JSON')
    if path.suffix == '.md':
        # Code examples may contain illustrative paths: check only prose links.
        prose = re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text)
        for href in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)', prose):
            check_link(path, href)
        Links(path).feed(prose)
    if path.suffix == '.html':
        Links(path).feed(text)

tracked = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z'], capture_output=True, check=False).stdout.decode().split('\0')
for name in filter(None, tracked):
    if any(part in EXCLUDED_DIRS for part in Path(name).parts):
        errors.append(f'Private/generated excluded path is tracked: {name}')

inventory_path = ROOT / 'site/file-index.json'
if inventory_path.exists():
    inventory = json.loads(inventory_path.read_text())
    actual = {p.relative_to(ROOT).as_posix() for p in files}
    if set(inventory) != actual:
        errors.append('Site file inventory is stale; run scripts/build_site.py')

if errors:
    print('\n'.join('ERROR: ' + x for x in errors)); sys.exit(1)
print(f'PASS: {len(templates)} templates; {len(files)} release files; local links, file map, and baseline privacy checks.')
print('Live provider/extension/OS checks are not part of this command.')
