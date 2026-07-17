# ActionFit Unity Profile

- Profile ID: `actionfit-unity`
- Base profile: `portable-core`
- Selector: `AI Code Convention profile: actionfit-unity`
- Default when absent: `portable-core`

The root `AI_GUIDE.md` owns every stable `AFCC-*` meaning. This reference supplies activation evidence, examples, and validation detail for the selected profile.

## Activation Contract

Accept the profile only when the primary project router contains exactly one selector whose complete trimmed line matches the value above. Do not infer it from repository identity, organization, folder layout, source style, installed packages, or dependency names. An unknown or duplicate selector is an error requiring clarification.

Profile selection does not activate every optional rule. Apply `AFCC-PRO-002` independently for each capability:

| Capability | Minimum evidence | Activated rule | Inactive behavior |
| --- | --- | --- | --- |
| UniTask | installed package, assembly, or compiling `Cysharp.Threading.Tasks` source | `AFCC-UTK-001` | use only portable `AFCC-ASY-001`; do not install UniTask |
| Project loop owner | factual architecture or installed owner guide naming a current loop contract | `AFCC-LOP-001` | keep the smallest existing Unity lifecycle pattern |
| DOTween | installed and assembly-visible `DG.Tweening` API | `AFCC-TWN-001` | do not add a symbol, dependency, shim, or DOTween call |
| UI Foundation | installed `com.actionfit.ui.foundation` guide and relevant public contract | `AFCC-UIF-001` | use portable ownership rules and report missing owner evidence |
| SO Singleton | installed `com.actionfit.sosingleton` guide and a single global configuration/catalog ownership decision | `AFCC-SOS-001` | keep the established regular ScriptableObject or runtime owner |
| Targeted serialization migration | explicit rename approval, text-serialized assets, exhaustive old-key scope, and asset reload validation | `AFCC-SER-003` | use `AFCC-SER-002` or do not rename |

## Profile Rule Details

### Organization and comments

- `AFCC-ORG-001`: use only populated functional regions and keep feature-specific members with their feature. Reordering an untouched class is not part of applying the rule.
- `AFCC-CMT-001`: write new explanatory comments in Korean unless the file is clearly English-only. Public method summaries explain caller-facing use; private comments explain non-obvious intent. Omit noise and simple expression-bodied getter comments.

```csharp
#region Fields
[SerializeField] private float duration = 0.5f; // 연출 시간(초)
#endregion

#region Public Methods
/// <summary>현재 상태에서 연출을 시작합니다.</summary>
public void Play() => PlayInternal();
#endregion
```

### Logging and guards

- `AFCC-LOG-001`: keep messages concise, English, and searchable as `[Owner] Action: detail`.
- Use an engine-visible logger for temporary and Editor diagnostics. Runtime logging follows the consuming project's evidenced logger contract.
- Mark temporary diagnostics with `[DEBUG_Feature]` and remove them before completion.
- `AFCC-GRD-001`: log an abnormal guard exit with owner and failed state; do not turn expected optional absence into an error.

```csharp
if (target == null)
{
    UnityEngine.Debug.LogError("[ExampleView] Initialize: target is null");
    return;
}
```

### Conditional compilation and discovery

- `AFCC-CPP-001`: keep the method declaration stable when only behavior varies by symbol. Guard the complete declaration when the callback contract itself is Editor/platform-only or cannot compile outside that target; wrap the complete Unity `OnValidate` method in `#if UNITY_EDITOR`.
- `AFCC-PRF-001`: prefer existing serialized/injected references, owner access, or cached hierarchy discovery. Runtime scene-wide discovery is not a fallback for unclear ownership; Editor-only inspection may use it with explicit scope.
- `AFCC-EAR-001`: keep movable Editor asset and folder selections relocatable through a serialized reference, GUID-backed lookup, or evidenced project finder. Validate missing and ambiguous results instead of silently binding the first arbitrary match.

### Concrete ownership and interfaces

