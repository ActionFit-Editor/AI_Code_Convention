---
name: code-convention-apply
description: Apply the effective local-first AI Code Convention rules to a concrete Unity code change that the user has already authorized. Use only after edit authority and scope are explicit; never use a general convention request to create authority for refactors, assets, settings, workflows, publishing, or deployment.
---

# Apply Code Conventions

This skill is write-capable but does not create edit authority. If the user has not authorized a concrete Unity code change and target scope, stop before writing and ask for that scope.

1. Resolve the exact repository or worktree. Read every applicable `AGENTS.md`, `CLAUDE.md`, primary project router, directory-scoped instruction, local convention, safety rule, and validation rule before editing.
2. Capture current Git state and preserve pre-existing changes. Do not move the work into another checkout or alter branches, worktrees, or index state through this skill.
3. Read the installed `com.actionfit.ai-codeconvention/AI_GUIDE.md` and `references/unity-code-authoring-rules.md`. Read every owner package guide relevant to an API being used. For serialized references, use only the installed `com.actionfit.referencebinding/AI_GUIDE.md` contract.
4. Resolve conflicts through `AFCC-PRE-001`: project-local and API-owner rules win. Record the selected source and do not blend incompatible rules.
5. Before changing a public API, state store, event, query, command, save key/schema, asset key, asmdef, required serialized-reference rule, or resource lifetime, prepare the `AFCC-DEC-001` Decision Log. Stop for a material unresolved decision.
6. Implement only the authorized files and behavior. Preserve serialized values, GUIDs, public contracts, user changes, and existing architecture. Do not introduce a bus, global registry, framework, or migration merely because the package describes one.
7. Request separate approval before any destructive or sensitive asset, scene, prefab, ScriptableObject, ProjectSettings, serialization, migration, credential, build, release, or external-system change not already named by the user.
8. Run the smallest validation that proves the changed contract, then add compile, EditMode, PlayMode, asset, persistence, or manual QA evidence in proportion to risk. Inspect the final targeted diff and remove only traces introduced by this work.
9. Report changed files, effective rule sources, ownership/state/communication choices, the Decision Log when triggered, validation, unverified behavior, and remaining risks.

This skill does not own Jira, task selection, branch or worktree creation, commits, pushes, pull requests, package publication, repository creation, tags, catalog writes, deployment, production operations, or global/home skill installation. Use the repository's dedicated workflow and separate authorization for those operations.
