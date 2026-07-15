---
name: code-convention-check
description: Compare AI Code Convention defaults with a consuming Unity repository's documented local conventions and installed package API guides, classify overlap and conflicts, and report the effective local-first rule without changing files. Use for convention overlap, drift, or package/API boundary checks, not source-wide compliance scanning.
---

# Check Code Conventions

Keep the entire check read-only. Do not edit files, install or refresh packages or skills, invoke write-capable Unity commands, change Git refs or index state, generate fixes, publish, or deploy.

1. Resolve the consuming repository root. Capture `git status --short --untracked-files=all` as the baseline and preserve every pre-existing change.
2. Read the repository's active instruction entry points in precedence order, starting with applicable `AGENTS.md`, `CLAUDE.md`, or equivalent files. Follow their links to the primary project router, directory-scoped instructions, architecture documents, coding conventions, safety rules, and approved migration procedures.
3. Resolve the installed AI Code Convention package from `Packages/com.actionfit.ai-codeconvention`; otherwise use `Library/PackageCache/com.actionfit.ai-codeconvention@*` without editing it. Read `AI_GUIDE.md` and `references/unity-code-authoring-rules.md`.
4. Discover additional convention documents with read-only search only when the active router does not enumerate them. Prefer `rg --files` and bounded searches for convention, architecture, async, serialization, lifecycle, time, UI, events, persistence, and package guidance. Do not assume a fixed `Docs/AI` layout.
5. Read an installed owner package's `AI_GUIDE.md` before judging a concrete API. For serialized-reference contracts, inspect `com.actionfit.referencebinding` when installed. Treat the owner guide as the effective API surface.
6. Compare documented rules and owned API contracts, not every source file. Use exactly these relationship categories:
   - `Aligned`: both sources require materially the same behavior.
   - `Local Extension`: the local rule adds a compatible project-specific requirement.
   - `Conflict — Local Wins`: both sources prescribe incompatible behavior and the local authority is selected.
   - `Package Default`: no local rule was found, so the cited `AFCC-*` default applies.
   - `Local Only`: a documented local rule has no corresponding package default; use package rule ID `N/A`.
   - `Package/API Mismatch`: a generic, historical design-input, or local claim names behavior that the installed owner package does not expose; the installed owner guide wins.
7. Always include the `AFCC-REF-001` owned-package boundary when ReferenceBinding is installed. Report the intentionally excluded design-input specialization as `Package/API Mismatch`, cite the installed owner guide path, and state that only its documented public surface is effective. Do not claim that the consuming project's local docs contain the excluded API when they do not.
8. Return a source-backed table with `Package rule ID`, `Category`, `Local or owner source`, `Effective rule`, and `Recommended follow-up`. Use repository-relative paths and line numbers when available. Group missing evidence separately and state that the result is not source-code compliance proof.
9. Capture the same Git status command after the check and compare it with the baseline. If durable repository state changed, identify the paths, treat the no-write contract as failed, and stop.

Recommend follow-up without performing it. A conflict does not authorize migration, code fixes, package refresh, asset writes, or settings changes.