Apply `AFCC-INT-001` progressively to new or deliberately revised contracts:

- Start with the concrete owner and the smallest direct, serialized, or injected dependency that preserves one-way ownership.
- Reject a new interface when its only evidence is one implementation, a hypothetical future implementation, dependency-injection registration, a convenient test double, or a naming convention.
- Accept an interface when an installed or external owner requires that contract, at least two active production implementations are interchangeable, platform or runtime variants share one consumer contract, or an unavoidable cross-assembly boundary needs a small implementation-free contract.
- Keep accepted interfaces consumer-oriented and read-only where possible. State-changing operations remain on an explicit owner API or command.
- Resolve and cache the selected dependency at the ownership boundary. Do not repeatedly query a service locator or discover an interface in a runtime hot path.
- Do not migrate an existing interface as incidental cleanup. Do not substitute an abstract base unless the implementations actually share state, behavior, or inheritance semantics.

Testing convenience does not independently justify an interface. A test seam qualifies only when the same boundary is a real production adapter or owner contract, such as a platform implementation or an external nondeterministic dependency with explicit ownership.

### Tree-oriented ownership and package boundaries

Apply `AFCC-TRE-001`, `AFCC-PKG-001`, `AFCC-PCR-001`, `AFCC-PRT-001`, `AFCC-BND-001`, `AFCC-ANI-001`, and `AFCC-PKG-002` together when a user asks for the corresponding architecture or package boundaries:

- Draw an ownership tree first: composition root, feature or service node, child owners, and each node's state and lifetime owner. Then record shared dependencies as additional directed edges. The result is a tree-oriented DAG, not a promise that every runtime reference has exactly one parent.
- Reject cycles. A lower node never reaches back into its composition root or a sibling implementation. Report upward through an existing callback, event, result, or a separately evidenced consumer contract.
- Keep composition roots project-owned. They select concrete project adapters, scene objects, SDK implementations, save keys, environment settings, and package-neutral defaults.
- A project-owned composition layer may physically live in one product-owned, non-reusable package. Opt in only when the package root `AI_GUIDE.md` contains the exact complete trimmed markers `AI Product Composition Root: <package-id>` and `AI Refactor target: package-oriented-product` inside `## Package Identity`, and the actual root ID matches the sibling `package.json` `name`. The pair selects only this product-composition target; it does not select `actionfit-unity` or make the package reusable.
- After normal embedded-before-PackageCache resolution, accept at most one declared product root. Treat an absent declaration as the normal generic architecture target. Report an incomplete pair, duplicate declaration, package-ID mismatch, declaration outside `Package Identity`, or unsupported target as missing evidence or a structural diagnostic; never infer intent from installation, dependency names, repository identity, folders, or source style.
- A package candidate owns one coherent rule/state/lifecycle unit. It can depend on lower reusable packages, but it cannot reference a consuming-project assembly, scene, prefab, project ScriptableObject, concrete SDK, save key, or asset identifier.
- Split a reusable node into engine, UI, and adapter packages only when concrete evidence shows distinct reuse, replacement, compilation, platform, or ownership boundaries. A three-package shape is an available decomposition, not a quota.
- Add a port only for a capability the package actually consumes and cannot own. Keep the port narrow and consumer-oriented, bind it once at the composition root, and cache the selected adapter at the ownership boundary.
- A safe neutral default is allowed only when it preserves the declared semantics. Silent success, fabricated data, or a no-op that hides a required capability is not a neutral default.
- Do not introduce a dependency-injection container, service locator, global registry, generic base node, or one-interface-per-class pattern to make the diagram appear uniform.

The product package may own concrete product bindings, dependency selection, and migration targets. Reusable dependencies still obey `AFCC-PKG-001`; project safety, workflow, current-state, compatibility, and migration facts remain local until another explicit owner can preserve them. A declaration does not authorize package creation, code or asset migration, project-document deletion, publication, or deployment.

