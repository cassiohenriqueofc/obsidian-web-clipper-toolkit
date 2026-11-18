"""Build a multilingual static documentation/file map; no deployment or network calls."""
import argparse
import html
import json
import shutil
from pathlib import Path
from urllib.parse import quote, urlsplit
from common import ROOT, project_files

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--base-url',default='')
p.add_argument('--indexable',action='store_true')
a=p.parse_args()
if a.base_url:
    u=urlsplit(a.base_url)
    if u.scheme!='https' or not u.netloc or u.query or u.fragment:
        p.error('Use an absolute HTTPS base URL without query or fragment')
if a.indexable and not a.base_url:
    p.error('--indexable requires an approved real --base-url')
base=a.base_url.rstrip('/')+'/' if a.base_url else ''
site=ROOT/'site';site.mkdir(exist_ok=True)
(site/'assets').mkdir(exist_ok=True)
shutil.copyfile(ROOT/'assets/banner.png',site/'assets/banner.png')
shutil.copyfile(ROOT/'web/site.css',site/'assets/site.css')
shutil.copyfile(ROOT/'web/site.js',site/'assets/site.js')
repo='https://github.com/cassiohenriqueofc/obsidian-web-cliper'
blob=repo+'/blob/main/'
version=(ROOT/'VERSION').read_text().strip()
texts={
 'en-US':dict(title='Web to notes. With the source.',desc='English Web Clipper templates, deliberate manual interpretation, preserved source content, and portable Markdown.',language='Language',intro='Capture · Interpret · Keep',start='Read the guide',download='Release ZIP',flow='From a page to a durable note',pause='Pause animation',resume='Resume animation',files='Every release file, connected',private='Private review release · Public hosting not enabled',access='Repository links require GitHub access while the repository is private.',summary='Three layouts. One portable workflow.',cards=[('Balanced','Six prompts, explained insights, project brief and collapsed original content.'),('Compact','Four prompts and an original-content block near the footer.'),('Archive','No AI dependency; keep the content supplied by Clipper.')],steps=[('Page','Current extraction, selection, or highlights','references/README.md'),('Template','Choose metadata, callouts and source placement','templates/01-balanced-original-callout-clipper.json'),('Interpret','Run manually; inspect uncertain claims','docs/en-US/prompt-map.md'),('Markdown','Keep the supplied source and interactive tasks','examples/01-balanced-original-callout-example.md'),('Git','Review changes and preserve versions','CHANGELOG.md')],groups={'root':'Project','templates':'Templates','docs':'Documentation','examples':'Examples','project':'Plan and review','scripts':'Utilities','assets':'Artwork','web':'Website source','site':'Built website','.github':'GitHub automation','references':'References'},footer='Community project. Not affiliated with Obsidian. Noncommercial source-available license. Updated November 18, 2026.'),
 'pt-BR':dict(title='Da web para notas. Com a fonte.',desc='Templates em inglês, interpretação manual com controle, conteúdo original preservado e Markdown portável.',language='Idioma',intro='Capturar · Interpretar · Preservar',start='Ler o guia',download='ZIP da versão',flow='Da página a uma nota durável',pause='Pausar animação',resume='Retomar animação',files='Todos os arquivos da versão, conectados',private='Versão privada para revisão · Hospedagem pública desativada',access='Os links do repositório exigem acesso ao GitHub enquanto ele for privado.',summary='Três formatos. Um fluxo portável.',cards=[('Balanced','Seis prompts, explicações, briefing e fonte recolhida.'),('Compact','Quatro prompts e conteúdo original perto do rodapé.'),('Archive','Sem dependência de IA; preserve o conteúdo fornecido pelo Clipper.')],steps=[('Página','Extração, seleção ou destaques atuais','references/README.md'),('Template','Metadados, callouts e posição da fonte','templates/01-balanced-original-callout-clipper.json'),('Interpretar','Execute manualmente; revise incertezas','docs/pt-BR/prompt-map.md'),('Markdown','Fonte preservada e tarefas interativas','examples/01-balanced-original-callout-example.md'),('Git','Revise mudanças e controle versões','CHANGELOG.md')],groups={'root':'Projeto','templates':'Templates','docs':'Documentação','examples':'Exemplos','project':'Plano e revisão','scripts':'Utilitários','assets':'Ilustração','web':'Fonte do site','site':'Site gerado','.github':'Automação GitHub','references':'Referências'},footer='Projeto da comunidade, sem vínculo com a Obsidian. Licença não comercial de código disponível. Atualizado em 18 de novembro de 2026.')
}
translations=json.loads((ROOT/'web/documentation-locales.json').read_text(encoding='utf-8'))
for lang,translation in translations.items():
    if lang in texts:
        continue
    texts[lang]=dict(title='Web → Notes',desc=translation['intro'],language=translation['language'],intro=translation['readme'],start=translation['title'],download='ZIP',flow=translation['flow'],pause=translation['pause'],resume=translation['resume'],files=translation['map'],private=translation['status'],access=translation['access'],summary=translation['deliveries'],cards=[('Balanced','6 prompts'),('Compact','4 prompts'),('Archive','0 prompts')],steps=[(translation['headings'][0],translation['intro'],'references/README.md'),('Template','JSON','templates/01-balanced-original-callout-clipper.json'),('Interpreter',translation['headings'][9],f'docs/{lang}/prompt-map.md'),('Markdown','Source','examples/01-balanced-original-callout-example.md'),('Git',translation['headings'][2],'CHANGELOG.md')],groups=texts['en-US']['groups'],footer=translation['status']+' · 2026-11-18')
