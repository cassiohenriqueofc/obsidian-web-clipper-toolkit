"""Generate ignored, owner-specific templates without changing tracked demo files."""
import argparse
import json
from pathlib import PurePosixPath
from common import ROOT

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--vault', required=True)
parser.add_argument('--folder', default='clippings')
parser.add_argument('--copy-vault', help='Optional separately selectable copy-destination templates; not auto-copy')
parser.add_argument('--copy-folder', default='Clippings')
args = parser.parse_args()

def valid_folder(value):
    if not value or '\\' in value or ':' in value or PurePosixPath(value).is_absolute() or '..' in PurePosixPath(value).parts:
        parser.error('Use a nonempty vault-relative folder with forward slashes and no ..')
    return value.strip('/')

for vault, folder, subdir in [(args.vault, args.folder, 'primary'), (args.copy_vault, args.copy_folder, 'secondary')]:
    if vault is None:
        continue
    if not vault.strip() or any(ord(c) < 32 for c in vault):
        parser.error('Vault name must be nonempty and contain no control characters')
    folder = valid_folder(folder)
    destination = ROOT / 'local-only' / 'templates' / subdir
    destination.mkdir(parents=True, exist_ok=True)
    for path in sorted((ROOT / 'templates').glob('*.json')):
        template = json.loads(path.read_text(encoding='utf-8'))
        template['vault'], template['path'] = vault, folder
        (destination / path.name).write_text(json.dumps(template, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Generated {subdir} templates in local-only/templates/{subdir}/ (ignored by Git).')
print('Keep Interpreter auto-run disabled. Verify vault and folder after import. Secondary templates do not perform automatic copying.')
