# Publicación e indexación

[English](../en-US/publishing.md) · [Inicio](../../README.md)

GitHub Pages está configurado para `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`. El workflow genera el sitio en siete idiomas con canonical, Open Graph/Twitter, JSON-LD, sitemap y robots indexable, y lo publica después de cada push a `main`. Verifica que la primera ejecución de Actions concluya correctamente antes de considerar que el sitio está disponible.

Para reconstruir localmente: `python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable`. El generador no publica; GitHub Actions realiza el despliegue.

La imagen Open Graph es estática (`assets/social-preview.jpg`); el GIF explicativo es independiente. El About, los temas y la imagen social de GitHub se administran en Settings; la conexión actual no puede modificarlos.
