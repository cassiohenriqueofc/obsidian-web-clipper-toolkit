# Desenvolvimento

[Guia do projeto](guide.md)

Para projetos, use clone Git local e repositório privado no GitHub. Use branches, commits factuais, revisão de diffs e changelog datado. Não crie repositórios para tarefas cotidianas ou conversas simples.

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