known=['site/index.html','site/file-index.json','site/robots.txt','site/llms.txt','site/llms-full.txt','site/assets/banner.png','site/assets/site.css','site/assets/site.js']+[f'site/{lang}/index.html' for lang in texts]
if base:known.append('site/sitemap.xml')
else:
    (site/'sitemap.xml').unlink(missing_ok=True)
inventory=sorted({x.relative_to(ROOT).as_posix() for x in project_files()}|set(known))
(site/'file-index.json').write_text(json.dumps(inventory,indent=2)+'\n',encoding='utf-8')
for lang,t in texts.items():
    directory=site/lang;directory.mkdir(exist_ok=True)
    locale=lang.replace('-','_')
    robots='index,follow' if a.indexable else 'noindex,nofollow'
    metadata=''
    schema={'@context':'https://schema.org','@type':'SoftwareSourceCode','name':'Obsidian Web Clipper Toolkit','description':t['desc'],'version':version,'programmingLanguage':['JSON','Markdown','Python'],'inLanguage':lang,'codeRepository':repo,'dateModified':'2026-11-18','isAccessibleForFree':True,'author':{'@type':'Person','name':'Cassio Henrique','email':'mailto:cassiohenriqueofc@gmail.com'},'publisher':{'@type':'Organization','name':'Múltipla Tecnologia'}}
    if base:
        url=base+lang+'/'
        metadata=f'<link rel="canonical" href="{html.escape(url,quote=True)}"><meta property="og:url" content="{html.escape(url,quote=True)}"><meta property="og:image" content="{html.escape(base,quote=True)}assets/banner.png"><meta name="twitter:image" content="{html.escape(base,quote=True)}assets/banner.png">'
        metadata+=''.join(f'<link rel="alternate" hreflang="{other}" href="{html.escape(base,quote=True)}{other}/">' for other in texts)
        schema['url']=url
    groups={}
    for file in inventory:
        group='/'.join(file.split('/')[:2]) if file.startswith('docs/') else (file.split('/')[0] if '/' in file else 'root')
        groups.setdefault(group,[]).append(file)
    catalog=''
    for group,names in groups.items():
        links=''.join(f'<li><a href="{blob+quote(file,safe="/")}">{html.escape(file)}</a></li>' for file in names)
        catalog+=f'<div class="file-group"><h3>{html.escape(t["groups"].get(group,group))}</h3><ul class="files">{links}</ul></div>'
    steps=''.join(f'<div class="step"><div class="number">0{i+1}</div><strong>{label}</strong><span>{description}</span><a href="{blob+path}">{html.escape(Path(path).name)}</a></div>' for i,(label,description,path) in enumerate(t['steps']))
    facts=''.join(f'<div class="fact"><h3>{title}</h3><p class="muted">{description}</p></div>' for title,description in t['cards'])
    other='pt-BR' if lang=='en-US' else 'en-US'
    language_options=''.join(f'<option value="{key}" '+('selected' if key==lang else '')+f'>{value["name"]}</option>' for key,value in translations.items())
    content=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Obsidian Web Clipper Toolkit — {t['title']}</title><meta name="description" content="{t['desc']}"><meta name="robots" content="{robots}"><meta property="og:title" content="Obsidian Web Clipper Toolkit"><meta property="og:description" content="{t['desc']}"><meta property="og:type" content="website"><meta property="og:locale" content="{locale}"><meta property="og:image:width" content="1774"><meta property="og:image:height" content="887"><meta name="twitter:card" content="summary_large_image">{metadata}<link rel="stylesheet" href="../assets/site.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><script src="../assets/site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="../{lang}/">WEB → NOTES <span class="muted">/ {version}</span></a><nav aria-label="Menu"><a href="{repo}">GitHub</a><a href="../{other}/">{'Português' if other=='pt-BR' else 'English'}</a><label for="language">{t['language']}<select id="language">{language_options}</select></label></nav></header>
