"""Build a sanitized versioned ZIP with manifest and SHA-256 checksums."""
import hashlib
import json
import subprocess
import zipfile
from common import ROOT, project_files

subprocess.run(['python3' if __import__('os').name != 'nt' else __import__('sys').executable, str(ROOT / 'scripts/validate.py')], check=True)
version = (ROOT / 'VERSION').read_text().strip()
if not __import__('re').fullmatch(r'\d+\.\d+\.\d+', version):
    raise SystemExit('VERSION must be major.minor.patch')
files = project_files()
dest = ROOT / 'dist'; dest.mkdir(exist_ok=True)
archive = dest / f'obsidian-web-clipper-v{version}.zip'
head = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip() or None
manifest = {'version': version, 'git_commit': head, 'files': []}
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        data = path.read_bytes()
        manifest['files'].append({'path': rel, 'size': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, data)
manifest_file = dest / 'release-manifest.json'
manifest_file.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
checksums = dest / 'SHA256SUMS.txt'
checksums.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n' for p in [archive, manifest_file]), encoding='utf-8')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == {x['path'] for x in manifest['files']}
    for entry in manifest['files']:
        assert hashlib.sha256(z.read(entry['path'])).hexdigest() == entry['sha256']
print(f'Created {archive.name}: {len(files)} files, {archive.stat().st_size} bytes; manifest and checksums verified.')
