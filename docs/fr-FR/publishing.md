# Publication et indexation

[English](../en-US/publishing.md) · [Accueil](../../README.md)

GitHub Pages est configuré à l’adresse `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`. Le workflow construit le site en sept langues avec les URL canoniques, Open Graph/Twitter, JSON-LD, un sitemap et des règles robots indexables, puis le publie après chaque push sur `main`. Vérifiez la première exécution Actions avant de considérer le site disponible.

Build local : `python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable`. Le script ne publie pas ; GitHub Actions déploie le site.

L’image Open Graph est statique (`assets/social-preview.jpg`) ; le GIF explicatif est distinct. La description About, les sujets et l’image sociale GitHub se gèrent dans Settings ; la connexion actuelle ne peut pas les modifier.
