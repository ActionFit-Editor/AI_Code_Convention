# AI Guide - AI Code Convention

This file is the portable authority for generic Unity code-authoring rules distributed by this package. It is intentionally guidance-only: it does not provide Runtime systems, gameplay architecture, code generation, analyzers, formatters, or asset mutation tools.

## Package Identity

- Package ID: `com.actionfit.ai-codeconvention`
- Display name: AI Code Convention
- Repository: `https://github.com/ActionFit-Editor/AI_Code_Convention.git`
- Repository visibility: Private
- Current package version at generation time: `0.1.0`
- Unity version: `6000.2`
- Custom Package Manager dependency: published `1.1.84`

## Purpose And Boundary

Use this package to choose safe, reusable defaults when authoring or changing Unity code, compare those defaults with a consuming project's documented conventions, and apply only the effective local-first rules within an already authorized change.

The package does not require a particular class or folder layout. Names such as `SceneController`, `GameplayRoot`, `GameSession`, and `FeatureRoot` describe conceptual responsibilities only. A consuming project may use different names, split the roles differently, or keep an established architecture.

The package does not prove that existing source code complies with its guidance. `code-convention-check` compares documented contracts and installed package APIs; source-wide linting and automatic remediation are outside its scope.

## Design Input Provenance And Exclusions

- The initial design input was verified by SHA-256 `480f4da5d4b47afaa0614b1b9d734022725f22abd98ff59d4e6afcb5a5099ac2` and rephrased into portable rules. The external file and its machine-specific path are not package content.
- The input carried no public redistribution license notice. This package therefore remains a Private draft pending a separate ownership and distribution-rights review.
- A detailed serialized-reference specialization in the input was intentionally excluded because it did not match the installed owner package's public surface. `AFCC-REF-001` and the installed `com.actionfit.referencebinding` guide are the only effective route; this package does not preserve obsolete API details.

## Project Router Registration

This package should be listed in `Packages/com.actionfit.custompackagemanager/PACKAGE_AI_GUIDE_ROUTER.md`.

Requested router entry:

- `Packages/com.actionfit.ai-codeconvention/AI_GUIDE.md` - AI Code Convention defines portable local-first Unity code-authoring guidance, read-only convention comparison, and authorized application boundaries. Read before comparing or applying shared code conventions.

If the router is not included in the consuming assistant's default reading sequence, connect it through an existing primary project entry point such as `PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. Do not silently create a new project documentation hierarchy.

Read this guide when:

- explaining or applying the portable Unity code-authoring defaults;
- comparing package defaults with a consuming project's local conventions;
- changing files under `Packages/com.actionfit.ai-codeconvention/`;
- changing the three `code-convention-*` skills or their shared reference;
- preparing this package for a later manual release.

## Authority And Precedence

### Stable Rule Identifier Contract

`AFCC-<DOMAIN>-<NUMBER>` identifiers are stable comparison keys. Do not renumber or reuse an identifier for a different meaning. If a rule's meaning must be replaced, add a new identifier and retain the old one as deprecated with a route to its successor. Shared-reference headings and line numbers are explanatory locations, not stable rule IDs.

### `AFCC-PRE-001` — Discover authority before choosing a rule

Apply guidance in this order:

1. System, user, repository, and directory-scoped instructions, including the consuming repository's primary AI entry points.
2. Project-local routers, architecture documents, coding conventions, safety rules, and approved migration procedures.
3. The installed package guide that owns a concrete API or tool contract.
4. This package's generic defaults when no higher authority defines the behavior.

Do not combine conflicting rules into a new compromise. Report the conflict, cite both sources, and choose the higher local or API-owning authority. A local rule may extend a package default without conflict.

### `AFCC-PRE-002` — Treat the installed API owner as factual truth

Project policy may override a generic recommendation, but it cannot make an unavailable API exist. For a named package API, menu, mode, or supported operation, the actually installed owner package guide and public surface are factual authority. Classify a stale or broader claim as `Package/API Mismatch`, select the installed surface, and recommend a separate compatibility decision instead of calling an unsupported operation.

### `AFCC-AUT-001` — Separate tool access from edit authority

Package, Unity, filesystem, and Agent Skill access do not authorize edits. `code-convention-apply` becomes eligible for implicit selection only after the user authorizes a concrete Unity code change and scope. That authorization does not extend to assets, settings, migrations, Jira, Git workflow, publishing, deployment, or unrelated refactors.

### `AFCC-CHG-001` — Preserve state and keep changes surgical

Inspect the current implementation, nearby style, ownership, call sites, serialized data, and existing user changes before editing. Modify only the authorized scope. Do not fold unrelated cleanup, renaming, architecture migration, settings changes, or broad reserialization into the task. Preserve existing values and references unless the user approved the exact data change.

