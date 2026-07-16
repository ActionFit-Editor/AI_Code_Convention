# AI Guide - AI Code Convention

This file is the portable authority for generic Unity code-authoring rules distributed by this package. The package also provides one narrow Editor-only MonoBehaviour starter generator. It does not provide Runtime systems, gameplay architecture, analyzers, formatters, a general-purpose code-generation framework, or migration tools.

## Package Identity

- Package ID: `com.actionfit.ai-codeconvention`
- Display name: AI Code Convention
- Repository: `https://github.com/ActionFitGames/AI_Code_Convention.git`
- Repository visibility: Private
- Current package version at generation time: `0.4.0`
- Unity version: `6000.2`
- Custom Package Manager dependency: published `1.1.91`
- ReferenceBinding dependency: published `0.1.1`

## Purpose And Boundary

Use this package to choose safe, reusable defaults when authoring or changing Unity code, opt in to an organization profile through explicit routing metadata, resolve concrete APIs through their installed owners, compare documented contracts, apply only the effective rules within an already authorized change, and explicitly create a new ActionFit convention starter script when that shape is desired.

The package does not require a particular class or folder layout. Names such as `SceneController`, `GameplayRoot`, `GameSession`, and `FeatureRoot` describe conceptual responsibilities only. A consuming project may use different names, split the roles differently, or keep an established architecture.

The package does not prove that existing source code complies with its guidance. `code-convention-check` compares documented contracts and installed package APIs; source-wide linting and automatic remediation are outside its scope.

## Editor Script Template Contract

- `Assets > Create > Scripting > ActionFit Convention MonoBehaviour Script` invokes Unity's native `ProjectWindowUtil.CreateScriptAssetFromTemplateFile` flow with a package-owned immutable template path and default file name `NewActionFitMonoBehaviour.cs`.
- The template uses Unity's `#SCRIPTNAME#`, `#ROOTNAMESPACEBEGIN#`, and `#ROOTNAMESPACEEND#` tokens. Unity owns destination selection, rename interaction, class-name replacement, root-namespace expansion, and existing-file handling.
- The generated starter contains example `Refs`, `Assets`, and `Settings` containers under `AFCC-RFS-002`, private `[SerializeField]` backing fields and getter-only access under `AFCC-SER-004`, and no empty lifecycle methods.
- `Refs.contentRoot` uses `RequiredReference("CONTENT_ROOT_MISSING")` and `AutoWireChild("ContentRoot")`. The exact GameObject name is the AutoWire search key, while the Required string is a diagnostic identifier. `Assets.iconSprite` uses `RequiredReference("ICON_SPRITE_MISSING")` without `AutoWireChild`; `Settings` has no reference attributes.
- The searchable `OnValidate` declaration keeps `ReferenceBindingRequests.Enqueue(this)` inside `#if UNITY_EDITOR`. It enqueues the owning `MonoBehaviour`, never a nested container, and does not reference `ReferenceBinding.Editor` from generated runtime code.
- `com.actionfit.referencebinding@0.1.1` is a required package dependency and owns attribute, processing, validation, Play Mode, Dirty-state, and save behavior. The generator never saves a Scene or Prefab. It also never replaces a valid manual reference or defines a second reference-processing API.
- The generated output compiles in Unity predefined assemblies through ReferenceBinding's auto-referenced Runtime assembly. A consuming custom asmdef must explicitly reference `com.actionfit.referencebinding`; package installation alone does not add that assembly reference, and this generator does not mutate consuming asmdefs.
- Invoking this menu is an explicit request for the `actionfit-unity` starter shape. It does not read or write the repository's profile selector, infer a profile, create or change an asmdef, overwrite or migrate existing scripts, or enforce runtime immutability mechanically.
- The generated file is user-owned after creation. Replace the example fields with feature-specific inputs while preserving the selected effective rules. Package updates never rewrite generated scripts, and the starter alone is not source-compliance proof.

