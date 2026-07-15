---
name: code-convention-help
description: Explain AI Code Convention, its portable core, explicit profiles, stable rule identifiers, API-owner routing, local-convention retirement checks, installed related skills, Decision Log, and safety boundaries. Use when a user asks how the package works, which profile is active, or which convention skill applies.
---

# AI Code Convention Help

Keep this workflow read-only. Do not edit code or assets, invoke Unity, refresh packages or skills, change Git state, publish, or deploy.

1. Read `PACKAGE_SKILLS.md` first. Treat its generated package identity, complete related-skill inventory, invocations, descriptions, agents, and access values as authoritative.
2. Resolve the physical package from `Packages/com.actionfit.ai-codeconvention`; otherwise use `Library/PackageCache/com.actionfit.ai-codeconvention@*` without editing PackageCache.
3. Read the installed `README.md` and `AI_GUIDE.md`. Use their current package version, precedence, stable `AFCC-*` meanings, Decision Log triggers, conceptual-role boundary, and release restrictions.
4. Read the consuming repository's primary router without changing it. Resolve the exact `AI Code Convention profile: <id>` selector through `AFCC-PRO-001`; use `portable-core` when absent, and report duplicate or unknown selectors instead of guessing.
5. Read `references/unity-code-authoring-rules.md` for portable detail. Read `references/profiles/actionfit-unity.md` only when that profile is selected. Report activated and inactive capability-gated IDs.
6. Read `references/owner-routing.md` and the installed owner guide before explaining a concrete API. Project architecture may supply concrete factual mappings but is not a second code-convention body.
7. Read `references/local-convention-retirement.md` when the user asks about overlap, drift, package-only operation, or removing local convention authority. Explain that its shadow and final checks are read-only and do not authorize deletion.
8. Explain that `code-convention-check` compares documented contracts, reports retirement readiness, and proves no durable change, while `code-convention-apply` is eligible only after the user authorizes a concrete Unity code change.
9. Route serialized-reference API questions to the installed `com.actionfit.referencebinding/AI_GUIDE.md`. Do not invent attributes, menus, write modes, bulk wiring, or save behavior.
10. State that the package contains no Runtime framework, source-compliance scanner, analyzer, formatter, code generator, Jira/PR workflow, publication authority, dependency installer, or global skill installer.
