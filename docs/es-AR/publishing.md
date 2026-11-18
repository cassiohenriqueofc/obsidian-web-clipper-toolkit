# Publicación y metadatos

Probá la vista local primero. La publicación y los cambios de visibilidad requieren aprobación separada. El sitio usa noindex por defecto. Indicá la URL HTTPS real y aprobada para generar canonical, Open Graph, hreflang y sitemap. Los archivos llms no garantizan posicionamiento.

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Usá datos de demostración. Excluí configuraciones locales, credenciales, notas privadas y rutas personales. Un repositorio privado no protege un secreto ya incorporado al historial. El titular autorizó únicamente la atribución indicada abajo.

[Guía del proyecto](guide.md)

El README es Markdown renderizado; los metadatos Open Graph, Twitter, canonical y
JSON-LD pertenecen al sitio generado. La imagen compacta para la vista previa está
en [assets/social-preview.jpg](../../assets/social-preview.jpg). Si querés,
subila en GitHub Settings → Social preview. Los nombres de los topics de GitHub
son públicos incluso si el repositorio es privado; esperá la aprobación antes de
agregarlos. Google indica que llms.txt no cambia la visibilidad ni el ranking en
Google Search y que la búsqueda con IA no requiere un schema especial.
