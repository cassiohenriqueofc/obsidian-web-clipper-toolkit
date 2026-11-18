# Release checks — 0.1.0

## Completed locally

- Parsed three JSON templates, checked fields/types, single-prefix layout and prompt counts.
- Validated local documentation links, all-file inventory and common sensitive-data patterns.
- Tested private customization and rejected an invalid parent-directory destination.
- Confirmed a credential-token fixture is rejected; values are suppressed in diagnostics.
- Generated absolute metadata with a demo HTTPS origin, then restored private noindex output.
- Tested the original two-language website in headless Chromium: language switching,
  pause control, reduced motion, no page errors, and 1440/736/375px overflow checks.
- Generated a fresh Proposal-based scaffold without creating a remote or overwriting files.
- Generated an authored animated workflow diagram; the banner is a separate generated asset.

- Checked all seven language pages in headless Chromium, with each file link present,
  seven language options, working language/pause controls, reduced-motion support,
  JSON-LD identity, no JavaScript errors and 21 locale/viewport overflow checks.
- Ran smoke_check.py: seven generated READMEs, no unresolved variables, valid Python,
  null URL omission, overwrite refusal, privacy rejection and portable memory install.
- Package integrity and checksums are verified by package_release.py.

Remote push/release/CI results are checked separately after the initial commit.
Repository settings limitations are documented in repository-protection.md.

## Not performed

Live model calls, installed Obsidian/Web Clipper capture/save checks, complete
Windows/macOS/Linux installation tests, automatic vault copying and public hosting.
No claim of zero secret risk or universal webpage capture is made.
