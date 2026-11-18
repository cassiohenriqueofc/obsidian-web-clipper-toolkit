---
project_name: "Example Project"
project_slug: "example-project"
summary: "Replace with a factual one-sentence description of the project."
version: "0.1.0"
date: "2026-11-18"
default_language: "en-US"
author_name: "Cassio Henrique"
company_name: "Múltipla Tecnologia"
contact_email: "cassiohenriqueofc@gmail.com"
repository_url: null
landing_page_url: null
content_type: "SoftwareSourceCode"
license_id: "LicenseRef-Noncommercial-Source-Available-1.0"
data_classification: "demo-only"
---

# Proposal

## Problem and intended result

Describe the actual problem, users, and observable result. Do not invent demand,
benchmarks, integrations, customers, or prior work.

## Scope

- In scope:
- Out of scope:
- Dependencies and their verified sources:

## Acceptance criteria

- [ ] State a concrete check for each required behavior.
- [ ] Define the data allowed in version control.
- [ ] Identify live checks that need access, credentials, cost, or approval.

## Evidence and attribution

Record source URL, license, upstream revision, modified files, and required notices
for any reused or forked work. If unknown, leave it unresolved instead of choosing
a convenient license. Include no copied code until its permissions are established.

## Decisions and approval

Record decisions, dates, implementation authorization and release visibility.
Null URLs remain unset; never invent a public site or canonical address.

## Variable contract

Frontmatter uses one flat key per line. Values must be JSON-compatible scalars:
quoted strings, numbers, true/false or null. This is a deliberately small valid
YAML subset parsed without extra packages. Other YAML features are rejected.
Edit these public/demo-safe values, then run scripts/new_project.py.

The generator reads only the public flat fields above. It intentionally omits the raw body from the new project to avoid copying private drafting notes. Add reviewed scope and acceptance criteria to the generated Proposal.md before implementation. Public attribution must match the explicit .privacy-policy.json allowlist.
