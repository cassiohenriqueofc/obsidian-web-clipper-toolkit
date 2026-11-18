# Guia do projeto

[English (US)](../en-US/guide.md) · [Português (Brasil)](../pt-BR/guide.md) · [Español (Argentina)](../es-AR/guide.md) · [Español (México)](../es-MX/guide.md) · [Español (España)](../es-ES/guide.md) · [Deutsch](../de-DE/guide.md) · [Français](../fr-FR/guide.md)

Atualizado: 2026-11-18 · 0.1.3 · Versão pública · GitHub Pages configurado

## Objetivo

Use JSON e Markdown portáveis, revise sugestões da IA, preserve evidências e mantenha uma alternativa sem IA.

## Instalação

Instale o Obsidian e o Web Clipper oficial em um navegador compatível. Crie a pasta no cofre, importe um template e confira cofre e destino. Mantenha a execução automática desativada. Nos estilos com IA, clique manualmente em Interpret, revise e salve. No Archive, não execute o Interpreter.

```powershell
# Windows — project root
py -3 scripts/configure_templates.py --vault "Demo Vault" --folder "clippings"
py -3 scripts/build_site.py
py -3 scripts/validate.py
```

```bash
# macOS / Linux — project root
python3 scripts/configure_templates.py --vault 'Demo Vault' --folder 'clippings'
python3 scripts/build_site.py
python3 scripts/validate.py
```

## Desenvolvimento

Para projetos, use clone Git local e repositório privado no GitHub. Use branches, commits factuais, revisão de diffs e changelog datado. Não crie repositórios para tarefas cotidianas ou conversas simples.

## Privacidade

Use dados demonstrativos. Ignore configurações locais, credenciais, notas privadas e caminhos pessoais. Um repositório privado não torna seguro um segredo versionado. O titular autorizou somente a atribuição indicada abaixo.

## Licença

Licença de código disponível para uso não comercial. Uso comercial depende de autorização separada. Versões modificadas compartilhadas exigem código correspondente, atribuição, mesma licença e registro datado. Alterações privadas não precisam ser publicadas. Não é open source aprovado pela OSI. A LICENSE inglesa é a válida.

## Fontes e atribuição

Use links Markdown com URLs verificadas no GitHub e wikilinks separados para notas existentes no Obsidian. Registre URL, revisão, licença, arquivos reutilizados e alterações antes da distribuição. Não invente créditos nem compatibilidade de licenças.

## Modelo reutilizável de projeto

Edite o frontmatter simples de project-template/Proposal.md. Gere uma pasta nova e vazia com new_project.py. O gerador não cria remoto, não envia commits, não publica site e não implementa a aplicação. Revise nome, contato, URLs e licença antes de publicar.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

## Armazenamento local e remoto

Mantenha o clone local completo e o remoto privado. Faça commit e push após revisar: o GitHub não sincroniza arquivos automaticamente. Faça backup separado das configurações ignoradas. Para economizar espaço, remova ZIPs duplicados e prévias descartáveis, não templates ou scripts.

## Publicação e metadados

O workflow do GitHub Pages está configurado para https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/. A primeira execução deve concluir para o site ser considerado publicado. A versão publicada usa canonical, Open Graph/Twitter, hreflang, JSON-LD, sitemap e robots indexável. Arquivos llms não garantem ranking.

## Validação e limites

Estrutura dos templates, links, padrões de privacidade, pacote e interações da página são verificados localmente. Os testes isolados anteriores do renderizador 1.7.1 passaram. Provedor real, gravação na extensão e testes completos nos três sistemas continuam pendentes.

O conteúdo original pode representar seleção ou destaques. O contexto da IA tem limites. O Clipper 1.7.1 pode reprocessar expressões literais nos estilos com IA; prefira Archive sem Interpreter nesses casos. A cópia automática entre cofres não está implementada.

Cada arquivo novo deve indicar função real, classificação dos dados, fonte quando aplicável e validação relevante. Notas usam YAML simples; código usa um cabeçalho útil e curto. Comentários explicam motivos e restrições, sem repetir o código. Não invente testes ou resultados.

**Desenvolvido por:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)