## Design Input Provenance And Exclusions

- The initial design input was verified by SHA-256 `480f4da5d4b47afaa0614b1b9d734022725f22abd98ff59d4e6afcb5a5099ac2` and rephrased into portable rules. The external file and its machine-specific path are not package content.
- The input carried no public redistribution license notice. This package therefore remains a Private draft pending a separate ownership and distribution-rights review.
- A detailed serialized-reference specialization in the input was intentionally excluded because it did not match the installed owner package's public surface. `AFCC-REF-001` and the installed `com.actionfit.referencebinding` guide are the only effective route; this package does not preserve obsolete API details.

## Project Router Registration

This package should be listed in `Packages/com.actionfit.custompackagemanager/PACKAGE_AI_GUIDE_ROUTER.md`.

Requested router entry:

- `Packages/com.actionfit.ai-codeconvention/AI_GUIDE.md` - AI Code Convention defines portable Unity code-authoring rules, explicit profiles, API-owner routing, read-only retirement checks, and authorized application boundaries. Read before comparing or applying shared code conventions.

If the router is not included in the consuming assistant's default reading sequence, connect it through an existing primary project entry point such as `PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. Do not silently create a new project documentation hierarchy.

Read this guide when:

- explaining or applying the portable Unity code-authoring defaults;
- comparing package defaults with a consuming project's local conventions;
- changing files under `Packages/com.actionfit.ai-codeconvention/`;
- changing or diagnosing the convention script template or its Unity creation menu;
- changing the three `code-convention-*` skills or their shared reference;
- preparing this package for a later manual release.

## Authority And Precedence

### Stable Rule Identifier Contract

`AFCC-<DOMAIN>-<NUMBER>` identifiers are stable comparison keys. Do not renumber or reuse an identifier for a different meaning. If a rule's meaning must be replaced, add a new identifier and retain the old one as deprecated with a route to its successor. Shared-reference headings and line numbers are explanatory locations, not stable rule IDs.

### `AFCC-PRO-001` — Select profiles explicitly

`portable-core` is the default. Select another profile only through one exact line in the consuming repository's primary router:

```text
AI Code Convention profile: actionfit-unity
```

Do not infer a profile from a repository name, organization, folder layout, installed package, or existing source style. Report duplicate, unknown, or conflicting selectors instead of guessing. The selector is routing metadata, not a local convention body.

### `AFCC-PRO-002` — Gate optional rules by evidenced capability

A selected profile may contain dependency-specific rules. Activate one only when the relevant installed package, assembly, source, or public API is evidenced in the consuming repository. A convention check or application must never install a dependency, add a scripting symbol, or invent an API merely to activate a rule.

### `AFCC-PRE-001` — Discover authority before choosing a rule

Apply guidance in this order:

1. System, user, repository, and directory-scoped instructions, including the consuming repository's primary AI entry points.
2. Project-local safety and workflow rules, factual architecture, explicit profile selection, any still-approved local convention during migration, and approved migration procedures.
3. The installed package guide that owns a concrete API or tool contract.
4. The explicitly selected package profile.
5. This package's portable-core defaults when no higher authority defines the behavior.

Do not combine conflicting rules into a new compromise. Report the conflict, cite both sources, and choose the higher local or API-owning authority. A local rule may extend a package default without conflict.

### `AFCC-PRE-002` — Treat the installed API owner as factual truth

Project policy may override a generic recommendation, but it cannot make an unavailable API exist. For a named package API, menu, mode, or supported operation, the actually installed owner package guide and public surface are factual authority. Classify a stale or broader claim as `Package/API Mismatch`, select the installed surface, and recommend a separate compatibility decision instead of calling an unsupported operation.

### `AFCC-AUT-001` — Separate tool access from edit authority

