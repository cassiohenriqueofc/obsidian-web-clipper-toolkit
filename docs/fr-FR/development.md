# Développement

Pour les projets, utilisez un clone Git local et un dépôt GitHub privé. Travaillez avec des branches, des commits factuels, une revue des différences et un journal daté. Ne créez pas de dépôt pour les tâches courantes ou les conversations simples.

```bash
git clone https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit.git obsidian-web-clipper-git
cd obsidian-web-clipper-git
git switch -c feat/describe-change
python3 scripts/validate.py
git diff
git add CHANGELOG.md
git diff --cached
git commit -m "docs: describe the verified change"
git push -u origin feat/describe-change
```

Conservez le clone local complet et le dépôt distant privé. Faites commit et push après vérification ; GitHub ne synchronise pas les fichiers automatiquement. Sauvegardez séparément les paramètres ignorés. Supprimez les ZIP en double et les aperçus jetables, pas les sources ni les scripts.

[Guide du projet](guide.md)
