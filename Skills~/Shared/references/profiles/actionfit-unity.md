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

- `AFCC-CPP-001`: keep the method declaration stable and place symbol-specific behavior inside the body. Conditional imports and declarations requiring an unavailable base type remain valid exceptions.
- `AFCC-PRF-001`: prefer existing serialized/injected references, owner access, or cached hierarchy discovery. Runtime scene-wide discovery is not a fallback for unclear ownership; Editor-only inspection may use it with explicit scope.
- `AFCC-EAR-001`: keep movable Editor asset and folder selections relocatable through a serialized reference, GUID-backed lookup, or evidenced project finder. Validate missing and ambiguous results instead of silently binding the first arbitrary match.

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

`AFCC-RFS-001` uses this shape for Inspector-connected references and closely related presentation settings:

```csharp
[Serializable]
public class Refs
{
    public Component icon; // 아이콘 표시 컴포넌트
    public Color activeColor = Color.white; // 활성 색상
}

public Refs refs;
```

Do not add `Tooltip`. A standalone serialized field is valid when a container would obscure ownership. Resolve concrete component wrappers and reference-binding shapes through `references/owner-routing.md` rather than copying types from another consuming project.

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
- Run a negative check showing that absent capabilities did not gain dependencies, symbols, or unavailable API calls.