Package, Unity, filesystem, and Agent Skill access do not authorize edits. `code-convention-apply` becomes eligible for implicit selection only after the user authorizes a concrete Unity code change and scope. That authorization does not extend to assets, settings, migrations, Jira, Git workflow, publishing, deployment, or unrelated refactors.

### `AFCC-CHG-001` — Preserve state and keep changes surgical

Inspect the current implementation, nearby style, ownership, call sites, serialized data, and existing user changes before editing. Modify only the authorized scope. Do not fold unrelated cleanup, renaming, architecture migration, settings changes, or broad reserialization into the task. Preserve existing values and references unless the user approved the exact data change.

### `AFCC-ADP-001` — Adopt progressively

Apply these rules first to new files, new features, and isolated changes. Do not remodel an established project merely because its structure differs. Introduce EventBus, QueryBus, Command, registries, providers, or finer asmdef boundaries only when the observed ownership and scale require them.

### `AFCC-STY-001` — Preserve established style when no selected rule applies

When neither the selected profile nor a higher authority defines a style choice, preserve the touched file's established namespace, formatting, member ordering, and naming. Do not normalize neighboring code or migrate an existing namespace merely to make the file resemble an example in this package.

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

This package requires `com.actionfit.referencebinding`. Read its installed `AI_GUIDE.md` and use only the public APIs and menus documented by that version. The dependency makes the owner available but does not add references to consuming custom asmdefs. This package does not define attributes, processing modes, bulk wiring, asset-saving APIs, or another ReferenceBinding implementation. If a local document names an API the installed package does not expose, report `Package/API Mismatch` and follow the installed package guide.

## ActionFit Unity Profile Rules

The following stable meanings are active only when `AFCC-PRO-001` selects `actionfit-unity`. Detailed selection examples and capability evidence live in `Skills~/Shared/references/profiles/actionfit-unity.md`.

### `AFCC-TRE-001` — Compose ownership as a tree-oriented DAG

Model the game's ownership and dependency direction as a tree-oriented view: one or more composition roots assemble coherent feature and service nodes, each node has one explicit lifecycle and state owner, and ordinary dependencies point from the composition owner toward the nodes it owns. The concrete dependency graph may be a directed acyclic graph because a reusable service can have multiple consumers; cycles remain prohibited. This rule describes ownership and dependency direction, not a required Unity Transform hierarchy, inheritance tree, class name, folder tree, or one-root runtime object graph. Apply it progressively to new or explicitly revised boundaries and do not remodel the whole project without separate authority.

### `AFCC-PKG-001` — Package coherent reusable nodes behind one-way dependencies

Treat a node as a package candidate only when project-neutral rules, state, lifecycle, and validation can be separated into a coherent capability with one-way dependencies. A reusable package assembly must not reference consuming-project types, scenes, prefabs, ScriptableObjects, save keys, asset IDs, or a concrete third-party SDK. Split engine, UI, and adapter packages only when observed ownership, replacement, compilation, or reuse boundaries justify the split; package count and maximum fragmentation are not goals. Preserve a project-owned composition layer for concrete bindings and migrations.

### `AFCC-PRT-001` — Expose evidenced ports and bind project adapters at composition roots

When a package genuinely requires an external capability, expose the narrowest consumer-oriented port that the package can own and bind the consuming project's adapter at a composition root. Keep project implementations, concrete SDKs, scene access, storage keys, and environment configuration outside the reusable package. Provide a neutral default only when its behavior is semantically safe and explicit. This rule does not override `AFCC-INT-001`: one hypothetical implementation, test convenience, dependency-injection registration, or naming symmetry does not justify a port. Do not add a dependency-injection container or service locator merely to perform the binding.

### `AFCC-ORG-001` — Organize classes by functional regions

Use functional `#region` blocks for non-trivial ActionFit classes. Keep global fields and properties separate from feature-specific members. Use this order when a block exists: `Fields`, `Properties`, `Unity Lifecycle`, `Initialization`, `Public Methods`, `Private Methods`, `Event Handlers`. Do not add empty regions or reorganize untouched code solely for consistency.

