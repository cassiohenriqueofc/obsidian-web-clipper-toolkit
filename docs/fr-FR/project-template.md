# Modèle de projet réutilisable

[Guide du projet](guide.md)

Modifiez les métadonnées simples de project-template/Proposal.md puis générez un nouveau dossier vide avec new_project.py. Le générateur ne crée pas de dépôt distant, ne pousse rien, ne publie pas et n’implémente pas l’application. Vérifiez noms, courriel, URL et licence avant diffusion.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

Chaque nouveau fichier doit préciser son rôle réel, sa classification des données, ses sources pertinentes et ses vérifications utiles. Les notes utilisent un YAML simple ; le code un en-tête bref et utile. Les commentaires expliquent raisons et contraintes sans répéter le code. N’inventez ni tests ni résultats.

Le générateur copie seulement les champs publics, pas le corps brut de la proposition. Ajoutez le périmètre vérifié au Proposal.md généré. L’attribution doit respecter la politique approuvée ; les langues suivent les fichiers livrés.
