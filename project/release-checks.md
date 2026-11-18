# Release checks — 0.1.1

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

## Remote state

The initial commit was pushed to main in the private repository. The Template
repository flag is verified true. The validate workflow is active, but its first
run returned startup_failure before jobs were created. No passing remote CI
result is claimed. Repository rulesets need a supporting private-repository plan.
Release assets are verified by the release operation; public hosting is not enabled.

## Independent review

No unrequested scope drift was found. A potential exposure path in future
scaffolds was corrected before packaging: raw Proposal body text is omitted,
public attribution is allowlisted, and JSON-LD languages follow delivered files.
Tests cover those changes. This was a preventative fix, not a finding that real
private data had leaked into the repository.

## Not performed

Live model calls, installed Obsidian/Web Clipper capture/save checks, complete
Windows/macOS/Linux installation tests, automatic vault copying and public hosting.
No claim of zero secret risk or universal webpage capture is made.
