# Publicación y metadatos

Revisa la vista local primero. Publicar y cambiar la visibilidad requiere aprobación separada. El sitio usa noindex por defecto. Indica la URL HTTPS real y aprobada para generar canonical, Open Graph, hreflang y sitemap. Los archivos llms no garantizan posicionamiento.

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Usa datos de demostración. Excluye configuraciones locales, credenciales, notas privadas y rutas personales. Un repositorio privado no protege un secreto incorporado al historial. El titular autorizó únicamente la atribución indicada abajo.

[Guía del proyecto](guide.md)
