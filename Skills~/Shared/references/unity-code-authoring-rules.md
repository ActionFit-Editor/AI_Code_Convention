# Unity Code-Authoring Reference

Use this reference only after reading the consuming repository's instructions and the installed `AI_GUIDE.md`. The guide owns the stable `AFCC-*` rules; this file supplies selection detail, examples, anti-patterns, and validation depth.

## Contents

1. [Rule selection](#rule-selection)
2. [Architecture and state](#architecture-and-state)
3. [Tree-oriented package target](#tree-oriented-package-target)
4. [Communication selection](#communication-selection)
5. [Persistence and live economy](#persistence-and-live-economy)
6. [Lifecycle, async, and static state](#lifecycle-async-and-static-state)
7. [Assets, serialization, and assemblies](#assets-serialization-and-assemblies)
8. [Anti-pattern review](#anti-pattern-review)
9. [Validation matrix](#validation-matrix)

## Rule Selection

Apply portable core without requiring a selector. Read `references/profiles/actionfit-unity.md` only when the primary project router contains the exact selector required by `AFCC-PRO-001`. Read `references/owner-routing.md` before choosing a concrete package API. Missing capability evidence leaves an optional rule inactive; it never authorizes dependency installation or symbol changes.

Project safety, workflow, and factual architecture still supply higher-scope constraints and concrete mappings. They do not need to duplicate the selected package's code-convention body.

## Architecture And State

Prefer the smallest ownership model that makes creation, mutation, and disposal clear.

| Conceptual role | Responsibility | Must not imply |
| --- | --- | --- |
| Scene composition | Create roots and connect scene dependencies. | A required `SceneController` class name. |
| Gameplay composition | Bind independent feature roots. | Direct sibling implementation references. |
| Session owner | Own ready, playing, paused, failed, and finished transitions. | Global mutable static session state. |
| Feature owner | Own feature rules, runtime model, dynamic objects, and cleanup. | A mandatory `FeatureRoot` base class. |

Choose state by authority:

- Configuration assets: source data, balance, catalogs, and asset references.
- Runtime model or session: values that change during the current run.
- Save DTO/schema: durable reconstructable values, never scene instances or components.
- Server authority: payment, reward, currency, ranking, or other cheat-sensitive truth in live features.

For an established project, map these responsibilities onto its current managers, roots, providers, and folders. Do not introduce the conceptual names solely to match this document.

Adopt progressively:

- MVP: explicit owner, direct calls, callbacks, matching cleanup, cancellation, Runtime/Editor separation.
- Growth: add cross-boundary facts, read-only queries, asset providers, or asmdefs only after real coupling appears.
- Advanced: registries, remote rollout, server validation, and finer assembly boundaries only when live operation or team scale requires them.

## Tree-Oriented Package Target

When the selected profile activates `AFCC-TRE-001`, begin with an ownership tree and enrich it into a directed acyclic dependency graph. Composition roots assemble feature and service nodes. Each node owns one coherent state and lifecycle boundary, while a shared lower-level node may serve more than one consumer. Cycles, child-to-root reach-through, and sibling implementation references indicate an ownership decision that still needs resolution.

Apply `AFCC-PKG-001` only after direct source evidence shows a reusable, project-neutral capability. A package boundary must keep dependencies one-way and exclude project types, scene/prefab references, project-owned ScriptableObjects, save keys, asset IDs, and concrete SDKs. Engine/UI/adapter separation is useful only when those concerns have different reuse or ownership; smaller packages are not inherently better.

`AFCC-PCR-001` permits a concrete composition layer to live in one product-owned, non-reusable package without weakening reusable-package neutrality. The package opts in only through the exact complete trimmed markers `AI Product Composition Root: <package-id>` and `AI Refactor target: package-oriented-product` inside its root guide's `## Package Identity`; the actual ID must equal the sibling manifest `name`. Resolve embedded packages before PackageCache and accept at most one declared product root. The marker pair does not select the code-convention profile, create edit authority, or prove that any migration has happened. Absence retains the generic architecture target; invalid or competing declarations are missing evidence or structural diagnostics, not permission to infer intent.

Apply `AFCC-PRT-001` with `AFCC-INT-001`. A port represents a real external capability that a reusable node consumes. The package owns the narrow consumer-facing contract; a project composition root owns adapter selection and binding. One hypothetical implementation, test substitution alone, or a desire to add a DI container is not sufficient evidence. A neutral default must preserve semantics and must not turn missing required behavior into silent success.

When `AFCC-BND-001` applies, keep new scene-facing `MonoBehaviour` classes as thin binders: they own Unity lifecycle, serialized `Refs`/`Assets`/`Settings`, subscriptions, and explicit calls. Plain C# feature owners hold reusable state and rules. This is a progressive boundary, not permission to rewrite every existing component.

When `AFCC-ANI-001` applies, pass exact animation targets and settings from the binder into non-serialized animation helpers. The helper owns only runtime handles it creates and pairs them with cleanup. Capability-specific rules such as DOTween ownership still apply.

When `AFCC-PKG-002` applies, keep Origin/Core free of optional UI, animation, SDK, ReferenceBinding, and project assemblies. Add inward-dependent Leaf packages only for independently replaceable dependency axes. Default installers may select the complete set, while direct consumers may choose a smaller dependency closure. One package per class and dependency cycles remain anti-patterns.

Architecture analysis and implementation remain separate authorities. A read-only analysis can propose target nodes, package candidates, ports, adapters, phases, and validation, but it cannot create edit, migration, package publication, or whole-project remodeling authority.

## Communication Selection

| Intent | Default mechanism | Owner |
| --- | --- | --- |
| Parent controls child | Direct call | Parent/composition owner |
| Child reports upward | C# event or callback | Child defines notification; parent subscribes |
| Siblings collaborate | Parent binding | Common composition owner |
| Distant owners observe a completed fact | EventBus | Domain where the fact occurred |
| Distant owner reads current state | Query or read-only runtime interface | State owner |
| Caller requests a state change | Owner API or Command | State owner |

"Distant" means separated by ownership, not hierarchy depth.

### EventBus

Use an event for a completed fact such as `OrderCompleted` or `RewardClaimSucceeded`. Do not model a query, setter, claim request, payment request, or required single-owner action as an event.

- Prefer IDs, coordinates, enums, numbers, and immutable snapshots in payloads.
- Avoid mutable collections, scene objects, implementation instances, and per-frame bulk data.
- Place event types with the domain that emits the fact; do not centralize every payload in a generic events file.
- Default to synchronous main-thread dispatch unless the installed implementation documents otherwise.
- Do not rely on subscriber order or replay. Read current state from its owner.
- Define exception isolation and re-entrant publish behavior in the bus implementation contract.
- Subscribe and unsubscribe at matching lifetime boundaries.

An existing project event hub is a local contract. Do not replace it simply because this reference uses the term EventBus.

### Query

Register only read-only providers at an owner boundary. Queries should be observably side-effect free.

- Define duplicate registration and stale-token disposal behavior.
- Return immutable or versioned snapshots when collection consistency matters.
- Keep cache invalidation explicit.
- Avoid service-locator use, leaf-object registration, and repeated hot-path lookup.
- Keep Unity object access on the main thread unless the concrete provider proves otherwise.

### Command Or Owner API

Use a command or owner API when the caller requests mutation.

- Return success, failure, and cancellation evidence.
- Accept cancellation for asynchronous work.
- Define duplicate-call behavior for rewards, payments, currency, and server requests.
- Publish a completed fact only after the mutation reaches the contractually required durable state.
- Do not move every write into one global command bus.

## Persistence And Live Economy

Treat save data as an external contract rather than a dump of runtime memory.

- Store stable IDs, numeric or string values, explicit enum values, versions, and reconstructable DTOs.
- Preserve key names, field names, enum numbers, schema versions, and time bases.
- Make migration idempotent. Write the completion marker after durable target data.
- Define source of truth and ordering for aggregate/child keys, cloud/local copies, account changes, and recovery.
- Invalidate runtime, UI, and query caches when reset or migration changes their source.
- Test previous-version load, repeated migration, partial write, retry, and forced termination.

For reward or live-economy operations:

1. Determine trusted authority and verification.
2. Define the idempotency key or durable receipt.
3. Persist duplicate-prevention evidence at the correct point before grant.
4. Define retry, ledger, compensation, and forced-termination recovery.
5. Define server time, rollout, kill switch, fallback, and rollback when remote control is involved.

Encryption or obfuscation may protect local data but does not replace trusted authority.

## Lifecycle Async And Static State

Pair every acquisition with cleanup at the same boundary:

```text
Awake      -> OnDestroy
OnEnable   -> OnDisable
Initialize -> Dispose or Clear
Open       -> Close
OnSpawn    -> OnDespawn
```

- Guard repeated initialization or clean the previous registration first.
- Treat `OnDestroy` as a final safety net, not a substitute for a shorter active lifetime.
- Reset pooled state and subscriptions before return.
- On partial initialization failure, release completed steps in reverse order.
- Make `Dispose` safe for partial and repeated calls when the owner contract requires it.

Async work should accept the project's approved cancellation type and use the boundary that actually ends the work: destroy, disable, close, pool return, scene unload, or shutdown. Await meaningful work, surface failure, and do not detach a task merely to simplify the caller.

Static fields and events survive scene unload and may survive Play Mode transitions. Assign a reset owner and validate the project's domain-reload configuration. Do not change that project-wide configuration as an implementation shortcut.

## Assets Serialization And Assemblies

The creator or factory owns dynamic instances, pool return, and resource handles. Keep resource paths and keys searchable. A load handle must outlive every dependent instance.

Treat these as compatibility contracts:

- `.meta` GUID and asset path identity;
- serialized field and managed-reference type names;
- explicit enum numeric values;
- asmdef names and dependency direction;
- Addressables keys and labels;
- scene, prefab, ScriptableObject, and project-setting values.

Before a rename, move, copy, or migration, read the project's approved procedure. Preserve an existing `.meta` when retaining identity; let Unity create a new GUID for a genuinely independent asset. Never duplicate a GUID in one AssetDatabase. Avoid broad YAML rewrites and remove unrelated serialization churn.

When the selected profile activates `AFCC-SER-004`, treat Inspector-authored serialized inputs as immutable runtime input. Keep their backing fields private, expose getter-only access, and move changing values into a separate runtime model. Editor-only authoring may establish those fields before Play Mode, but runtime code must not replace the stored values or reference identities. A getter-only reference does not make the referenced object's own mutable state immutable.

Serialized-reference attributes, validation, and repair APIs belong to the required ReferenceBinding owner package. Read `com.actionfit.referencebinding/AI_GUIDE.md`; do not infer write or save operations from this generic reference. Its package dependency makes the Runtime assembly available to predefined assemblies, but a custom consuming asmdef still needs an explicit `com.actionfit.referencebinding` reference.

When the selected profile activates `AFCC-RFS-003`, treat each newly created or deliberately revised supported mandatory `Refs` Component field as selector-owned. Use `RequiredReference` and `AutoWireChild` together plus the Editor-guarded owner enqueue. Resolve duplicate same-type/same-name candidates through an existing valid serialized reference or an explicit user decision. Any temporary duplicate rename requires exact asset-edit authority, deterministic collision-free naming, old/new hierarchy path reporting, runtime-name and Animation-binding impact checks, targeted serialized diff review, and reload validation. Do not weaken the rule into first-match selection, runtime lookup, or an optional attribute merely because the hierarchy is ambiguous.

Assembly direction:

```text
Editor -> Runtime
Runtime -X-> Editor
Tests -> the assemblies they verify
```

Keep `UnityEditor` outside Player compilation. Put configuration types in Runtime when players need them. Add contract assemblies only for stable cross-feature contracts, and do not move arbitrary types into Shared to break a dependency cycle.

## Anti-Pattern Review

Flag these patterns before adding more of them:

- project-wide remodel or unrelated cleanup inside a feature task;
- God manager, mutable global session singleton, or uncleared static event;
- direct sibling implementation dependency or child-to-parent reach-through;
- UI mutating domain state directly;
- ScriptableObject used as changing session state;
- SaveData read and written as if it were an in-memory model;
- EventBus used for request/response, setters, or every-frame bulk data;
- Query used for mutation or as a general service locator;
- leaf objects coupled directly to global buses;
- detached async work without cancellation or observed failure;
- resource handle whose owner or release boundary is unknown;
- Runtime assembly referencing Editor code;
- fixed Editor project paths for movable asset or folder references when a serialized or GUID-backed route exists;
- singleton ScriptableObject selected without proving single-instance configuration ownership or reading its installed owner;
- serialized rename, GUID change, asset reset, or reserialization without an approved migration;
- public setters, mutation methods, or runtime assignments for profile-owned Inspector inputs that `AFCC-SER-004` requires to remain read-only;
- persistence schema change without fixtures and recovery;
- public API change mixed with unrelated refactoring.
- package extraction proposed only because a folder or class can be made smaller;
- a so-called tree that hides shared dependencies, cycles, lifetime ownership, or composition bindings;
- package-oriented product composition inferred from package presence, repository identity, dependency names, folders, or source style instead of the exact package-owned marker pair;
- duplicate, incomplete, misplaced, mismatched, or unsupported product-root declarations, or a product-owned composition root presented as a reusable package;
- project types, scenes, save keys, asset IDs, or concrete SDKs referenced from a reusable package assembly;
- one interface per implementation, a DI container, or a service locator introduced to make package wiring uniform;
- a scene binder that duplicates reusable feature state or animation rules instead of explicitly calling their owners;
- an animation helper that serializes the scene target it should receive from its caller;
- an Origin/Core package that imports optional UI, tween, SDK, ReferenceBinding, or project assemblies;
- profile or optional-library behavior inferred without an exact selector and capability evidence;
- a concrete package API selected without reading the installed owner guide;

An existing occurrence is evidence, not automatic authority to fix it. Report it and split remediation into a separately authorized task unless the current scope explicitly owns it.

### Documentation completion gate

Apply `AFCC-DOC-001` after the final diff is known. Re-read every governing and final-diff-routed document completely, reconcile it with the implemented ownership and validation paths, and then run each repository-declared documentation or package validator. Semantic re-reading and mechanical validation are independent completion requirements.

## Validation Matrix

Run the smallest evidence that can prove the changed contract, then add risk-specific checks.

| Change | Minimum evidence | Add when risk applies |
| --- | --- | --- |
| General C# | call sites, targeted diff, compile | PlayMode or manual QA for gameplay flow |
| API/event/query/command | publishers/providers/consumers, cleanup | EditMode/PlayMode for failure, cycles, duplicates |
| Async/lifecycle | success, cancellation, partial failure, disposal | unload, retry, shutdown, pooled reuse |
| Save schema | previous fixture, migration repeat | forced termination, duplicate reward, cloud conflict |
| asmdef/namespace/type move | Editor and minimum Player compile, direction | Missing Script/reference and serialized-type checks |
| Asset identity or serialization | path/GUID/meta pair, targeted diff | reload, prefab variant, scene, Addressables checks |
| Dynamic asset/load | key, failure, release ownership | memory/profile and cold remote load |
| Static/event hub | re-entry and cleanup | domain reload disabled when supported |
| Live/remote data | default, range, failure fallback | rollout, kill switch, rollback, server compatibility |
| Profile or owner route | exact selector, capability and installed guide | negative fixture without the optional capability |
| Tree/package/product-root/port target | owner and edge map, cycle check, project-coupling evidence, exact product marker pair and manifest match when opted in, qualifying port evidence | phased migration and project-adapter compatibility plan |
| Binder/animation/Leaf boundary | serialized owner, plain-logic compile, explicit animation targets, dependency-isolation compile | lifecycle cleanup, optional integration matrix, default-bundle closure |
| Convention retirement | shadow mapping, stale-link and skill-drift audit | package-only rerun after approved deletion |
| `AFCC-DOC-001` documentation completion gate | complete re-read of governing and final-diff-routed documents, exact repository validator command and result | CI failure propagation, owner or package version drift, unrelated blocker classification |

For every check, record the exact scope and distinguish package failures, project regressions, known issues, environment failures, and unverified manual behavior.
