---
name: code-convention-help
description: Explain AI Code Convention, its portable local-first Unity rules, stable rule identifiers, installed related skills, Decision Log, progressive reference, ReferenceBinding route, and safety boundaries. Use when a user asks how the package works or which convention skill applies.
---

# AI Code Convention Help

Keep this workflow read-only. Do not edit code or assets, invoke Unity, refresh packages or skills, change Git state, publish, or deploy.

1. Read `PACKAGE_SKILLS.md` first. Treat its generated package identity, complete related-skill inventory, invocations, descriptions, agents, and access values as authoritative.
2. Resolve the physical package from `Packages/com.actionfit.ai-codeconvention`; otherwise use `Library/PackageCache/com.actionfit.ai-codeconvention@*` without editing PackageCache.
3. Read the installed `README.md` and `AI_GUIDE.md`. Use their current package version, precedence, `AFCC-*` identifiers, Decision Log triggers, conceptual-role boundary, and release restrictions.
4. Read `references/unity-code-authoring-rules.md` only when the user needs detailed architecture, EventBus/query/command selection, persistence, lifecycle, assets, assemblies, anti-patterns, or the validation matrix.
5. Explain that project-local instructions and the installed owner package for a concrete API override generic defaults. A conflict is reported and resolved local-first; it is not blended into a new rule.
6. Explain that `code-convention-check` compares documented contracts without changing files, while `code-convention-apply` is eligible only after the user authorizes a concrete Unity code change.
7. Route serialized-reference API questions to the installed `com.actionfit.referencebinding/AI_GUIDE.md`. Do not invent attributes, menus, write modes, bulk wiring, or save behavior.
8. State that the package contains no Runtime framework, compliance scanner, analyzer, formatter, code generator, Jira/PR workflow, publication authority, or global skill installer.
