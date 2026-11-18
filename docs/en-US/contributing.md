# Development

[Project guide](guide.md)

Use a local Git clone and a private GitHub repository for projects. Use feature branches, factual commits, reviewed diffs and a dated change log. Do not create repositories for everyday tasks or simple chats.

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
