# Repository protection — observed 2026-11-18

- Repository visibility verified as private; the repository was initially empty.
- GitHub's rulesets endpoint rejected access with: upgrade to GitHub Pro or make this repository public. No visibility change was made. Enforced rulesets are unavailable under the observed plan.
- The integration cannot read repository Actions administration settings (403). This is not proof that workflows cannot run; execution is verified separately after push where possible.
- No server-enforced branch protection is claimed. Private visibility, demo-only files, ignored local configuration, baseline scanning, least-privilege CI and contribution/review policies are included.
- Recommended owner action: upgrade to a plan supporting private-repository rules, then require a passing validate check and pull requests on main; block force-pushes and deletions. Keeping the repository private takes precedence over enabling free public rules.
- Public hosting and repository visibility changes remain disabled/not performed.

Written contribution rules cannot prevent an authorized maintainer from bypassing Git review. A private repo also does not make committed credentials safe.

The integration also rejected enabling the GitHub Template repository setting (403). The reusable project scaffold is included, but the repository is not claimed to have that flag enabled. Owner action: Settings → General → Template repository; preserve private visibility.