### `AFCC-CMT-001` — Keep comments useful and language-consistent

Write new explanatory comments in Korean unless the touched file is clearly English-only. Document public method usage with XML summaries, explain non-obvious private or protected behavior briefly, and add concise same-line field or property comments where they provide meaning. Omit comments for self-explanatory code and simple expression-bodied getters.

### `AFCC-LOG-001` — Keep diagnostics visible and searchable

Write log messages in concise English using `[Owner] Action: detail`. Temporary investigation logs use the engine logger and a searchable `[DEBUG_Feature]` tag and are removed before completion. Editor tools and validation code use a logger proven to remain compiled and visible in the Editor; runtime code uses the consuming project's approved runtime logger. Never name or assume a project-specific logger or compilation symbol in this profile.

### `AFCC-GRD-001` — Keep abnormal guard exits observable

Before returning from a null, range, state, or other defensive guard that should not occur in normal flow, emit an error through the approved diagnostic path with enough owner and field context to investigate. Do not log expected absence such as an optional value, cache miss, capability probe, or normal false result as an error.

### `AFCC-CPP-001` — Preserve method discoverability across compilation symbols

Keep a method declaration searchable and put conditional compilation inside its body when the behavior varies by symbol. Conditional `using` directives and declarations that cannot compile without a platform-specific base type are exceptions. Do not duplicate whole method declarations across symbol branches when one stable declaration can contain the branch.

### `AFCC-PRF-001` — Avoid scene-wide discovery in runtime paths

Do not add runtime scene-wide `FindObjectOfType`, `FindObjectsByType`, or `FindAnyObjectByType` calls. Prefer an existing serialized or injected reference, approved owner/singleton, cached hierarchy lookup, or event/provider boundary. Editor-only tools may use scene-wide discovery when their scope and cost are explicit. An external API that requires discovery is an evidenced exception, not a reason to spread the pattern.

### `AFCC-INT-001` — Prefer concrete ownership over speculative interfaces

For new ActionFit code, prefer a concrete owner type and a direct, serialized, or injected reference. Do not add an interface solely for one implementation, a speculative future replacement, dependency-injection registration, test substitution, naming symmetry, or to hide unclear ownership or dependency direction. Treat the query or read-only runtime interface permitted by `AFCC-COM-001` as an evidenced exception after considering a concrete owner or query API.

An interface is justified only when an installed or external API owner requires it, two or more active production implementations must be interchangeable, platform or runtime variants need one stable consumer contract, or a stable cross-assembly ownership boundary cannot remain one-way without a small implementation-free contract. Keep an accepted interface narrow, consumer-oriented, and read-only by default; route mutations through an explicit owner API or command. Resolve and cache the dependency once instead of repeatedly locating an interface in a hot path. Existing interfaces are not automatic migration targets and require separate change authority. Do not mechanically replace an interface with an abstract class; use an abstract base only when real shared state, behavior, or inheritance semantics exist. Unit-test substitution alone is insufficient unless the same boundary represents a real production adapter or owner contract.

### `AFCC-EAR-001` — Keep Editor asset references relocatable

For Editor tools, do not encode a movable project asset or folder as a fixed path constant when the project already supports a serialized asset reference, GUID-backed lookup, or an evidenced project finder. Preserve the selected asset's GUID and make missing or ambiguous lookup visible. A package-owned immutable path and a script-relative generated output are evidenced exceptions. Concrete finder APIs remain factual project architecture or installed-owner contracts.

### `AFCC-UTK-001` — Use UniTask when that capability is installed

When UniTask is evidenced, use it for new asynchronous, delayed, and periodic work instead of introducing a coroutine. Preserve an `IEnumerator` flow when a Unity or external API requires that exact shape. Accept and propagate cancellation, pair owned cancellation sources with the active lifetime, use `WaitUntil` for condition waits instead of hand-written polling, and observe failures. Do not convert an unrelated existing coroutine merely because a nearby file is touched.