### `AFCC-ADP-001` — Adopt progressively

Apply these rules first to new files, new features, and isolated changes. Do not remodel an established project merely because its structure differs. Introduce EventBus, QueryBus, Command, registries, providers, or finer asmdef boundaries only when the observed ownership and scale require them.

## Decision Contract

### `AFCC-DEC-001` — Prepare a Decision Log for contract changes

Before adding or changing a public API, state store, event, query, command, save key/schema, asset key, asmdef, required serialized reference rule, or resource lifetime, record:

```text
1. Feature owner:
2. File location:
3. State location: configuration / runtime model / save data / server
4. Communication: direct call / C# event or callback / parent binding / EventBus / query / command
5. Affected files:
6. External contract: public API / serialization / save / event / asset ID / none
7. Validation:
8. Failure, rollback, and migration:
```

Keep the log in the final report unless the consuming project requires a specific tracked location. Stop for a material unresolved choice instead of inventing an architecture.

## Portable Code-Authoring Rules

### `AFCC-OWN-001` — Make ownership explicit

Scenes and composition roots assemble; feature owners own rules, runtime models, creation, and disposal. Parents may call children. Children report upward through callbacks or events rather than reaching into parents. Sibling features should not directly depend on each other's implementation. Treat the conceptual root names in this guide as roles, not required public types.

### `AFCC-STA-001` — Put state in the correct authority

Keep configuration, balance data, catalogs, and asset references in configuration assets such as ScriptableObjects. Keep changing session state in runtime models or a session owner. Keep durable values in an explicit save schema. Keep fraud-, payment-, reward-, currency-, and ranking-sensitive authority on a trusted server when the feature is live. Do not use a ScriptableObject as mutable play-session state by default.

### `AFCC-TIM-001` — Use one explicit project-approved time authority

For scheduling, persistence, cooldowns, and date boundaries, use the consuming project's approved clock or time facade and document whether a value is UTC, local, fixed-zone, or server time. Do not mix direct system-clock calls with an offset-aware or testable project clock. The concrete clock type remains a project-local extension.

### `AFCC-COM-001` — Select communication by intent and ownership distance

Use direct calls for parent-to-child control, C# events or callbacks for child-to-parent notification, and an owning parent for sibling binding. Use EventBus for a fact that already happened and must cross ownership boundaries. Use a query or read-only runtime interface for current state. Use an owner API or command for state changes. Do not use buses from leaf views or hot-path objects merely to avoid a clear dependency.

### `AFCC-LIF-001` — Pair registration and disposal at the same lifetime

Unsubscribe, unregister, release, and cancel at the matching lifetime boundary. Make repeated initialization and partial failure policies explicit. Clean up partially created resources in reverse order. Static state and static events need a reset owner that remains correct when domain reload behavior differs.

### `AFCC-ASY-001` — Make asynchronous lifetime and failure observable

Use the consuming project's approved async abstraction. Accept and propagate cancellation when work can outlive its caller. Use a cancellation boundary that matches destroy, disable, close, pool return, scene unload, or application shutdown as appropriate. Await meaningful results and handle exceptions; detached work is allowed only when failure cannot affect the flow and is still observed.

### `AFCC-PER-001` — Treat persistence as a versioned durable contract

Separate runtime models from save DTOs. Preserve stable keys, field names, enum values, time bases, and schema versions. Make migrations idempotent and record completion only after the target data is durable. Define multi-key ordering, partial-failure recovery, source of truth, reset/cache invalidation, and previous-version fixtures.

### `AFCC-ECO-001` — Make live-economy mutations idempotent and trusted

Do not treat client save data as final authority for payments, ads, rewards, currency, ranking, or cheat-sensitive values. Evaluate receipt or server verification, idempotency keys, durable claim receipts or ledgers, replay prevention, server time, failure recovery, rollout, kill switch, and rollback. Persist duplicate-prevention evidence before granting when the feature contract requires it.

### `AFCC-AST-001` — Give dynamic assets a lifetime owner

The creator or feature factory owns release, pool return, and Addressables handles. Keep resource paths and asset identifiers in searchable constants or catalogs. Do not release a handle before every dependent instance is finished, and do not scatter string-based loading across unrelated features.

### `AFCC-SER-001` — Preserve serialization and asset identity

Treat serialized field names, managed-reference type names, enum numeric values, asmdef names, asset GUIDs, Addressables keys, scenes, prefabs, ScriptableObjects, and `.meta` files as compatibility contracts. Follow the consuming project's approved rename or migration procedure. Use targeted Unity or project-approved tools, inspect the diff, and remove unrelated serialization churn. Never infer permission to reset existing values.

### `AFCC-SER-002` — Use a portable serialized-field rename fallback

