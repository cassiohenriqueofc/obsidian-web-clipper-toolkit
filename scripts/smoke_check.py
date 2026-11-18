"""Check scaffold generation, refusal to overwrite, privacy rejection and portable memory install."""
import ast
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from common import ROOT

scratch=ROOT/'local-only';scratch.mkdir(exist_ok=True)
def run(script,*args):
    return subprocess.run([sys.executable,str(ROOT/'scripts'/script),*map(str,args)],capture_output=True,text=True)
with tempfile.TemporaryDirectory(dir=scratch) as tmp:
    base=Path(tmp);out=base/'generated'
    result=run('new_project.py','--proposal',ROOT/'project-template/Proposal.md','--output',out)
    assert result.returncode==0,result.stderr
    assert run('new_project.py','--output',out).returncode!=0
    metadata=json.loads((out/'metadata.jsonld').read_text())
    assert 'url' not in metadata and 'codeRepository' not in metadata
    assert len(list(out.glob('README*.md')))==7
    for path in out.rglob('*'):
        if path.is_file():assert '{{' not in path.read_text(),path
    ast.parse((out/'source.py').read_text())
    assert (out/'LICENSE').read_text()==(out/'LICENSE.md').read_text()
    clean=subprocess.run([sys.executable,str(out/'scripts/check_privacy.py')],capture_output=True)
    assert clean.returncode==0,clean.stdout
    fixture=out/'credential-fixture.txt';fixture.write_text('sk-'+('A'*30))
    rejected=subprocess.run([sys.executable,str(out/'scripts/check_privacy.py')],capture_output=True)
    assert rejected.returncode!=0
    fixture.unlink()
    vault=base/'demo-vault';vault.mkdir()
    assert run('install_memory.py','--vault-root',vault).returncode==0
    assert (vault/'aimemory/project-defaults.md').exists()
    assert run('install_memory.py','--vault-root',vault).returncode!=0
    assert run('configure_templates.py','--vault','Demo Vault','--folder','../outside').returncode!=0
print('PASS: fresh seven-locale scaffold, null URL omission, resolved variables, valid Python, overwrite refusal, privacy fixture rejection, memory install and traversal rejection.')
