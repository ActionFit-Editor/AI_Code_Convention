# AI Code Convention (com.actionfit.ai-codeconvention)

Portable, local-first Unity code-authoring guidance for Codex and Claude. The package compares project conventions with reusable defaults and applies the effective rules only inside a user-authorized code change.

This first draft is a **Private** guidance package. It contains no Runtime assembly, EventBus implementation, gameplay framework, analyzer, formatter, or code generator.

## Install

```json
{
  "dependencies": {
    "com.actionfit.ai-codeconvention": "https://github.com/ActionFit-Editor/AI_Code_Convention.git#0.1.0"
  }
}
```

## Unity Menu

- README: `Tools > Package > AI Code Convention > README`.
- If this package later owns or bootstraps a settings ScriptableObject, add `Setting SO` under the same package root.

## AI Guide

- Read `AI_GUIDE.md` before modifying or diagnosing this package in a consuming project.
- Project-local instructions and package/API-specific guides override this package's generic defaults.
- Detailed architecture and validation guidance is installed progressively with the related Agent Skills.

## Agent Skills

Custom Package Manager `1.1.84` or newer installs the schema v2 skills into project-local agent folders while preserving modified or conflicting targets.

- `$code-convention-help`: explains the package, rule identifiers, skills, and safety boundaries without changing state.
- `$code-convention-check`: compares documented local conventions with package defaults and reports the effective local-first rule without changing files.
- `$code-convention-apply`: applies the effective conventions only after the user authorizes a concrete Unity code change.

The comparison skill reports `Aligned`, `Local Extension`, `Conflict — Local Wins`, `Package Default`, `Local Only`, and `Package/API Mismatch`. It is a document-level convention audit, not a source-wide compliance scanner.

## Assembly

- **Editor** (`com.actionfit.ai-codeconvention.Editor`): editor-only package assembly.

## Safety

- Serialized-reference work is routed to the installed `com.actionfit.referencebinding/AI_GUIDE.md`; this package does not reproduce its APIs or add asset-writing modes.
- Package publication, repository creation, tags, and catalog registration are separate manual operations.
- Public redistribution requires a separate ownership and distribution-rights review.
