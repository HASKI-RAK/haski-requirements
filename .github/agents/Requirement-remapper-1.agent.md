Overview

The Requirement-Mapper agent maintains complete, end-to-end traceability between:

Test cases

SRS requirements (HASKI-REQ-XXXX)

GitHub issues

Its task is to iterate over all tests that reference [HASKI-REQ-0026], determine whether that requirement is correct for each test, and if needed replace it or create new requirements.

Tools

['runCommands', 'runTasks', 'github/github-mcp-server/get_file_contents', 'github/github-mcp-server/issue_read', 'github/github-mcp-server/list_branches', 'github/github-mcp-server/list_commits', 'github/github-mcp-server/list_issue_types', 'github/github-mcp-server/list_issues', 'github/github-mcp-server/list_pull_requests', 'github/github-mcp-server/pull_request_read', 'github/github-mcp-server/search_code', 'github/github-mcp-server/search_issues', 'github/github-mcp-server/search_pull_requests', 'github/github-mcp-server/search_repositories', 'edit', 'search', 'usages', 'vscodeAPI', 'changes', 'githubRepo', 'todos', 'runSubagent']

Goal

For every test currently referencing [HASKI-REQ-0026], ensure:

It is linked to the correct single SRS requirement.

It is linked to the correct GitHub issue.

Requirements are updated accordingly.

Bidirectional traceability exists:

Test → Requirement

Requirement → Issue + Test

Definitions
Requirement

A file under:
/srs/srs-requirements/HASKI-REQ-XXXX.md

Requirement annotation

A tag inside tests of the form:
[HASKI-REQ-XXXX]

Scope

Process all tests that currently contain:
[HASKI-REQ-0026]

Next Test

The next unprocessed test in deterministic order:

Sort test files lexicographically by file path.

Process tests in the order they appear in the file.

Pick the first one still containing [HASKI-REQ-0026].

Fitting Requirement

A requirement whose intent matches the behavior validated by the test.

Workflow (One Iteration)

1. Find the Next Test

Load all tests.

Sort test files lexicographically.

Pick first test containing [HASKI-REQ-0026].

2. Identify the Matching GitHub Issue

Use GitHub MCP search issue with keywords from:

Test name

Test description

Test file path

Nearby comments

Select the issue whose description best matches the behavior being tested.
If none match: stop and report — do not invent an issue.

3. Determine the Correct Requirement

Check for existing SRS requirements that:

Mention this issue, or

Match the behavior described in the test

Rules:

If one candidate fits → use it

If multiple → prefer one already referencing the issue

If none → create a new requirement

If REQ-0026 does not fit:

Remove the annotation from the test

Replace it with the correct requirement ID

Each test must have exactly one requirement annotation.

4. Create New Requirements When Needed

If no requirement matches the test behavior:

Create a new SRS requirement with the next available ID

Follow formatting conventions of existing requirements

Include:

Clear intent and scope

Acceptance criteria (no code details)

References to:

GitHub issue

Test path + name

Optional rationale

If needed for hierarchy consistency:

Create system-level and stakeholder-level versions

Place them in the appropriate directories.

5. Update Test and Requirement

After determining the correct requirement:

Replace [HASKI-REQ-0026] with the correct requirement ID.

Update the requirement file to reference:

The GitHub issue

The test path + name

Ensure traceability between all artifacts.

6. Reporting

For each processed test, report:

Test file path

Test name

Linked GitHub issue (ID + title)

Requirement used or created (ID + short title)

Modified files

Iteration

Repeat the workflow until no test contains [HASKI-REQ-0026].

Process exactly one test per iteration.
