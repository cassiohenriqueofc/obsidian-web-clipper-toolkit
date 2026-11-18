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

The initial commit was pushed to main in the repository, which was private at the time. The Template
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

## v0.1.1 page and repository update

- Merged pull request #1 into the private repository's `main` branch. The merged
  commit is recorded by GitHub; the local release ZIP will be built from the
  release source commit after this review record is merged.
- Chromium checks passed for 21 locale/viewport combinations (1440, 736 and 375
  pixels), plus language switching, animation pause, reduced motion, and absence
  of JavaScript errors.
- A sample HTTPS metadata build generated canonical, language alternates, Open
  Graph, Twitter, JSON-LD and sitemap for all seven locales. The checked-in build
  was restored to `noindex,nofollow`; no site was deployed.
- The 1774 × 887 social-preview JPEG is 121159 bytes. It is included in the
  repository and is ready for GitHub Settings → Social preview.
- Repository URL is now `https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit`.
  GitHub still reports it private and template-enabled.
- Actions runs for the PR ended in `startup_failure` before creating jobs; no
  remote check result is claimed. Local validation, scaffold smoke checks, and
  Python compilation passed.
- The connected integration could not update the GitHub About description
  (repository-settings API returned 403). The recommended description is saved
  in `project/seo-review.md`. Topics were not added because GitHub makes topic
  names public even for private repositories.


## v0.1.2 animation and README update

- Built `assets/feature-flow.gif` from the existing social-preview image. The five stages show capture, template choice, manual interpretation, source retention, and vault organization. The original static preview is unchanged.
- Added a motion-reduced static image and a pause/resume control to each generated language page; preserved noindex output.
- Refreshed the English README intro and updated localized README/guide version labels.
- `python3 scripts/validate.py`, `python3 scripts/smoke_check.py`, and `git diff --check` passed. `python3 scripts/package_release.py` created and verified the 185-file v0.1.2 archive, manifest, and checksums.
- Settings edit remains blocked (GitHub API HTTP 403; browser control runtime unavailable). At the time of this v0.1.2 check, the repository remained private; the owner has since made it public. The template flag remains enabled.


## Public GitHub Pages deployment

- Owner confirmed the repository is public and authorized site indexing/deployment.
- Added `.github/workflows/deploy-pages.yml`; it enables Pages, builds with the canonical project URL and `--indexable`, validates the output, and deploys the `site/` artifact.
- Checked-in generated pages are built with the canonical URL and indexable robots/sitemap metadata.
- First deployment is blocked: GitHub reports “The job was not started because your account is locked due to a billing issue.” The Pages API also returned 403 to the connected integration. The site is not live until the billing issue is resolved and an Actions run succeeds.
- Repository About description and topics could not be changed through the connected integration (HTTP 403); the browser UI runtime is unavailable.


## v0.1.3 public site configuration

- Added `.github/workflows/deploy-pages.yml` for the approved GitHub Pages URL and indexable build.
- Local build, validation, seven-locale metadata checks, smoke checks, and diff checks passed.
- GitHub Actions run `44402578776` and its retry both failed before steps started. GitHub annotated the job: “The job was not started because your account is locked due to a billing issue.”
- Pages creation via the connected GitHub API returned HTTP 403. The site is not deployed. After billing is resolved and repository settings access is available, rerun the workflow and verify the Pages URL.
- About description, topics, and repository social-preview settings remain unchanged; API/UI access is unavailable.


## v0.1.4 SEO and handoff preparation — 2026-11-19

- Created a 1200 × 630 JPEG social image and added it to the static site output.
- Updated page metadata, language alternates, `x-default`, Open Graph/Twitter image dimensions and alt text, and SoftwareSourceCode JSON-LD.
- Added accessible root language navigation, a custom noindex 404, and a seven-locale sitemap with the Proposal date as `lastmod`.
- Updated publishing instructions in all seven locales and recorded personal-site metadata separation in the SEO review.
- `python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable`, `python3 scripts/validate.py`, `python3 scripts/smoke_check.py`, sitemap/metadata assertions, and `git diff --check` passed locally. The release packager created and verified a 191-file `obsidian-web-clipper-v0.1.4.zip` with manifest and checksums.
- No GitHub Pages deploy, Search Console verification, sitemap submission, or GitHub Settings update was possible in this session. Actions remains blocked by billing; About/topics/social-preview settings remain pending.


## Post-merge deployment state — 2026-11-18

- PR #6 merged to `main` as `57c92624889c5f27b29ae3538dc4a2328ce95879`.
- The post-merge validate and Pages build runs failed before starting steps; GitHub reports the account billing lock. The deploy job was skipped.
- GitHub Pages API site creation returned HTTP 403 (`Resource not accessible by integration`). The Pages URL returned HTTP 404 after merge. No deployment or indexing is claimed.
- The sanitized 0.1.4 ZIP, manifest, and checksums were uploaded on `artifacts/v0.1.4`; the manifest records source commit `87149ae`.