### `AFCC-DUR-001` — Express gameplay durations in seconds

Represent gameplay duration values as `float` seconds by default. Convert explicitly at an API boundary that requires milliseconds, ticks, frames, or another unit, and make the unit visible in the name or type when ambiguity remains.

### `AFCC-LOP-001` — Use an evidenced project loop owner for periodic work

When the consuming project documents a central loop owner, route new periodic runtime work through the appropriate evidenced loop phase instead of adding another `Update` or `LateUpdate`. Register and unregister at matching active lifetimes. Keep Unity lifecycle callbacks and external-SDK callbacks that are semantically tied to their component or required API. The concrete loop type and event names remain factual project architecture.

### `AFCC-RFS-001` — Deprecated: use the original mixed public Refs shape only for compatibility

This rule retains the original meaning for existing serialized code: Inspector-connected component references and closely related presentation settings may remain in a nested public `[Serializable]` `Refs` container with a public `refs` instance. Do not apply this mixed public shape to new or deliberately revised fields. Use `AFCC-RFS-002` and `AFCC-SER-004` instead. Moving an existing field out of `refs` changes its serialized property path and requires separately approved migration and asset validation.

### `AFCC-RFS-002` — Separate ActionFit serialized inputs by role

For new or deliberately revised ActionFit serialized inputs, use nested public sealed `[Serializable]` containers with distinct roles. `Refs` contains only `Component` references from the owner GameObject or any descendant, including inactive descendants. `Assets` contains only persistent external Unity asset references such as sprites, materials, audio clips, ScriptableObjects, and prefab assets. `Settings` contains numeric and other non-reference Inspector-authored configuration values, not runtime state, mutable collections, save DTOs, or persistence schemas. Keep every container's serialized backing fields private and expose getter-only properties under `AFCC-SER-004`. Do not add `Tooltip`. A standalone serialized field remains valid when a container would obscure ownership. Concrete component wrappers, attribute support, persistence checks, and reference-binding shapes belong to their installed owner guides.

### `AFCC-SER-004` — Keep Inspector-authored inputs runtime-read-only

Establish a serialized input only through a declaration default, Unity deserialization, or explicit Editor-only authoring while the application is not playing or entering Play Mode. Use private `[SerializeField]` backing fields and getter-only accessors for `Refs`, `Assets`, `Settings`, and their contained values. Do not expose setters or mutation methods, and do not reassign a container, reference identity, or setting from runtime code. When gameplay needs a changing value, copy the authored input into a separately owned runtime model and mutate that state instead. This rule freezes the stored value or reference identity; it does not make the referenced Component or asset object's own state immutable. Editor attributes, `SerializedObject`, and installed owner tooling may author private fields before Play Mode, but must not create a Player or Play-Mode mutation path. Getter-only guidance does not mechanically block reflection or manual Play-Mode Inspector edits; a consuming project that needs enforcement beyond ordinary C# access must use an explicitly owned analyzer or custom Inspector rather than claiming this guidance alone provides it.

### `AFCC-SOS-001` — Select singleton ScriptableObjects by state ownership

When `com.actionfit.sosingleton` is installed, use its documented singleton base and load contract only for one globally referenced configuration or catalog asset that does not require multiple variants. Keep per-character, per-item, per-season, mutable session, or otherwise multi-instance data in regular ScriptableObjects or runtime owners. Read the installed owner guide before naming the base type, Resources path, cache, or menu; package installation does not authorize creating or moving an asset.

### `AFCC-TWN-001` — Preserve DOTween ownership when that capability is installed

