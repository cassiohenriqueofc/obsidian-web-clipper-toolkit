"""Render a clean project scaffold from Proposal.md, never overwrite an existing project."""
import argparse
import datetime
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from common import ROOT

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--proposal',type=Path,default=ROOT/'project-template/Proposal.md')
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
text=a.proposal.read_text(encoding='utf-8')
if not text.startswith('---\n') or '\n---\n' not in text[4:]:
    p.error('Proposal.md must start with flat YAML frontmatter')
front=text.split('---\n',2)[1]
values={}
for line in front.splitlines():
    if not line.strip() or line.lstrip().startswith('#'):continue
    if ':' not in line:p.error('Each frontmatter line must be key: JSON scalar')
    key,value=line.split(':',1)
    if not re.fullmatch(r'[a-z][a-z0-9_]*',key) or key in values:p.error('Invalid or duplicate key')
    try:values[key]=json.loads(value.strip())
    except ValueError:p.error(f'{key}: use a JSON-compatible scalar')
    if isinstance(values[key],(dict,list)):p.error(f'{key}: nested values are not supported')
required={'project_name','project_slug','summary','version','date','default_language','author_name','company_name','contact_email','repository_url','landing_page_url','content_type','license_id','data_classification'}
if set(values)!=required:p.error('Proposal fields must match the provided variable contract')
for key in required-{'repository_url','landing_page_url'}:
    if not isinstance(values[key],str) or not values[key].strip() or any(ord(c)<32 for c in values[key]):p.error(f'{key}: require a nonempty single-line string')
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',values['project_slug']):p.error('Use a lowercase hyphenated project_slug')
if not re.fullmatch(r'\d+\.\d+\.\d+',values['version']):p.error('Use major.minor.patch')
try:datetime.date.fromisoformat(values['date'])
except ValueError:p.error('Use a real ISO date')
if values['default_language']!='en-US':p.error('This starter uses en-US as its default language')
if values['data_classification']!='demo-only':p.error('Scaffolds must begin with demo-only data')
if values['license_id']!='LicenseRef-Noncommercial-Source-Available-1.0':p.error('This starter includes the selected noncommercial license; a different license needs separate review')
if values['content_type'] not in {'SoftwareSourceCode','CreativeWork','WebSite','TechArticle'}:p.error('Use a supported Schema.org content_type')
for key in ['repository_url','landing_page_url']:
    if values[key] is not None:
        parsed=urlsplit(values[key])
        if parsed.scheme!='https' or not parsed.netloc or parsed.username or parsed.password:p.error(f'{key}: use a real approved HTTPS URL or null')
if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',values['contact_email']):p.error('Use the approved public contact email')
if a.output.exists() and any(a.output.iterdir()):p.error('Output must be absent or empty; refusing to overwrite')
render_values=dict(values)
for key,value in values.items():render_values[key+'_json']=json.dumps(value,ensure_ascii=False)
pending={}
for path in (ROOT/'project-template').rglob('*.tmpl'):
    def substitute(match):
        key=match.group(1)
        if key not in render_values:raise ValueError('Unknown template variable '+key)
        return '' if render_values[key] is None else str(render_values[key])
    try:pending[path.relative_to(ROOT/'project-template').as_posix()[:-5]]=re.sub(r'\{\{([a-z_]+)\}\}',substitute,path.read_text(encoding='utf-8'))
    except ValueError as exc:p.error(str(exc))
license_text=(ROOT/'LICENSE').read_text(encoding='utf-8')
pending['LICENSE.md']=pending.get('LICENSE.md',license_text)
pending['LICENSE']=pending['LICENSE.md']
pending['Proposal.md']=text
metadata={'@context':'https://schema.org','@type':values['content_type'],'name':values['project_name'],'description':values['summary'],'version':values['version'],'dateModified':values['date'],'inLanguage':['en-US','pt-BR','es-AR','es-MX','es-ES','de-DE','fr-FR'],'author':{'@type':'Person','name':values['author_name'],'email':'mailto:'+values['contact_email']},'publisher':{'@type':'Organization','name':values['company_name']}}
if values['repository_url']:metadata['codeRepository']=values['repository_url']
if values['landing_page_url']:metadata['url']=values['landing_page_url']
pending['metadata.jsonld']=json.dumps(metadata,ensure_ascii=False,indent=2)+'\n'
pending['PRIVACY.md']='Only explicitly approved public attribution may be published. Keep personal configuration in local-only/. Review staged files and commit identity before pushing.\n'
a.output.mkdir(parents=True,exist_ok=True)
for name,content in pending.items():
    target=a.output/name
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(content,encoding='utf-8')
print(f'Generated {len(pending)} scaffold files. No repository was created and no code was implemented. Review public attribution, URLs, license and notices before committing.')
