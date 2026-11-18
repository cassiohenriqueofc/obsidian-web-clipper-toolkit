# Prompt map

All prompts are English, use shared page evidence independently, and run only after the user manually clicks Interpret. Global manual execution is an extension setting; template JSON does not enforce it. Leave automatic execution disabled.

| Prompt | Destination | Balanced | Compact | Archive | Output |
| --- | --- | --- | --- | --- | --- |
| Summary | abstract callout | Yes | Yes | No | Two paragraphs |
| Insights | note callout | Yes | Yes | No | Up to five explained bullets |
| Research | question callout | Yes | No | No | Keywords plus labeled suggested queries/questions |
| Uncertainty | warning callout | Yes | Yes | No | Missing evidence and conflicts |
| Project | example callout | Yes | No | No | Copyable MVP/agent brief |
| Tasks | todo callout, outside fences | Yes | Yes | No | Unchecked Markdown tasks |

## Placement and syntax

Actual natural-language instructions are inside quoted prompt variables in noteContentFormat. The words custom-prompts do not create a registry. Prompt variables are not placed in context. Metadata properties use direct extraction rather than AI. Context contains shared rules and bounded page evidence, including selected schema/meta fields, a JSON-LD excerpt, Markdown, and HTML.

AI-generated body responses have accidental blockquote prefixes removed, dangerous long backtick runs reduced, and one > prefix added to every line. That last step preserves multiline callout containment, including blank lines. Generated task lines are outside fences. The archived source is never passed through those AI cleanup filters.

## Exact instructions

### Summary

Summarize the supplied source in two concise paragraphs. Identify its topic, apparent content type, purpose, and useful contribution. Attribute important claims to the source. If evidence is sparse or only metadata is available, say so; do not infer video contents from a title.

### Insights

Extract up to five source-supported key points. Explain each briefly and include any source-provided steps, definitions, or technical details needed to understand it. Distinguish observations from interpretation. Return Markdown bullets only.

### Research

Return three labeled groups: Keywords extracted from the source, Suggested search queries, and Suggested questions to investigate. Limit each group to five items. Search queries and questions are unverified suggestions, not Google or YouTube rankings, search results, or measured popularity.

### Uncertainty

List missing evidence, contradictions in authors or dates, possible extraction limits, and assumptions that matter. Compare supplied text with metadata when possible. Do not invent conflicts. If none are apparent, state that none were identified within the supplied evidence. Do not claim completeness.

### Project

Propose one practical project grounded in the source. Label it as a proposed idea. Return a copyable brief with these headings: Goal, Source evidence, MVP scope, Requirements, Acceptance criteria, Open questions, and Agent instructions. Tell a later agent to verify assumptions and prepare an OpenSpec-style proposal and task list before implementation. Do not claim to have run OpenSpec, researched competitors, or created project files. Use plain note-name candidates only, never invented wikilinks.

### Tasks

Return up to four concise follow-up actions as unchecked Markdown task lines beginning - [ ]. Label source-prescribed actions and suggested actions distinctly. Do not add introductory text, headings, code fences, or callout syntax. Do not claim any task is complete.

## Evidence budget

AI receives at most 24000 Markdown characters, 8000 HTML characters, and 12000 JSON-LD characters, plus explicit metadata and prompts. These are character limits, not token limits. Independent excerpt limits may cut JSON-LD or code mid-structure. The prompt treats them as evidence excerpts, not validated complete documents. The saved original content is not sliced. If content is selected/highlighted, Clipper may supply that instead of the entire article. Capturing a full page and capturing a selection are different operations.

## Source handling

The original content variable is preserved inside a dynamically sized backtick fence. Only structural quote prefixes are added. The fence is four backticks longer than all backticks present in the original source combined, so source fences cannot terminate it. This trades slightly longer fences for avoiding source changes. Literal source blockquote characters may follow the single structural quote prefix inside the fence.

The Clipper 1.7.1 compiler has a deferred-variable post-processing pass. In AI variants, source text containing literal Clipper expressions may be processed again by the extension. Verify preservation on template/tutorial pages; use Source Archive (no deferred prompts) for those pages if affected. This is an extension-engine limitation, not a reason to silently alter original source text.
