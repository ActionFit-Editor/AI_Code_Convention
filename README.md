# AI Code Convention (com.actionfit.ai-codeconvention)

Portable Unity code-authoring guidance for Codex and Claude. The package combines a portable core with explicitly selected profiles, routes concrete APIs to their installed owners, and applies effective rules only inside a user-authorized code change.

This package remains a **Private** guidance package. It contains no Runtime assembly, EventBus implementation, gameplay framework, analyzer, formatter, or code generator.

## Install

```json
{
  "dependencies": {
    "com.actionfit.ai-codeconvention": "https://github.com/ActionFitGames/AI_Code_Convention.git#0.2.0"
  }
}
```

## Unity Menu

- README: `Tools > Package > AI Code Convention > README`.
- If this package later owns or bootstraps a settings ScriptableObject, add `Setting SO` under the same package root.

## AI Guide

- Read `AI_GUIDE.md` before modifying or diagnosing this package in a consuming project.
- `portable-core` is the default profile. A consuming project's primary router may opt in with the exact selector `AI Code Convention profile: actionfit-unity`.
- Never infer a profile from a repository name, organization, installed dependency, or folder layout.
- Project-local safety and factual architecture remain authoritative context, and an installed package/API owner remains factual truth for its concrete surface.
- Detailed architecture and validation guidance is installed progressively with the related Agent Skills.

The selected package profile can be the sole code-convention authority. A consuming project does not need a separate local convention document when its router selects the profile and its architecture documents contain only factual project mappings.

## Agent Skills

Custom Package Manager `1.1.84` or newer installs the schema v2 skills into project-local agent folders while preserving modified or conflicting targets.

- `$code-convention-help`: explains the selected profile, effective rule identifiers, owner routes, skills, and safety boundaries without changing state.
- `$code-convention-check`: compares documented contracts, reports the effective profile-aware rule and local-convention retirement readiness, and proves the check did not change files.
- `$code-convention-apply`: resolves the selected profile and installed API owners, then applies the effective conventions only after the user authorizes a concrete Unity code change.

The comparison skill reports `Aligned`, `Local Extension`, `Conflict — Local Wins`, `Package Default`, `Local Only`, and `Package/API Mismatch`. Retirement readiness is a separate result, not a seventh relationship category. The check is a document-level convention audit, not a source-wide compliance scanner.

## Assembly

- **Editor** (`com.actionfit.ai-codeconvention.Editor`): editor-only package assembly.

## Safety

- Serialized-reference work is routed to the installed `com.actionfit.referencebinding/AI_GUIDE.md`; this package does not reproduce its APIs or add asset-writing modes.
- Package publication, repository creation, tags, and catalog registration are separate manual operations.
- Public redistribution requires a separate ownership and distribution-rights review.