When DOTween is evidenced, never treat an auto-killed tween field or `IsActive()` result as ownership proof. For a fixed repeatable animation, create one non-auto-killed tween, restart it, and kill it at the owner's final lifetime. For variable animations, assign a class-owned unique ID and kill only that ID. Create natural one-shots without a retained field. A target-wide kill is permitted only when one system exclusively owns every tween on that target; shared targets require per-system IDs.

### `AFCC-SER-003` — Use approved targeted serialized-key migration in this profile

After explicit approval of a Unity-serialized field rename, use this profile's targeted key-only procedure when the consuming repository can prove text serialization, an exhaustive old-key scope, preserved values and object references, targeted diff inspection, and asset reload validation. Otherwise fall back to `AFCC-SER-002` or do not rename. An installed API owner may require a narrower migration contract. This rule never creates rename or asset-write authority.

### `AFCC-UIF-001` — Route UI wrappers and localization to the installed owner

When `com.actionfit.ui.foundation` is installed, use its documented public wrapper and localization contracts for relevant ActionFit UI work. Read the installed guide before selecting a concrete type, registration path, refresh lifecycle, migration command, or optional animation mode. If the owner is absent or its guide does not expose the needed behavior, report missing evidence or `Package/API Mismatch`; do not invent a wrapper or API.

### `AFCC-RET-001` — Retire local convention authority only after a no-write gate

Local convention documents may be removed only after a read-only shadow audit maps every normative item to portable core, the selected profile, an installed owner, factual architecture, or explicit retirement. The audit must also prove zero unresolved `Local Only` and `Conflict — Local Wins` rows, zero missing owner routes, zero stale links after removal, and zero package-to-installed-skill drift. Deletion remains a separately authorized repository operation; the check itself never writes.

## Convention Comparison Contract

`code-convention-check` uses exactly six relationship categories:

- `Aligned`: local and package sources require materially the same behavior.
- `Local Extension`: the local rule adds a compatible project-specific requirement.
- `Conflict — Local Wins`: the sources prescribe incompatible behavior and project policy wins.
- `Package Default`: no local counterpart is documented; use `N/A` for the local source.
- `Local Only`: no package counterpart exists; use `N/A` for the package rule ID.
- `Package/API Mismatch`: a generic, historical design-input, or local claim exceeds the installed owner package's real public surface; the installed owner guide wins.

Every row includes the package rule ID, category, local or owner source path, effective rule, and recommended follow-up. The report cites sources, identifies missing evidence, and never claims that all source code complies. The `AFCC-REF-001` design-input exclusion is reported as an owned-package `Package/API Mismatch` against the required ReferenceBinding owner, without falsely attributing the excluded design to local project documents.

Retirement readiness is reported separately from these six categories. Read `Skills~/Shared/references/local-convention-retirement.md` for shadow and final gates, count definitions, stale-link checks, and skill-drift evidence. A readiness result is not source-code compliance proof and does not authorize deletion.

## Project-Specific Convention Boundary

Reusable organization choices may live in an explicitly selected package profile. Concrete project types, loop event names, clock facades, storage paths, popup interfaces, service adapters, asset keys, and current runtime ownership remain factual project architecture or installed API-owner guidance. Do not copy those project-only identifiers into portable core or an organization profile.

A consuming project may operate with no local code-convention documents. Its primary router may contain only the package authority pointer and exact profile selector, while project safety, workflow, and factual architecture stay local for their separate responsibilities. If local convention documents remain during migration, compare them through the normal precedence and retirement contracts until removal is explicitly authorized.

## Validation And Reporting

### `AFCC-VAL-001` — Validate in proportion to the changed contract

Start with call-site inspection, targeted searches, and diff review. Add compile, EditMode, PlayMode, validation-menu, asset, persistence, or manual QA evidence according to the risk. A successful refresh request is not compilation proof. Separate regressions from known issues and infrastructure failures. Unity-only risks cannot be closed by static inspection alone.

### `AFCC-REP-001` — Report decisions and remaining evidence

