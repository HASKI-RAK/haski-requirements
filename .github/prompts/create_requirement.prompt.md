---
mode: 'agent'
tools: ['todos', 'usages', 'vscodeAPI', 'problems', 'githubRepo', 'runCommands', 'runTasks', 'github/get_issue', 'github/get_issue_comments', 'github/list_issues', 'github/search_issues', 'github/update_issue', 'edit/createFile', 'edit/editFiles', 'search']
description: 'Link a SyRS requirement with GitHub issues and create a resulting SRS requirement with full traceability.'
---

# Create SRS Requirement from SyRS Requirement

You are an AI agent that creates Software Requirements Specification (SRS) requirements based on System Requirements Specification (SyRS) requirements and their implementing GitHub issues. Therefore reverse engineer the requirement from the implemented issue and SyRS requirement.

## Input Required

SyRS Requirement ID: `${input:syrsId:Enter the SyRS requirement ID (e.g., HASKI-SYRS-0001)}`

## Steps to Execute

### 1. Locate and Read the SyRS Requirement

- Search for the file `strs/syrs-requirements/`${input:syrsId}`.md`
- Read the file to extract:
  - Title
  - Description
  - Type
  - Priority
  - Key functionality/capabilities described
  - Any existing links to GitHub issues or stories
- Store this information for later use
- If the SyRS doesn't provide all information you need, search for the related informal stakeholder need in `strs/stakeholder-requirements`

### 2. Search for Related GitHub Issues

Since issues may not yet reference the SyRS ID, perform intelligent searches across multiple dimensions:

#### 2a. Direct Reference Search
- Use `github/search_issues`: `repo:HASKI-RAK/HASKI-Frontend,HASKI-RAK/HASKI-Backend "${input:syrsId}" is:issue`
- Store any found issues as candidates

#### 2b. Keyword-Based Searches
Extract 3-5 key terms from the SyRS title and description, then search:
- Use `github/search_issues` with query: `repo:HASKI-RAK/HASKI-Frontend,HASKI-RAK/HASKI-Backend [key term 1] [key term 2] is:issue`
- Example: If SyRS is about "Lernpfad-Anpassung basierend auf Lernstil", search for:
  - `repo:HASKI-RAK/HASKI-Frontend,HASKI-RAK/HASKI-Backend Lernpfad Anpassung is:issue`
  - `repo:HASKI-RAK/HASKI-Frontend,HASKI-RAK/HASKI-Backend Lernstil adaptive is:issue`
  - `repo:HASKI-RAK/HASKI-Frontend,HASKI-RAK/HASKI-Backend learning path personalization is:issue`
- Store all relevant results (do not deduplicate yet)

#### 2c. Feature/Component-Based Search
Based on SyRS type and domain, search for related components:
- If UI-related: search in HASKI-Frontend with UI component terms
- If backend/algorithm: search in HASKI-Backend with algorithm/service terms
- Use labels if SyRS mentions specific areas (e.g., "feature:learning-path", "component:ILS")
- Store all results

#### 2d. Collect and Analyze All Matching Issues
- Compile all issues from searches 2a-2c
- For each unique issue number, retrieve full details using `github/get_issue` and `github/get_issue_comments`
- Analyze and categorize by relevance:
  1. **High Confidence**: Direct SyRS reference OR multiple keyword matches
  2. **Medium Confidence**: Single keyword match + relevant labels/component
  3. **Low Confidence**: Tangentially related (may provide context)
- **Important**: Keep all issues for information extraction, even if some seem less relevant

### 3. Present All Related Issues and Select Primary Implementation

- Display comprehensive list to user, grouped by confidence:
  ```
  Found N issues related to ${input:syrsId}:
  
  [High Confidence - Direct Implementation]
  1. GH-123 (Frontend): "Implement adaptive learning path" [closed] ⭐
     Matches: ${input:syrsId}, Lernpfad, Anpassung, adaptive
     Key info: Uses ILS algorithm, frontend component
  
  2. GH-124 (Backend): "API for learning style detection" [closed]
     Matches: Lernstil, adaptive, personalization
     Key info: REST endpoint, ILS service integration
  
  [Medium Confidence - Related Work]
  3. GH-456 (Backend): "Add ILS-based recommendation" [open]
     Matches: Lernstil, personalization
     Key info: Extends GH-124, adds caching
  
  [Low Confidence - Contextual]
  4. GH-789 (Frontend): "Refactor course navigation" [closed]
     Matches: Lernpfad
     Key info: UI refactoring, may affect learning path display
  
  All issues will be analyzed to extract comprehensive requirements information.
  ```

