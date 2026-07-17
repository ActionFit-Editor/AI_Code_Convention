# AI Code Convention (com.actionfit.ai-codeconvention)

Portable Unity code-authoring guidance for Codex and Claude. The package combines a portable core with explicitly selected profiles, routes concrete APIs to their installed owners, applies effective rules only inside a user-authorized code change, and provides one opt-in ActionFit MonoBehaviour starter template with required ReferenceBinding support.

This package is distributed from a **Public** repository. It contains no Runtime assembly, EventBus implementation, gameplay framework, analyzer, formatter, or general-purpose code-generation framework. Its Editor-only generator creates one new convention starter script through Unity's native Project window flow. Public visibility makes the source readable but does not embed credentials or grant rights beyond the repository's explicit license terms.

## Install

```json
{
  "dependencies": {
    "com.actionfit.custompackagemanager": "https://github.com/ActionFit-Editor/Custom_Package_Manager.git#1.1.100",
    "com.actionfit.referencebinding": "https://github.com/ActionFit-Editor/ReferenceBinding.git#0.1.2",
    "com.actionfit.ai-codeconvention": "https://github.com/ActionFit-Editor/AI_Code_Convention.git#0.4.4"
  }
}
```

Custom Package Manager resolves the two declared ActionFit dependencies when installing from its catalog. Direct Git UPM consumers must keep the three root-manifest entries above because Unity does not resolve transitive Git URLs from a package's semantic-version dependency entries.

## Unity Menu

- Convention MonoBehaviour: `Assets > Create > Scripting > ActionFit Convention MonoBehaviour Script`.
- README: `Tools > Package > AI Code Convention > README`.
- If this package later owns or bootstraps a settings ScriptableObject, add `Setting SO` under the same package root.

The convention template creates a new `MonoBehaviour` with example `Refs`, `Assets`, and `Settings` containers, private serialized backing fields, and getter-only access. Its `Refs.contentRoot` example uses `RequiredReference` plus exact-name `AutoWireChild`, its `Assets.iconSprite` example uses `RequiredReference` without hierarchy wiring, and the complete `OnValidate` declaration is Editor-guarded before it queues the owner through `ReferenceBindingRequests`. Unity owns the selected destination, rename interaction, `#SCRIPTNAME#` replacement, and root-namespace expansion.

`com.actionfit.referencebinding@0.1.2` is a required dependency. The generated script compiles in Unity's predefined assemblies because the owner Runtime assembly is auto-referenced. A consuming custom asmdef must explicitly reference `com.actionfit.referencebinding`; the generator does not mutate project asmdefs. Invoking the menu does not select a profile, modify an existing script, save a Scene or Prefab, or prove that later edits remain compliant.

## AI Guide

- Read `AI_GUIDE.md` before modifying or diagnosing this package in a consuming project.
- `portable-core` is the default profile. A consuming project's primary router may opt in with the exact selector `AI Code Convention profile: actionfit-unity`.
- Never infer a profile from a repository name, organization, installed dependency, or folder layout.
- Project-local safety and factual architecture remain authoritative context, and an installed package/API owner remains factual truth for its concrete surface.
- The `actionfit-unity` profile separates Inspector-authored inputs into `Refs`, `Assets`, and `Settings`, exposes them through getter-only APIs, and keeps their stored values or reference identities unchanged during runtime.
- The `actionfit-unity` profile prefers concrete ownership and permits a new interface only for an evidenced external contract, interchangeable production implementations, platform or runtime variants, or an unavoidable implementation-free assembly boundary. Existing interfaces are not automatic migration targets.
- The `actionfit-unity` profile targets a tree-oriented ownership view whose concrete dependency graph is an acyclic DAG: composition roots assemble coherent feature or service nodes, reusable nodes can become project-neutral packages, and only evidenced external capabilities become narrow ports bound to project adapters at a composition root.
- The `actionfit-unity` profile may keep concrete product composition in one product-owned, non-reusable package when its root `AI_GUIDE.md` explicitly declares `AI Product Composition Root: <package-id>` and `AI Refactor target: package-oriented-product` inside `## Package Identity`. These markers select only the product-composition target; they never select the code-convention profile or create migration authority.
- New or deliberately revised scene code keeps `MonoBehaviour` classes as thin serialized binders, plain C# owners as the reusable logic boundary, and non-serialized animation helpers that receive exact targets and lifetime inputs from the binder.
- Optional integration axes may become inward-dependent Leaf packages—Origin/Core, Unity Binding, UI Foundation Binding, DOTween Animation, SDK Adapter, and Installer—when each boundary can compile, test, version, and evolve coherently. A default installer may select the full set without forcing direct consumers to import every leaf.
- The target is progressive. Package count, strict tree-shaped runtime references, speculative interfaces, dependency-injection containers, and whole-project remodeling are not goals.
- Detailed architecture and validation guidance is installed progressively with the related Agent Skills.

The selected package profile can be the sole code-convention authority. A consuming project does not need a separate local convention document when its router selects the profile, an explicitly declared product package owns any package-oriented composition target, and its remaining architecture documents contain only factual project mappings.

## Agent Skills

Custom Package Manager `1.1.100` or newer installs the schema v2 skills into project-local agent folders while preserving modified or conflicting targets.

- `$code-convention-help`: explains the selected profile, effective rule identifiers, owner routes, skills, and safety boundaries without changing state.
- `$code-convention-check`: compares documented contracts, reports the effective profile-aware rule and local-convention retirement readiness, and proves the check did not change files.
- `$code-convention-apply`: resolves the selected profile and installed API owners, then applies the effective conventions only after the user authorizes a concrete Unity code change.

The comparison skill reports `Aligned`, `Local Extension`, `Conflict — Local Wins`, `Package Default`, `Local Only`, and `Package/API Mismatch`. Retirement readiness is a separate result, not a seventh relationship category. The check is a document-level convention audit, not a source-wide compliance scanner.

## Assembly

- **Editor** (`com.actionfit.ai-codeconvention.Editor`): editor-only package assembly.

## Safety

- Serialized-reference behavior is routed to the required `com.actionfit.referencebinding/AI_GUIDE.md`; this package consumes its documented public attributes and owner queue without reproducing its APIs or adding asset-writing modes.
- Package publication, repository creation, tags, and catalog registration are separate manual operations.
- Public distribution has been authorized for this package. Tokens, credentials, and private configuration remain prohibited from package content regardless of repository visibility.
