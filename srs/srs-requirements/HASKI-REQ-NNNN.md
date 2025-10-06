---
id: ${newReqId}
title: [Derive from primary issue title and SyRS, make it requirement-focused]
type: [Infer from SyRS type and issue labels: Functional | Interface | NFR:Performance | NFR:Security | NFR:Usability]
status: [Map primary issue state: open->Approved, closed->Implemented]
source_id: [${input:syrsId}]
links:
  stories: ["GH-${primaryIssue}", "GH-[other related issue numbers]"]
  parents: ["${input:syrsId}"]
---

## Beschreibung

[Synthesize from SyRS requirement, primary issue description, and context from related issues. Use "shall" language. Be specific and measurable.]

## Akzeptanzkriterien

[Insert merged and organized acceptance criteria from all analyzed issues]

## Rationale

Primary implementation: GitHub issue GH-${primaryIssue}: [Issue Title]
Related work: [List other analyzed issues with brief description of how they relate]
Derived from system requirement ${input:syrsId}.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/[repo]/issues/${primaryIssue}
- Related issues: [Links to other analyzed issues]
- [Add technical constraints from issue comments across all issues]
- [Note dependencies between issues]