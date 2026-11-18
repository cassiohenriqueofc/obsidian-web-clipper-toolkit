# Git e versões

[English](../en-US/development.md) · [Início](../../README.pt-BR.md)

O ZIP é uma fotografia sem histórico .git. Para desenvolver, faça clone em uma
pasta vazia, separada da cópia extraída. Autentique pelo gerenciador de credenciais
ou GitHub CLI; não coloque tokens no endereço remoto.

```powershell
gh auth login
$gitProject = Join-Path $HOME "Projects\obsidian-web-clipper-git"
git clone https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit.git $gitProject
Set-Location -LiteralPath $gitProject
py -3 scripts/validate.py
```

```bash
gh auth login
git clone https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit.git "$HOME/Projects/obsidian-web-clipper-git"
cd "$HOME/Projects/obsidian-web-clipper-git"
python3 scripts/validate.py
```

Copie seu endereço noreply exato em GitHub Settings → Emails e configure-o apenas
no repositório local:

```bash
git config user.name "YOUR_GITHUB_HANDLE"
git config user.email "YOUR_GITHUB_NOREPLY_ADDRESS"
git switch -c feat/improve-template
python3 scripts/validate.py
git diff
git add templates/01-balanced-original-callout-clipper.json CHANGELOG.md
git diff --cached
git commit -m "feat: clarify source evidence instructions"
git push -u origin feat/improve-template
```

Abra um pull request. Não use force-push na main. A política escrita não equivale
a uma proteção aplicada pelo GitHub; veja project/repository-protection.md.

Atualize VERSION, os dois READMEs e CHANGELOG.md, gere o site e o pacote:

```powershell
py -3 scripts/build_site.py
py -3 scripts/validate.py
py -3 scripts/package_release.py
```

```bash
python3 scripts/build_site.py
python3 scripts/validate.py
python3 scripts/package_release.py
```

Os arquivos saem em dist/, ignorada pelo Git. Revise antes de publicar. Use tags
novas por versão; não substitua tags publicadas. O [guia completo](../en-US/development.md)
inclui comandos de tag e release. Uma release privada exige acesso ao repositório
e não autoriza mudar sua visibilidade ou publicar o site.