<main id="main"><section class="hero"><div><div class="eyebrow">{t['intro']}</div><h1>{t['title']}</h1><p class="muted">{t['desc']}</p><div class="actions"><a class="button primary" href="{blob}docs/{lang}/install.md">{t['start']}</a><a class="button" href="{repo}/releases/tag/v{version}">{t['download']}</a></div></div><img class="banner" src="../assets/banner.png" width="1774" height="887" alt="Browser page transformed into structured Markdown notes and a knowledge graph"></section>
<section><p class="eyebrow">{t['private']}</p><h2>{t['summary']}</h2><div class="facts">{facts}</div></section>
<section aria-labelledby="flow"><div class="section-head"><h2 id="flow">{t['flow']}</h2><button id="pause" type="button" aria-pressed="false" data-pause="{t['pause']}" data-resume="{t['resume']}">{t['pause']}</button></div><div class="workflow">{steps}</div></section>
<section aria-labelledby="files"><h2 id="files">{t['files']}</h2><p class="muted">{t['access']}</p><div class="catalog">{catalog}</div></section></main><footer>{t['footer']} <a href="{blob}LICENSE">License</a> · <a href="../llms.txt">llms.txt</a> · <a href="../llms-full.txt">llms-full.txt</a><p>{translations[lang]['contact']}: Cassio Henrique · Múltipla Tecnologia · <a href="mailto:cassiohenriqueofc@gmail.com">cassiohenriqueofc@gmail.com</a></p></footer></body></html>'''
    (directory/'index.html').write_text(content,encoding='utf-8')
(site/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>Choose language</title></head><body>'+ ' · '.join(f'<a href="{lang}/">{t["name"]}</a>' for lang,t in translations.items())+'</body></html>',encoding='utf-8')
(site/'robots.txt').write_text('User-agent: *\n'+('Allow: /\nSitemap: '+base+'sitemap.xml\n' if a.indexable else 'Disallow: /\n'),encoding='utf-8')
overview='# Obsidian Web Clipper Toolkit\n\n> English manual-Interpreter templates, original content retention, and multilingual documentation. Version '+version+'.\n\nPrivate review release. No live provider/OS acceptance claim. No automatic second-vault copy. Noncommercial source-available license.\n\n'
overview+='\n'.join(f'- [{lang} documentation]({base+lang+"/" if base else lang+"/"})' for lang in texts)
overview+='\n- [Repository]('+repo+')\n- [License]('+blob+'LICENSE)\n- [Handoff]('+blob+'handoff.md)\n'
(site/'llms.txt').write_text(overview,encoding='utf-8')
(site/'llms-full.txt').write_text(overview+'\n\n'+(ROOT/'README.md').read_text(encoding='utf-8')+'\n\n'+(ROOT/'project/capture-spec.md').read_text(encoding='utf-8'),encoding='utf-8')
if base:
    (site/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(base+lang+'/')+'</loc></url>' for lang in texts)+'</urlset>',encoding='utf-8')
print(f'Built multilingual site with {len(inventory)} linked files. Indexable: {a.indexable}. Public deployment: not performed.')
