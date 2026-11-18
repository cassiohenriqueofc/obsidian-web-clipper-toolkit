# Desarrollo

[Guía del proyecto](guide.md)

Para proyectos, usa un clon Git local y un repositorio privado en GitHub. Trabaja con ramas, commits concretos, revisión de cambios y registro fechado. No crees repositorios para tareas cotidianas o conversaciones sencillas.

```bash
git clone https://github.com/cassiohenriqueofc/obsidian-web-cliper.git obsidian-web-clipper-git
cd obsidian-web-clipper-git
git switch -c feat/describe-change
python3 scripts/validate.py
git diff
git add CHANGELOG.md
git diff --cached
git commit -m "docs: describe the verified change"
git push -u origin feat/describe-change
```
