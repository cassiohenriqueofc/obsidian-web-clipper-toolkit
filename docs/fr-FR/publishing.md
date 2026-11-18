# Publication et métadonnées

Prévisualisez localement. La publication et les changements de visibilité demandent une approbation distincte. Le site utilise noindex par défaut. Indiquez l’URL HTTPS réelle et approuvée pour générer canonical, Open Graph, hreflang et sitemap. Les fichiers llms ne garantissent aucun classement.

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Utilisez des données de démonstration. Excluez paramètres locaux, identifiants, notes privées et chemins personnels. Un dépôt privé ne protège pas un secret déjà enregistré dans l’historique. Le titulaire a autorisé uniquement l’attribution indiquée ci-dessous.

[Guide du projet](guide.md)

Le README est du Markdown rendu ; les métadonnées Open Graph, Twitter, canonical
et JSON-LD appartiennent au site généré. L’image de prévisualisation compacte se
trouve dans [assets/social-preview.jpg](../../assets/social-preview.jpg). Vous
pouvez la téléverser dans GitHub Settings → Social preview. Les noms des topics
GitHub sont publics même si le dépôt est privé ; attendez l’autorisation avant
de les ajouter. Google précise que llms.txt ne modifie ni la visibilité ni le
classement dans Google Search et qu’aucun balisage spécial n’est requis pour la
recherche avec IA.
