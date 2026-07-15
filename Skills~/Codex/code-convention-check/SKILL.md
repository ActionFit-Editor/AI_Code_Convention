---
name: code-convention-check
description: Compare AI Code Convention portable/profile rules with a consuming Unity repository's documented contracts and installed API-owner guides, classify overlap and conflicts, detect skill drift, and report shadow or final local-convention retirement readiness without changing files. Use for convention overlap, package-only migration, drift, or API-boundary checks, not source-wide compliance scanning.
---

# Check Code Conventions

Keep the entire check read-only. Do not edit files, install or refresh packages or skills, invoke write-capable Unity commands, change Git refs or index state, generate fixes, publish, or deploy.

1. Resolve the consuming repository root. Capture `git status --short --untracked-files=all` as the baseline and preserve every pre-existing change.
2. Read the repository's active instruction entry points in precedence order, starting with applicable `AGENTS.md`, `CLAUDE.md`, or equivalent files. Follow their links to the primary project router, directory-scoped instructions, factual architecture, safety rules, any remaining convention documents, and approved migration procedures.
3. Resolve the installed AI Code Convention package from `Packages/com.actionfit.ai-codeconvention`; otherwise use exactly one `Library/PackageCache/com.actionfit.ai-codeconvention@*` without editing it. Read `AI_GUIDE.md` and `references/unity-code-authoring-rules.md`.
4. Resolve the primary router's exact `AI Code Convention profile: <id>` selector. Use `portable-core` when absent. Report duplicate or unknown selectors; never infer a profile. Read `references/profiles/actionfit-unity.md` only when selected, and report each optional rule's capability evidence or inactive state.
5. Read `references/owner-routing.md`, then every installed owner package's `AI_GUIDE.md` needed for a concrete API. For serialized-reference contracts, inspect `com.actionfit.referencebinding` when installed. Treat the owner guide as the effective API surface.
6. Discover additional convention documents with read-only search only when the active router does not enumerate them. Prefer `rg --files` and bounded searches for convention-like normative wording. Do not assume a fixed `Docs/AI` layout, and continue normally when local convention documents are absent. Classify project architecture as factual unless it independently prescribes a general coding rule.
7. Compare documented rules and owned API contracts, not every source file. Use exactly these relationship categories:
   - `Aligned`: both sources require materially the same behavior.
   - `Local Extension`: the local rule adds a compatible project-specific requirement.
   - `Conflict — Local Wins`: both sources prescribe incompatible behavior and the local authority is selected.
   - `Package Default`: no local rule was found, so the cited `AFCC-*` default applies.
   - `Local Only`: a documented local rule has no corresponding package default; use package rule ID `N/A`.
   - `Package/API Mismatch`: a generic, historical design-input, or local claim names behavior that the installed owner package does not expose; the installed owner guide wins.
8. Always include the `AFCC-REF-001` owned-package boundary when ReferenceBinding is installed. Report the intentionally excluded design-input specialization as `Package/API Mismatch`, cite the installed owner guide path, and state that only its documented public surface is effective. Do not claim that the consuming project's local docs contain the excluded API when they do not.
9. Return a source-backed table with `Package rule ID`, `Category`, `Local or owner source`, `Effective rule`, and `Recommended follow-up`. Use repository-relative paths and line numbers when available. Group missing evidence separately and state that the result is not source-code compliance proof.
10. Read `references/local-convention-retirement.md`. In shadow mode map every retirement-candidate rule and report `READY TO RETIRE` or `NOT READY`. In final/package-only mode report `READY` only when local authority, unmigrated rules, unresolved `Local Only`, unresolved `Conflict — Local Wins`, missing owner routes, stale convention links, and package-to-installed-skill drift are all zero. Keep retirement readiness separate from the six categories.
11. Detect drift without refreshing: enumerate registered sources from `Skills~/manifest.json`, compare Codex/Claude sources and managed project-local targets, and allow generated `PACKAGE_SKILLS.md` only in installed help targets. Modified, preserved, linked, file-backed, unmanaged, conflicting, or missing targets block retirement.
12. Capture the same Git status command after the check and compare it byte-for-byte with the baseline. If durable repository state changed, identify the paths, treat the no-write contract as failed, and stop.

Recommend follow-up without performing it. A conflict or readiness result does not authorize migration, deletion, code fixes, package/skill refresh, asset writes, or settings changes.
