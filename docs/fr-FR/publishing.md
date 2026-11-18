# Publication et indexation

[English](../en-US/publishing.md) · [Accueil](../../README.md)

## État actuel

Le propriétaire a autorisé la publication et l’indexation à l’adresse `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`. Le workflow est configuré, mais GitHub Actions n’a pas démarré en raison d’un blocage de facturation du compte. Le site n’est pas encore publié. N’envoyez pas le sitemap et n’annoncez pas d’indexation avant d’avoir vérifié une publication réussie.

## Métadonnées générées

La compilation indexable produit un titre et une description par langue, des URL canoniques absolues, `hreflang` et `x-default`, les métadonnées Open Graph et Twitter, ainsi que le JSON-LD `SoftwareSourceCode`. L’image sociale statique mesure 1200 × 630 ; le GIF est séparé. Le sélecteur de langue et la page 404 utilisent `noindex,follow` et ne figurent pas dans le sitemap. `robots.txt` autorise l’exploration et indique le sitemap. `lastmod` reprend la date vérifiée du Proposal ; mettez-la à jour si le contenu documenté du projet change.

Ces signaux aident les moteurs à comprendre et présenter les pages, sans garantir classement, indexation ou résultats enrichis. `llms.txt` est un index destiné aux clients compatibles, pas un facteur de classement Google.

## Générer et vérifier

```bash
python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable
python3 scripts/validate.py
```

Après la levée du blocage Actions, lancez le workflow et vérifiez les sept langues, `robots.txt`, le sitemap et la page 404. Vérifiez la propriété dans Google Search Console et Bing Webmaster Tools avant d’envoyer le sitemap en ligne. Les jetons de vérification ne sont pas conservés dans ce dépôt. La description About, les sujets et l’image sociale GitHub sont des réglages distincts encore en attente.
