# Publicación e indexación

[English](../en-US/publishing.md) · [Inicio](../../README.md)

## Estado actual

El propietario autorizó la publicación e indexación en `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`. El workflow está configurado, pero GitHub Actions no se ha iniciado por un bloqueo de facturación de la cuenta. El sitio aún no está publicado. No envíes el sitemap ni afirmes que se ha indexado hasta verificar una publicación correcta.

## Metadatos generados

La compilación indexable genera un título y una descripción por idioma, canonical absoluto, `hreflang` y `x-default`, Open Graph, Twitter y JSON-LD `SoftwareSourceCode`. La imagen social estática mide 1200 × 630; el GIF es independiente. El selector de idioma y el 404 usan `noindex,follow` y no se incluyen en el sitemap. `robots.txt` permite el rastreo e indica el sitemap. `lastmod` usa la fecha revisada de la Propuesta; actualízala cuando cambie el contenido del proyecto.

Estas señales ayudan a los buscadores a entender y mostrar las páginas, pero no garantizan posiciones, indexación ni resultados enriquecidos. `llms.txt` es un índice para clientes compatibles, no un factor de posicionamiento de Google.

## Generar y verificar

```bash
python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable
python3 scripts/validate.py
```

Cuando se resuelva el bloqueo de Actions, ejecuta el workflow y revisa los siete idiomas, `robots.txt`, el sitemap y el 404. Verifica la propiedad en Google Search Console y Bing Webmaster Tools antes de enviar el sitemap publicado. Los tokens de verificación no se guardan en este repositorio. La descripción About, los temas y la imagen social de GitHub son ajustes independientes y siguen pendientes.
