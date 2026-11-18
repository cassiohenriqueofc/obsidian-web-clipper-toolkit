# Publicação e indexação

[English](../en-US/publishing.md) · [Início](../../README.md)

O GitHub Pages está configurado em `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`. O workflow gera o site em sete idiomas com canonical, Open Graph/Twitter, JSON-LD, sitemap e robots indexável, e publica após cada push para `main`. Confirme a primeira execução do Actions antes de considerar o site disponível.

Para gerar localmente: `python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable`. O script não publica; o GitHub Actions faz o deploy.

A imagem Open Graph é estática (`assets/social-preview.jpg`); o GIF explicativo é independente. A descrição About, os tópicos e a imagem social do GitHub são configurados em Settings; a conexão atual não pode alterá-los.
