# Unity Code-Authoring Reference

Use this reference only after reading the consuming repository's instructions and the installed `AI_GUIDE.md`. The guide owns the stable `AFCC-*` rules; this file supplies selection detail, examples, anti-patterns, and validation depth.

## Contents

1. [Architecture and state](#architecture-and-state)
2. [Communication selection](#communication-selection)
3. [Persistence and live economy](#persistence-and-live-economy)
4. [Lifecycle, async, and static state](#lifecycle-async-and-static-state)
5. [Assets, serialization, and assemblies](#assets-serialization-and-assemblies)
6. [Anti-pattern review](#anti-pattern-review)
7. [Validation matrix](#validation-matrix)

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

Serialized-reference attributes, validation, and repair APIs belong to the installed ReferenceBinding package when present. Read `com.actionfit.referencebinding/AI_GUIDE.md`; do not infer write or save operations from this generic reference.

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
- serialized rename, GUID change, asset reset, or reserialization without an approved migration;
- persistence schema change without fixtures and recovery;
- public API change mixed with unrelated refactoring.

An existing occurrence is evidence, not automatic authority to fix it. Report it and split remediation into a separately authorized task unless the current scope explicitly owns it.

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

For every check, record the exact scope and distinguish package failures, project regressions, known issues, environment failures, and unverified manual behavior.
