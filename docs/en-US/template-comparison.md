# Template comparison

Scores are editorial fit ratings out of 10 for the requested workflow, not measured accuracy, speed, or model quality. All styles retain the full content variable supplied by Clipper.

| Rank | Template | Score | Pros | Cons | Best use |
| --- | --- | --- | --- | --- | --- |
| 1 | 01 Balanced Original Callout | 9.0 | Detailed analysis, research suggestions, project brief, interactive tasks, one collapsed original-content callout | More AI output and context; source syntax edge cases need live review | Default general capture |
| 2 | 02 Compact Original Footer | 8.5 | Fewer prompts, shorter analysis, original content near footer | No project brief/research pack; original-content block has no callout folding | Routine reading |
| 3 | 03 Source Archive | 8.0 | No AI dependency, no model cost, untruncated source, reliable fallback | No generated summary, explanations, or project prompts | Archiving and provider failure |

All three use exactly one structural > prefix per callout/code line. Original source text can itself begin with > inside the fenced archive; those source characters are retained literally, not used to create nested callouts. A code-only block outside a callout (footer style) is also quoted once as requested. Only the original-content callout is collapsed by default to keep long captures manageable; generated sections are expanded.