Report changed files, ownership/state/communication decisions, validation performed, unverified behavior, remaining risks, and any local-versus-package conflict with the selected authority. Include the Decision Log when `AFCC-DEC-001` applies. Do not claim package publication, deployment, gameplay validation, or a clean worktree without evidence.

## Agent Skills

- `Skills~/manifest.json` registers schema v2 `code-convention-help`, `code-convention-check`, and `code-convention-apply` for Codex and Claude with prefix `code-convention`.
- The help skill is read-only and reads generated `PACKAGE_SKILLS.md` as the authoritative inventory.
- The help skill resolves and reports the selected profile, effective stable IDs, capability gates, and installed owner routes.
- The check skill is read-only. It compares documented rules, uses the six stable relationship categories, reports shadow or final retirement readiness, detects package-to-installed-skill drift, and proves repository state did not change.
- The check skill does not inventory or judge every source file. Use the separately installed AI Refactor package when a user requests an evidence-backed source inventory and staged architecture proposal.
- The apply skill is write-capable but may be selected only after the user authorizes a concrete Unity code change. It works without local convention documents by reading the selected profile and installed owner guides. Project architecture supplies concrete facts, not an independent convention body. The `AFCC-TRE-001`, `AFCC-PKG-001`, and `AFCC-PRT-001` target applies only inside separately authorized architecture or package scope with observed evidence. The skill does not create edit authority or own Jira, Git branches, worktrees, pull requests, publishing, or deployment.
- `Skills~/Shared/references/unity-code-authoring-rules.md` contains progressive details for architecture, communication, persistence, lifecycle, assets, assemblies, anti-patterns, and validation.
- `Skills~/Shared/references/profiles/actionfit-unity.md` contains the opt-in profile's activation, capability, examples, and validation detail.
- `Skills~/Shared/references/owner-routing.md` resolves concrete Time, UI Foundation, and ReferenceBinding contracts through installed guides.
- `Skills~/Shared/references/local-convention-retirement.md` defines the no-write shadow and final retirement gates.
- Custom Package Manager installs project-local copies and preserves unknown, modified, file-backed, or linked targets. Do not author `PACKAGE_SKILLS.md` in package sources.

## Package Tools Menu

- Unity menu root: `Tools/Package/AI Code Convention/`.
- `README` opens the installed package README.
- `Assets/Create/Scripting/ActionFit Convention MonoBehaviour Script` creates one new convention starter through Unity's native Project window flow.
- The package has no settings asset. Keep the `Tools/Package` README entry in its existing README priority band; the creation command remains under `Assets/Create/Scripting`.

## Package Validation

- Run `Tests/Shell/run-tests.sh` for the package guidance, metadata, skill-parity, menu-source, and template-text contracts.
- Run the `com.actionfit.ai-codeconvention.Editor.Tests` EditMode assembly to prove the package template is importable through its virtual `Packages/` path, retains the Unity tokens and runtime-read-only role shape, compiles against the ReferenceBinding Runtime assembly, and preserves the declared attributes and Editor-guarded owner queue.
- Run isolated Unity package validation after Editor menu, template, asmdef, or test changes.
- Before release, perform one interactive smoke test in a disposable predefined-assembly destination and one destination whose custom asmdef already references `com.actionfit.referencebinding`: create, rename, confirm root namespace expansion, compile, and remove only the smoke-test output. Do not use an existing user script as the target or edit an asmdef merely for the smoke test.

## Release And Distribution Boundary

- This `0.4.0` candidate is Private because its design input does not include a public redistribution license notice.
- A separate ownership and distribution-rights review is required before changing visibility or publishing publicly.
- Publishing is manual through Custom Package Manager. Do not create a repository, push, tag, append a catalog row, deploy, or install into global/home skill directories without separate authorization.
- Before any later release, re-check remote tags and align `package.json`, README, this guide, PackageInfo, and release notes.