- If no issues found: 
  - "No GitHub issues found for `${input:syrsId}`. This SyRS requirement may not be implemented yet. Options:
    1. Provide issue number manually
    2. Search different keywords (I'll ask for suggestions)
    3. Skip issue linking and create SRS requirement anyway"

- If issues found, determine the primary issue.
- Store the selected issue number as `${primaryIssue}`
- **Important**: All other related issues will still be analyzed for acceptance criteria, technical constraints, and implementation details

### 4. Retrieve and Synthesize Information from All Issues

#### 4a. Primary Issue Details
- Use `github/get_issue` to retrieve full details of `${primaryIssue}`:
  - Title
  - Body/Description
  - Labels
  - Acceptance criteria
  - State (open/closed)
  - Repository (Frontend/Backend)

#### 4b. Extract Information from Related Issues
For each additional related issue from step 3:
- Use `github/get_issue` to retrieve full details
- Use `github/get_issue_comments` for implementation discussions
- Extract:
  - Additional acceptance criteria not in primary issue
  - Technical constraints or dependencies mentioned
  - Implementation approaches or architectural decisions
  - Test scenarios or edge cases discussed
  - Related PRs that provide implementation context

#### 4c. Synthesize Comprehensive Requirement Data
- Combine acceptance criteria from all relevant issues
- Identify technical constraints mentioned across issues
- Note dependencies between issues (e.g., "extends GH-124")
- Collect all related PRs for verification_method context

### 5. Determine Next SRS Requirement ID

- Use `search` tool to find all files matching pattern `srs/srs-requirements/HASKI-REQ-*.md`
- Extract the highest existing requirement number (e.g., from HASKI-REQ-0042 extract 42)
- Increment by 1 and format as `HASKI-REQ-XXXX` (zero-padded to 4 digits)
- Store as `${newReqId}`

### 6. Extract Acceptance Criteria from All Issues

- Parse the PRIMARY issue body for sections containing:
  - "Acceptance Criteria"
  - "AC:"
  - "Definition of Done"
  - "DoD:"
  - Checklist items (lines starting with `- [ ]` or `- [x]`)
  
- **Additionally**, extract acceptance criteria from all RELATED issues found in step 3
- Merge and organize criteria by:
  1. Functional requirements (what the system shall do)
  2. Quality requirements (performance, usability, security)
  3. Verification criteria (how to test)
  
- Deduplicate similar criteria but preserve nuanced differences
- If no criteria found anywhere, create placeholder: "- [ ] Verify implementation matches issue GH-${primaryIssue} requirements"

### 7. Create SRS Requirement File

- Use `edit/createFile` to create `srs/srs-requirements/${newReqId}.md`
- Use the following template structure:

```yaml
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
```

### 8. Update GitHub Issues and SyRS with Cross-Links

#### 8a. Update Primary GitHub Issue
- Use `github/update_issue` to update issue #${primaryIssue}
- Prepend to issue body:
  ```
  **Requirements:** `req:${newReqId}` (SRS) | `${input:syrsId}` (SyRS)
  
  ---
  
  [existing body content]
  ```
  
#### 8b. Update Related GitHub Issues (Optional)
- For high-confidence related issues, add a reference:
  ```
  **Related Requirement:** `req:${newReqId}` (see primary implementation in GH-${primaryIssue})
  ```
  
#### 8c. Update SyRS Requirement
- Use `edit/editFiles` to update `strs/syrs-requirements/${input:syrsId}.md`
- Add to front matter links section:
  ```yaml
  links:
    stories: ["GH-${primaryIssue}", "GH-[related issues]"]
    children: ["${newReqId}"]
  ```
- If update fails, provide manual instruction to user

### 9. Verify and Report

- Use `search` to verify the new file was created at `srs/srs-requirements/${newReqId}.md`
- Print summary:
  ```
  ✓ Created SRS requirement: ${newReqId}
  ✓ Linked to SyRS: ${input:syrsId}
  ✓ Linked to GitHub issue: GH-${primaryIssue}
  ✓ Updated issue with requirement references
  ✓ Applied label 'linked-requirement' to issue(s)
  ✓ Updated SyRS with traceability links
  
  Next steps:
  - Review generated requirement at srs/srs-requirements/${newReqId}.md
  - Run: python scripts/generate_docs.py
  ```

### 10. Optional: Regenerate Documentation

- Ask user: "Would you like to regenerate the documentation site now? (y/n)"
- If yes, use `runCommands` to execute: `python scripts/generate_docs.py --verbose`

## Error Handling

- If SyRS requirement not found: Report error and list available SyRS requirements
- If no GitHub issues found: Offer to create requirement anyway with manual issue linking
- If file creation fails: Provide the generated content to user for manual creation
- If issue update fails: Provide manual instructions with the exact text to add
- If label application fails: Note in summary but continue (label may not exist in repository)

## Validation Rules

- Ensure `${newReqId}` follows pattern HASKI-REQ-XXXX
- Verify YAML front matter is valid
- Ensure at least one acceptance criterion exists
- Verify parent link to `${input:syrsId}` is present
- Confirm GitHub issue link uses correct repository

## Search Strategy Tips

When extracting keywords for issue search:
- Prioritize domain-specific terms (e.g., "Lernstil", "ILS", "adaptive")
- Include both German and English variants
- Use technical component names mentioned in SyRS
- Consider user-facing feature names vs. technical implementation terms
- For NFRs, include quality attributes (e.g., "performance", "Sicherheit", "usability")