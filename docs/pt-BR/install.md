# Instalação e uso

[Português](install.md) · [English](../en-US/install.md) · [Início](../../README.pt-BR.md)

Instale o [Obsidian](https://obsidian.md/download) e o [Web Clipper oficial](https://obsidian.md/clipper)
em um navegador compatível. Consulte a lista atual de navegadores na página oficial.
Python 3.10+ é necessário apenas para os utilitários; a importação de JSON não precisa dele.
Use um modelo acessível para os estilos com IA; Archive não depende de provedor.

## Windows

Baixe o ZIP da versão e SHA256SUMS.txt no GitHub autenticado. Compare o hash antes
de extrair em uma pasta vazia ou previamente copiada para backup:

```powershell
$archive = Join-Path $HOME "Downloads\obsidian-web-clipper-v0.1.3.zip"
Get-FileHash -Algorithm SHA256 -LiteralPath $archive
$projectDir = Join-Path $env:LOCALAPPDATA "Programs\Demo Notes\obsidian-web-clipper"
New-Item -ItemType Directory -Force -Path $projectDir | Out-Null
Expand-Archive -LiteralPath $archive -DestinationPath $projectDir
Set-Location -LiteralPath $projectDir
py -3 scripts/validate.py
py -3 scripts/configure_templates.py --vault "Demo Vault" --folder "clippings"
```

Troque a pasta demonstrativa pela sua. A extração não usa -Force para evitar
sobrescrever uma versão existente silenciosamente. A pasta do projeto não se
torna automaticamente um cofre do Obsidian.

## macOS

Use o instalador oficial .dmg e a extensão correspondente ao navegador escolhido.
Safari é específico do macOS. Em uma pasta nova:

```bash
mkdir -p "$HOME/Projects/obsidian-web-clipper"
cd "$HOME/Projects/obsidian-web-clipper"
shasum -a 256 "$HOME/Downloads/obsidian-web-clipper-v0.1.3.zip"
# Compare com o checksum da versão.
unzip -n "$HOME/Downloads/obsidian-web-clipper-v0.1.3.zip"
python3 scripts/validate.py
python3 scripts/configure_templates.py --vault 'Demo Vault' --folder 'clippings'
```

## Linux

Escolha o pacote adequado na página oficial. Instale a extensão em um navegador
compatível. Com Python 3.10+ e unzip disponíveis:

```bash
mkdir -p "$HOME/Projects/obsidian-web-clipper"
cd "$HOME/Projects/obsidian-web-clipper"
sha256sum "$HOME/Downloads/obsidian-web-clipper-v0.1.3.zip"
# Compare com o checksum da versão.
unzip -n "$HOME/Downloads/obsidian-web-clipper-v0.1.3.zip"
python3 scripts/validate.py
python3 scripts/configure_templates.py --vault 'Demo Vault' --folder 'clippings'
```

Respeite maiúsculas e minúsculas nos nomes das pastas. Estes são procedimentos
documentados; não foram executados como instalação completa nos três sistemas.

## Configuração e captura

1. Abra o cofre e crie sua pasta `clippings`.
2. Importe um JSON pelo importador de templates da extensão.
3. Confira o cofre e a pasta no painel; a reexportação do 1.7.1 pode omitir o cofre.
4. Configure provedor/modelo nas opções locais. Desative a execução automática.
5. Abra a página, escolha o template, clique manualmente em Interpret, revise e salve.
6. Use Archive sem Interpreter quando não quiser IA. Não salve prompts não resolvidos.

As cópias personalizadas ficam em local-only/templates, ignorada pelo Git.
Não copie chaves de API para o terminal, exemplos, issues ou configurações versionadas.

## Segundo cofre, atualização e backup

A cópia entre cofres é manual nesta versão. Copie o arquivo Markdown já salvo
para manter a mesma análise, verificando se o destino já existe:

```powershell
$sourceFile = Read-Host "Caminho completo do Markdown salvo"
$destinationDir = Read-Host "Pasta existente no segundo cofre"
if (!(Test-Path -LiteralPath $sourceFile -PathType Leaf)) { throw "Origem ausente" }
if (!(Test-Path -LiteralPath $destinationDir -PathType Container)) { throw "Destino ausente" }
$targetFile = Join-Path $destinationDir (Split-Path $sourceFile -Leaf)
if (Test-Path -LiteralPath $targetFile) { throw "Arquivo já existe; revise primeiro" }
Copy-Item -LiteralPath $sourceFile -Destination $targetFile
```

No macOS/Linux, substitua os caminhos demonstrativos:

```bash
source_file='/path/to/first-vault/clippings/example.md'
destination_dir='/path/to/second-vault/Clippings'
test -f "$source_file" && test -d "$destination_dir" || exit 1
target_file="$destination_dir/$(basename "$source_file")"
test ! -e "$target_file" || { printf '%s\n' 'Destino existente; revise'; exit 1; }
cp -n -- "$source_file" "$target_file"
```

Antes de atualizar, exporte seus templates para backup privado. Importe a nova
versão separadamente e teste uma página pequena antes de remover a anterior.
O ZIP não contém histórico .git; use clone para desenvolvimento versionado.
