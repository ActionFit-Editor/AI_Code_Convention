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
8. Explain that the `actionfit-unity` architecture target uses `AFCC-TRE-001`, `AFCC-PKG-001`, and `AFCC-PRT-001`: a tree-oriented ownership view backed by an acyclic DAG, coherent project-neutral package nodes, and narrow evidenced ports bound to project adapters at composition roots. State that strict runtime trees, package-count goals, speculative interfaces, DI containers, and whole-project remodeling are excluded.
9. Explain that `code-convention-check` compares documented contracts, reports retirement readiness, and proves no durable change, while `code-convention-apply` is eligible only after the user authorizes a concrete Unity code change. Route source-wide architecture inventory and staged refactoring proposals to the separately installed `$refactor-plan` skill when available; this package does not perform that audit.
10. Route serialized-reference API questions to the installed `com.actionfit.referencebinding/AI_GUIDE.md`. Do not invent attributes, menus, write modes, bulk wiring, or save behavior.
11. When asked about script generation, explain the explicit `Assets > Create > Scripting > ActionFit Convention MonoBehaviour Script` menu, its `Refs`/`Assets`/`Settings` getter-only starter, `RequiredReference` examples, the `Refs`-only `AutoWireChild` example, Editor-guarded owner enqueue, Unity-owned naming and root namespace expansion, and the required `com.actionfit.referencebinding` dependency. State that predefined assemblies can consume the owner automatically while a custom asmdef needs an explicit `com.actionfit.referencebinding` reference; the generator does not mutate asmdefs, existing scripts, Scenes, Prefabs, or saved assets.
12. State that the package contains no Runtime framework, source-compliance scanner, analyzer, formatter, general-purpose code-generation framework, Jira/PR workflow, publication authority, standalone dependency installer, or global skill installer. Custom Package Manager resolves the package's declared dependencies; creating a starter does not change manifests or enforce later compliance.