When no project-specific migration procedure exists and an approved Unity-serialized field rename is unavoidable, preserve compatibility with Unity's standard former-name metadata and validate affected assets. If the consuming project instead requires an Editor migration or a verified targeted YAML-key migration, classify that difference as `Conflict — Local Wins` and follow the local procedure. Never rename a serialized field merely to improve style.

### `AFCC-ASM-001` — Keep Runtime and Editor dependencies one-way

Keep Editor-only APIs and tooling out of Player compilation. Editor assemblies may depend on Runtime assemblies; Runtime assemblies must not depend on Editor assemblies. Introduce asmdefs at meaningful ownership or compilation boundaries, not pre-emptively for every folder. Keep public contract assemblies small and implementation-free.

### `AFCC-REF-001` — Defer serialized-reference APIs to their owner

When `com.actionfit.referencebinding` is installed, read its `AI_GUIDE.md` and use only the public APIs and menus documented by that version. This package does not define attributes, processing modes, bulk wiring, asset-saving APIs, or another ReferenceBinding implementation. If a local document names an API the installed package does not expose, report `Package/API Mismatch` and follow the installed package guide.

## Convention Comparison Contract

`code-convention-check` uses exactly six relationship categories:

- `Aligned`: local and package sources require materially the same behavior.
- `Local Extension`: the local rule adds a compatible project-specific requirement.
- `Conflict — Local Wins`: the sources prescribe incompatible behavior and project policy wins.
- `Package Default`: no local counterpart is documented; use `N/A` for the local source.
- `Local Only`: no package counterpart exists; use `N/A` for the package rule ID.
- `Package/API Mismatch`: a generic, historical design-input, or local claim exceeds the installed owner package's real public surface; the installed owner guide wins.

Every row includes the package rule ID, category, local or owner source path, effective rule, and recommended follow-up. The report cites sources, identifies missing evidence, and never claims that all source code complies. The `AFCC-REF-001` design-input exclusion is reported as an owned-package `Package/API Mismatch` whenever ReferenceBinding is installed, without falsely attributing the excluded design to local project documents.

## Project-Specific Convention Boundary

Keep project-selected async libraries and loop hubs, clock facades, serialized-field containers, UI wrapper types, comment and log language, tween ownership patterns, and serialization migration procedures in the consuming project's own guidance. Compare them as local extensions, local-only rules, or conflicts as appropriate; do not copy them into this portable package or initiate migration.

## Validation And Reporting

### `AFCC-VAL-001` — Validate in proportion to the changed contract

Start with call-site inspection, targeted searches, and diff review. Add compile, EditMode, PlayMode, validation-menu, asset, persistence, or manual QA evidence according to the risk. A successful refresh request is not compilation proof. Separate regressions from known issues and infrastructure failures. Unity-only risks cannot be closed by static inspection alone.

### `AFCC-REP-001` — Report decisions and remaining evidence

Report changed files, ownership/state/communication decisions, validation performed, unverified behavior, remaining risks, and any local-versus-package conflict with the selected authority. Include the Decision Log when `AFCC-DEC-001` applies. Do not claim package publication, deployment, gameplay validation, or a clean worktree without evidence.

## Agent Skills

- `Skills~/manifest.json` registers schema v2 `code-convention-help`, `code-convention-check`, and `code-convention-apply` for Codex and Claude with prefix `code-convention`.
- The help skill is read-only and reads generated `PACKAGE_SKILLS.md` as the authoritative inventory.
- The check skill is read-only. It compares documented rules, uses the six stable relationship categories, and proves repository state did not change.
- The apply skill is write-capable but may be selected only after the user authorizes a concrete Unity code change. It does not create edit authority or own Jira, Git branches, worktrees, pull requests, publishing, or deployment.
- `Skills~/Shared/references/unity-code-authoring-rules.md` contains progressive details for architecture, communication, persistence, lifecycle, assets, assemblies, anti-patterns, and validation.
- Custom Package Manager installs project-local copies and preserves unknown, modified, file-backed, or linked targets. Do not author `PACKAGE_SKILLS.md` in package sources.

## Package Tools Menu

- Unity menu root: `Tools/Package/AI Code Convention/`.
- `README` opens the installed package README.
- The package has no settings asset or executable Unity command.
- Keep it in the README-only priority band.

## Release And Distribution Boundary

- This `0.1.0` draft is Private because its design input does not include a public redistribution license notice.
- A separate ownership and distribution-rights review is required before changing visibility or publishing publicly.
- Publishing is manual through Custom Package Manager. Do not create a repository, push, tag, append a catalog row, deploy, or install into global/home skill directories without separate authorization.
- Before any later release, re-check remote tags and align `package.json`, README, this guide, PackageInfo, and release notes.
