"""Copy the portable project policy into an existing local vault; never overwrite."""
import argparse
import shutil
from pathlib import Path
from common import ROOT

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--vault-root',type=Path,required=True)
a=p.parse_args()
if not a.vault_root.is_dir():p.error('The vault directory must already exist')
target=a.vault_root/'aimemory'/'project-defaults.md'
if target.exists():p.error('Memory note already exists; review and merge it manually')
target.parent.mkdir(exist_ok=True)
shutil.copyfile(ROOT/'aimemory/project-defaults.md',target)
print('Installed aimemory/project-defaults.md. Load this note when starting future projects; account-wide OpenAI settings are unchanged.')
