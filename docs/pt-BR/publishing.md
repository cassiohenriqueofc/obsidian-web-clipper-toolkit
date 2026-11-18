# Publicação e indexação

[English](../en-US/publishing.md) · [Início](../../README.md)

## Estado atual

O proprietário autorizou a publicação e indexação em `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`. O workflow está configurado, mas o GitHub Actions não iniciou por um bloqueio de cobrança da conta. O site ainda não está no ar. Não envie o sitemap nem afirme que houve indexação antes de confirmar uma publicação bem-sucedida.

## Metadados gerados

O build indexável cria título e descrição por idioma, canonical absoluto, `hreflang` e `x-default`, Open Graph, Twitter e JSON-LD `SoftwareSourceCode`. A imagem social estática mede 1200 × 630; o GIF é separado. A página de idioma e o 404 usam `noindex,follow` e ficam fora do sitemap. `robots.txt` permite rastreamento e aponta para o sitemap. `lastmod` usa a data revisada da Proposta; atualize-a quando o conteúdo do projeto mudar.

Esses sinais ajudam os mecanismos a entender e exibir as páginas, mas não garantem posição, indexação ou resultados avançados. `llms.txt` é um índice para clientes compatíveis, não um fator de posição do Google.

## Gerar e conferir

```bash
python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable
python3 scripts/validate.py
```

Depois que o bloqueio do Actions for resolvido, execute o workflow e confira as sete páginas, `robots.txt`, sitemap e 404. Verifique o domínio no Search Console e Bing Webmaster Tools antes de enviar o sitemap publicado. Tokens de verificação não ficam neste repositório. A descrição About, os tópicos e a imagem social do GitHub são configurações separadas e continuam pendentes.
