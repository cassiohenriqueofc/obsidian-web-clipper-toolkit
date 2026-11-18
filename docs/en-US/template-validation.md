# T2 verification report

Status: local structure and fixture checks passed; live acceptance checks pending.

## Completed

- Three templates parse as JSON and match the required import fields and allowed property types in the 1.7.1 source.
- Unique property names, create behavior, relative folder clippings, and Demo Vault vault fields verified.
- Original 1.7.1 tokenizer, parser, and renderer executed in an isolated harness. Import paths were adjusted and dependencies narrowed; relevant replace/slice filters were taken from that version.
- All template body ASTs rendered without errors. Prompt counts: Balanced 6, Compact 4, Archive 0.
- Original-content fixtures preserved source quotes, blank lines, task syntax, remote-image syntax, literal template examples, and 50 consecutive backticks through the renderer. Source is not sliced.
- Dynamic original-content fence exceeded source fence lengths, preventing collision.
- Templates add one structural quote prefix; no nested structural callout prefixes were authored.
- Successful mock responses demonstrated multiline containment and task checkboxes outside code fences using the actual replace implementation. These were fixtures, not model responses.
- Archive body has no deferred variables, avoiding the compiler's deferred post-processing pass. Its metadata callout deliberately omits schema variables for that reason. Metadata property fields compile separately.
- Context and filenames/properties were inspected statically. No keys or credentials from the supplied settings were copied.

## Limits and pending checks

- Not a complete extension runtime test: date and filename filters used fixture adapters; browser selectors, schema extraction, frontmatter generation, and endpoint/model execution were not exercised.
- No live API calls, extension import on the user's computer, Windows save, secondary copy, or Obsidian rendering test occurred.
- Source with literal Clipper expressions in AI variants may be evaluated again by 1.7.1's deferred post-processing. Prefer Source Archive and do not run Interpreter for those pages. Extension UI prompt collection can also mistake literal source prompt examples for prompts; review before execution.
- Single structural prefixes produce separate foldable callouts, not nested ones. Source's own > characters remain literal inside fenced evidence.
- Full-content retention means no template truncation of the supplied content variable; it cannot recover content that Clipper did not extract or bypass transfer limits.
- Manual execution is global settings behavior and cannot be guaranteed by an imported template alone. Automatic execution must remain disabled.
- The exporter omits vault in 1.7.1; verify the vault dropdown after template import/re-export. The save operation accepts one vault at a time.

## Repeat the current repository checks

Run python3 scripts/build_site.py and python3 scripts/validate.py (Windows: py -3). The earlier isolated 1.7.1 harness ran during template development and is not bundled; its source references are in references/README.md. The current validator checks structure, links, privacy patterns and the file map, not a full extension runtime.

The later validation phase should test actual provider calls, browser selection/highlights, malformed dates, capture transfer limits, existing filenames and Obsidian rendering. The example notes are mock-response fixtures, not real provider outputs.
