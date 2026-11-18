# Install and use

[English](install.md) · [Português](../pt-BR/install.md) · [Home](../../README.md)

## Requirements

Install the official [Obsidian desktop app](https://obsidian.md/download) and
[Web Clipper](https://obsidian.md/clipper) in a supported browser. Check the
extension's current browser list; do not assume every Apple browser or every
Linux package supports the extension. Safari is macOS-specific. A paid provider
is not required for Archive. AI styles require an accessible configured model.
Python 3.10+ is needed only for project utilities, not for importing JSON.

## Windows

Download the versioned release ZIP from the private repository while signed in.
Keep its companion SHA256SUMS.txt and verify before extraction:

```powershell
$archive = Join-Path $HOME "Downloads\obsidian-web-clipper-v0.1.1.zip"
Get-FileHash -Algorithm SHA256 -LiteralPath $archive
# Compare the result with SHA256SUMS.txt from the same release.
$projectDir = Join-Path $env:LOCALAPPDATA "Programs\Demo Notes\obsidian-web-clipper"
New-Item -ItemType Directory -Force -Path $projectDir | Out-Null
Expand-Archive -LiteralPath $archive -DestinationPath $projectDir
Set-Location -LiteralPath $projectDir
py -3 scripts/validate.py
```

Use an empty destination or back it up first. Expand-Archive intentionally omits
-Force so an existing project is not silently overwritten. Substitute your own
project directory for the demo value; a project folder is not automatically an Obsidian vault.

```powershell
py -3 scripts/configure_templates.py --vault "Demo Vault" --folder "clippings"
# Import a generated JSON from local-only/templates in the extension.
```

## macOS

Install the Obsidian .dmg from the official download page and the appropriate
browser extension from the official Clipper page. Use a new extraction folder:

```bash
mkdir -p "$HOME/Projects/obsidian-web-clipper"
cd "$HOME/Projects/obsidian-web-clipper"
shasum -a 256 "$HOME/Downloads/obsidian-web-clipper-v0.1.1.zip"
# Compare with the release checksum before extracting.
unzip -n "$HOME/Downloads/obsidian-web-clipper-v0.1.1.zip"
python3 scripts/validate.py
python3 scripts/configure_templates.py --vault 'Demo Vault' --folder 'clippings'
```

## Linux

Choose the appropriate desktop package from Obsidian's official download page.
Install Web Clipper in a supported browser. With Python 3.10+ and unzip available:

```bash
mkdir -p "$HOME/Projects/obsidian-web-clipper"
cd "$HOME/Projects/obsidian-web-clipper"
sha256sum "$HOME/Downloads/obsidian-web-clipper-v0.1.1.zip"
# Compare with the release checksum before extracting.
unzip -n "$HOME/Downloads/obsidian-web-clipper-v0.1.1.zip"
python3 scripts/validate.py
python3 scripts/configure_templates.py --vault 'Demo Vault' --folder 'clippings'
```

Folder capitalization matters on case-sensitive filesystems. These Linux/macOS
commands are documented workflows, not a claim of an end-to-end install test.

## Configure Web Clipper

1. Open the vault in Obsidian. Create `clippings` inside its root.
2. Import a JSON with the template importer; do not use the full-settings importer.
3. Verify the vault dropdown and folder. Clipper 1.7.1's exporter may omit the vault field.
4. Enable Interpreter for AI styles and add the provider/model you can access.
   Keep auto-run off. Do not assume a display label is a valid API model ID.
5. Visit a page, select the style, click Interpret manually, review all outputs,
   then choose Add to Obsidian. Archive has no authored AI prompts.
6. Inspect YAML, the complete original-content block, and interactive tasks.

If no model is available, use Archive. Do not save unresolved prompt expressions
after a model failure. Never put API keys in shell commands, example JSON, issues,
screenshots, or repository files. [Official template guide](https://obsidian.md/help/web-clipper/templates).

## Optional second-vault copy

Clipper's save operation targets one vault. This release does not install a
watcher or auto-copy service. To keep the identical interpreted note, copy the
saved Markdown file instead of generating it again. Windows example:

```powershell
$sourceFile = Read-Host "Full path to the saved Markdown file"
$destinationDir = Read-Host "Existing folder in your second vault"
if (!(Test-Path -LiteralPath $sourceFile -PathType Leaf)) { throw "Source file missing" }
if (!(Test-Path -LiteralPath $destinationDir -PathType Container)) { throw "Destination missing" }
$targetFile = Join-Path $destinationDir (Split-Path $sourceFile -Leaf)
if (Test-Path -LiteralPath $targetFile) { throw "Target already exists; review before replacing" }
Copy-Item -LiteralPath $sourceFile -Destination $targetFile
```

macOS/Linux, after setting paths for your own vaults:

```bash
source_file='/path/to/first-vault/clippings/example.md'
destination_dir='/path/to/second-vault/Clippings'
test -f "$source_file" && test -d "$destination_dir" || exit 1
target_file="$destination_dir/$(basename "$source_file")"
test ! -e "$target_file" || { printf '%s\n' 'Target exists; review first'; exit 1; }
cp -n -- "$source_file" "$target_file"
```

## Updates and rollback

Export your current templates privately before importing a replacement. Import
the new version as a separate template, test a small page, then remove the old
one only after review. Keep release ZIPs outside the Git working tree. ZIPs are
snapshots without .git history; clone for ongoing version-controlled work.
