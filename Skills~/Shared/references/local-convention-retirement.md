# Local Convention Retirement

This is a read-only readiness contract. It never edits, deletes, moves, rewrites, installs, refreshes, stages, commits, or publishes anything.

## Classification Scope

Count a document as local code-convention authority when it normatively tells code authors how to choose style, libraries, communication, lifecycle, serialization, diagnostics, or implementation patterns outside the installed package/profile/owner chain.

Do not count these as local code-convention authority:

- the exact profile selector and package route;
- repository safety, approval, workflow, branch, validation, or release rules;
- factual architecture that records current concrete types, paths, owners, keys, public surfaces, sequences, or compatibility history;
- content-specific business and persistence contracts;
- installed API-owner guides.

If a factual document also restates a general coding rule, classify only that normative wording and recommend replacing it with the governing `AFCC-*` ID while retaining the facts.

## Shadow Gates

Run these gates while retirement-candidate local documents still exist:

| Gate | Pass condition | Evidence |
| --- | --- | --- |
| Profile | exactly one valid selector, or evidenced `portable-core` default | router path and line |
| Mapping | every normative local item maps to portable core, selected profile, installed owner, factual architecture, or explicit retirement | source-backed migration rows |
| Relationships | zero unresolved `Local Only` and zero unresolved `Conflict — Local Wins` rows | six-category comparison table |
| Owners | every required concrete API owner resolves; missing optional owners leave their capability inactive | installed guide paths and versions |
| Links | every route to a retirement candidate has a concrete replacement plan | bounded reference search |
| Skill drift | package sources and managed installed Codex/Claude targets are current, with no modified, preserved, linked, unmanaged, or conflicting target | read-only manager inspection or content/hash comparison |
| No write | final Git status exactly matches the captured baseline | identical status snapshots |

Report `READY TO RETIRE` only when every shadow gate passes. Otherwise report `NOT READY`, the failing counts, sources, and the smallest follow-up. This result does not authorize deletion.

## Final Gates

After a separately authorized deletion and router update, rerun the check without assuming a local convention directory exists. Report `READY` only when all of these counts are zero:

```text
Local code-convention authority
Unmigrated rules
Unresolved Local Only
Unresolved Conflict — Local Wins
Missing owner routes
Stale convention links
Package-to-installed-skill drift
Durable changes caused by the check
```

Also report the selected profile, activated capability rules, installed owner guide paths, bounded searches used, and any missing evidence. A `READY` result proves only the documented authority and no-write contracts; it does not prove source-wide code compliance.

## Drift Rules

- Read `Skills~/manifest.json` to enumerate registered sources and targets.
- Compare package Codex and Claude `SKILL.md` sources for intended parity.
- Compare package sources with project-local managed targets without writing or refreshing them.
- Allow generated `PACKAGE_SKILLS.md` only in installed help targets; it must not exist in package sources.
- Treat a missing, modified, preserved, linked, file-backed, unmanaged, or conflicting target as drift that blocks retirement.
- Do not print credential or unrelated ignored-state contents while inspecting ownership metadata.

Retirement readiness remains a separate result. Do not add a seventh relationship category beyond the six owned by the root guide.
