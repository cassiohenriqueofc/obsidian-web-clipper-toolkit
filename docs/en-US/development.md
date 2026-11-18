# Git and releases

[Português](../pt-BR/development.md) · [Home](../../README.md)

Use Git 2.23+, GitHub CLI if desired, and Python 3.10+. Authenticate using a
credential manager or gh auth login; do not paste tokens into remote URLs.

## Clone rather than mixing ZIP and history

The release ZIP is a snapshot without .git. For ongoing development, clone into
an empty directory, separate from an extracted snapshot:

```powershell
gh auth login
$gitProject = Join-Path $HOME "Projects\obsidian-web-clipper-git"
git clone https://github.com/cassiohenriqueofc/obsidian-web-cliper.git $gitProject
Set-Location -LiteralPath $gitProject
py -3 scripts/validate.py
```

```bash
gh auth login
git clone https://github.com/cassiohenriqueofc/obsidian-web-cliper.git "$HOME/Projects/obsidian-web-clipper-git"
cd "$HOME/Projects/obsidian-web-clipper-git"
python3 scripts/validate.py
```

## Privacy-conscious commit identity

Copy your exact noreply address from GitHub Settings → Emails and set it locally:

```bash
git config user.name "YOUR_GITHUB_HANDLE"
git config user.email "YOUR_GITHUB_NOREPLY_ADDRESS"
```

Do not commit these placeholders as an identity. Configure actual values locally.

## Change, review, commit

```bash
git switch -c feat/improve-template
python3 scripts/validate.py
git diff
git add templates/01-balanced-original-callout-clipper.json CHANGELOG.md
git diff --cached
git commit -m "feat: clarify source evidence instructions"
git push -u origin feat/improve-template
gh pr create --base main --title "Clarify source evidence" --body-file /path/to/pr-description.md
```

On Windows substitute py -3. Write the PR description to a file before running
the command. Do not force-push main. A written PR policy is not the same as an
enforced branch rule; see project/repository-protection.md for observed status.

## Version and package

Update VERSION, both READMEs, and CHANGELOG.md for each release. Rebuild the site,
validate, and package only the reviewed project files:

```bash
python3 scripts/build_site.py
python3 scripts/validate.py
python3 scripts/package_release.py
```

The package script excludes .git, local-only, private, secret files, unapproved
exports, and dist; it refuses obvious sensitive files and writes ZIP, manifest,
and SHA-256 checksums under ignored dist/. It is not a substitute for reviewing
the release diff. Commit/tag first, then publish the reviewed ZIP:

```bash
git tag -a v0.1.0 -m "Release 0.1.0"
git push origin v0.1.0
gh release create v0.1.0 dist/obsidian-web-clipper-v0.1.0.zip dist/SHA256SUMS.txt dist/release-manifest.json --verify-tag --title "v0.1.0 — General capture toolkit" --notes-file RELEASE_NOTES.md
```

Use a new version for later releases; never overwrite a published tag. Private
release downloads require access to the repository. Do not change visibility or
enable public hosting as part of an ordinary release.