For new or deliberately revised scene presentation, the `MonoBehaviour` is a thin binder and sole owner of serialized `Refs`, `Assets`, and `Settings`. It initializes and explicitly calls a plain C# feature owner instead of containing reusable state transitions. The binder may own Unity lifecycle and subscriptions, but children do not reach back into the binder and the binder does not locate project services through scene-wide discovery or a service locator.

Keep reusable animation helpers non-serialized. Their entry points receive the exact targets, settings, and cancellation/lifetime context from the binder. They may retain only runtime handles they create and clean up. Apply `AFCC-TWN-001` as an additional capability rule when DOTween is evidenced.

Use dependency-specific Leaf packages only where the axis can compile, test, version, and evolve independently. Origin/Core points inward to no optional UI, DOTween, SDK, or project assembly. Unity Binding, UI Foundation Binding, DOTween Animation, SDK Adapter, and Installer packages may depend inward on lower nodes. A default bundle may install all supported leaves while direct consumers choose a smaller declared closure. Do not turn this list into a package-count quota.

Example target view:

```text
Project Composition Root
├── Feature A package
│   └── Shared service package
├── Feature B package
│   └── Shared service package
└── Project adapters
    ├── SDK adapter -> narrow package port
    └── Scene adapter -> narrow package port
```

The repeated shared-service line represents two incoming consumer edges to one owned service node. It does not authorize duplicate service instances or a dependency cycle. Record the selected lifetime and instancing decision separately.

### Async, duration, and periodic work

When UniTask evidence exists:

- use UniTask for new delayed, condition-wait, and periodic work;
- retain `IEnumerator` only for an API that requires it;
- propagate cancellation and pair an owned source with destroy, disable, close, pool return, or shutdown as appropriate;
- use `UniTask.WaitUntil` for condition waits instead of a hand-written polling loop;
- observe cancellation and non-cancellation failures;
- do not convert an unrelated existing coroutine as incidental cleanup.

`AFCC-DUR-001` uses `float` seconds for gameplay durations. Convert at an API boundary when an external method requires another unit.

When an evidenced project loop owner exists, `AFCC-LOP-001` selects the phase whose documented semantics match the work and pairs registration with the same active lifetime. Do not guess concrete event names from another project.

### Serialized fields and owner-routed UI

`AFCC-RFS-001` is deprecated. Existing mixed public `refs` fields may remain until an explicitly approved serialization migration, but new or deliberately revised inputs use `AFCC-RFS-002` and `AFCC-SER-004`.

Use three role-specific containers:

- `Refs`: `Component` references found on the owner GameObject or any descendant, including inactive descendants. Prefer the relevant Component or `Transform` instead of storing a hierarchy GameObject.
- `Assets`: persistent external Unity asset references, including sprites, materials, audio clips, ScriptableObjects, and prefab assets. Do not store Addressables handles, runtime instances, or scene objects here.
- `Settings`: numeric and other non-reference Inspector-authored values such as booleans, enums, colors, and vectors. Do not store runtime state, mutable collections, save DTOs, or persistence schemas here.

Use private serialized backing fields and getter-only public access:

```csharp
[Serializable]
public sealed class Refs
{
    [SerializeField] private Component icon;

    public Component Icon => icon;
}

[Serializable]
public sealed class Assets
{
    [SerializeField] private Sprite iconSprite;

    public Sprite IconSprite => iconSprite;
}

[Serializable]
public sealed class Settings
{
    [SerializeField] private float animationDurationSeconds = 0.25f;

    public float AnimationDurationSeconds => animationDurationSeconds;
}

[SerializeField] private Refs refs = new();
[SerializeField] private Assets assets = new();
[SerializeField] private Settings settings = new();

public Refs References => refs;
public Assets AssetReferences => assets;
public Settings Configuration => settings;
```

Do not add setters or runtime mutation methods. The serialized inputs may be established by declaration defaults, Unity deserialization, or Editor-only authoring before Play Mode. Once runtime begins, do not replace the containers or assign their fields. Copy any value that must change into a separately owned runtime model. Returning a Component or asset does not freeze that referenced object's internal state; only the stored reference identity remains fixed.

`com.actionfit.referencebinding` is a required dependency of this package rather than an optional capability gate. Use `RequiredReference` on mandatory `Refs` fields and add `AutoWireChild` only when the Component type plus exact root-or-descendant GameObject name defines one unique hierarchy candidate. `Assets` may use `RequiredReference` for mandatory references but never `AutoWireChild`; ReferenceBinding does not search the AssetDatabase or prove that a reference is persistent. Wrap the owner MonoBehaviour's complete `OnValidate` declaration and `ReferenceBindingRequests.Enqueue(this)` call in `#if UNITY_EDITOR`. A custom consuming asmdef must explicitly reference `com.actionfit.referencebinding`; package installation does not rewrite asmdefs. Editor-only attributes and tools may author private fields before Play Mode, but the installed owner must reject Player and Play-Mode mutation paths.

A standalone serialized field remains valid when a container would obscure ownership. Resolve concrete component wrappers and reference-binding shapes through `references/owner-routing.md` rather than copying types from another consuming project. Moving an existing field between containers changes its serialized property path, so apply the new shape progressively and use the approved serialization migration contract for existing assets.

For ScriptableObject ownership, apply `AFCC-STA-001` before `AFCC-SOS-001`. A singleton is appropriate only for one globally referenced configuration or catalog instance; multiple variants and mutable session state keep their existing explicit owner. Resolve the concrete singleton base, Resources path, cache, and creation menu through `references/owner-routing.md`.

For an explicitly approved serialized rename, `AFCC-SER-003` is the package-owned targeted procedure: prove text serialization, search the exhaustive old-key scope, replace only the matching key, preserve values and object references, inspect the targeted diff, and validate asset reload. If any evidence is unavailable, use `AFCC-SER-002` or stop. The procedure does not authorize a rename or broad YAML rewrite.

### DOTween ownership

When DOTween evidence exists:

| Use case | Pattern | Ownership check |
| --- | --- | --- |
| Fixed repeated animation | create once with `SetAutoKill(false)`, pause, then `Restart` | final owner kills at its terminal lifetime |
| Variable animation | assign a private unique object ID and use `DOTween.Kill(id)` | kill only the caller-owned ID |
| Natural one-shot | do not retain the tween field | no later field kill exists |
| Infinite paused/resumed loop | retain and pause/resume | it never returns to the completed pool before cleanup |

An auto-killed field and `IsActive()` do not prove ownership. Target-wide kill is valid only when one system owns every tween on that target. Shared targets use per-system IDs.

## Minimum Validation

- Confirm the exact selector and list every activated or inactive capability rule.
- Inspect the touched file's existing style before applying organization or comment rules.
- Compile the affected assembly after async, conditional compilation, owner API, or optional-library changes.
- Exercise success, cancellation, repeated enable/disable, and disposal for lifetime-sensitive work.
- For serialized changes, inspect every targeted asset diff and verify reload without value loss.
- For DOTween changes, exercise replay, disable/destroy cleanup, and another animation sharing the same target.
- For a new interface, identify the qualifying production evidence and inspect its implementations and consumers; confirm that an existing interface was not migrated without separate authority.
- For a package-tree proposal, identify each node owner, all dependency edges and cycles, project-only coupling, the production evidence for each port, and why each package split is coherent rather than merely smaller.
- For a product-root proposal, verify the exact marker pair in `Package Identity`, the sibling manifest name, unique resolved ownership, separate profile selector, and the absence of an inferred or duplicated local declaration.
- For a binder boundary, verify that serialized scene inputs have one owner, plain logic has no Unity serialization dependency, and animation entry points receive their targets explicitly.
- For Leaf packages, compile Origin/Core without optional integration assemblies and compile each leaf against only its declared inward dependencies.
- Run a negative check showing that absent capabilities did not gain dependencies, symbols, or unavailable API calls.
