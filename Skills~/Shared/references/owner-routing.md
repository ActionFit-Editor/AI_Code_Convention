# API Owner Routing

Use this reference before selecting any concrete package API. Project policy may choose behavior, but only the installed owner can prove that a type, member, menu, mode, or supported operation exists.

## Resolution Order

1. Resolve `Packages/<package-id>/AI_GUIDE.md` for a physical embedded package.
2. Otherwise resolve exactly one `Library/PackageCache/<package-id>@*/AI_GUIDE.md` for an installed downloaded package.
3. Read the installed `package.json` and public source only when the guide needs factual confirmation.
4. If the package is installed but the guide is absent, ambiguous, or contradicts the public surface, report missing evidence or `Package/API Mismatch` and do not invent an operation.
5. If the package is not installed, keep its capability-specific profile rule inactive.

## Owner Table

| Concern | Package trigger | Governing rule | Installed owner guide | Project boundary | Forbidden inference |
| --- | --- | --- | --- | --- | --- |
| Clock and time-zone contracts | `com.actionfit.time` | `AFCC-TIM-001` | `Packages/com.actionfit.time/AI_GUIDE.md` or matching PackageCache guide | concrete facade, saved keys, developer controls, and business calendar remain project facts | do not construct or name a clock the owner does not expose |
| UI wrappers and localization | `com.actionfit.ui.foundation` | `AFCC-UIF-001` | `Packages/com.actionfit.ui.foundation/AI_GUIDE.md` or matching PackageCache guide | game services, popup flow, art, assets, and concrete adapters remain project facts | do not invent a wrapper, registration lifecycle, settings asset, or optional animation mode |
| Serialized-reference binding | `com.actionfit.referencebinding` | `AFCC-REF-001` | `Packages/com.actionfit.referencebinding/AI_GUIDE.md` or matching PackageCache guide | a project chooses which fields opt in and owns any separately approved asset migration | do not infer bulk wiring, saving, unsupported shapes, or a public processing mode |
| Singleton ScriptableObject loading | `com.actionfit.sosingleton` | `AFCC-STA-001`, `AFCC-SOS-001` | `Packages/com.actionfit.sosingleton/AI_GUIDE.md` or matching PackageCache guide | the project decides whether data has one global asset, multiple variants, or mutable runtime ownership | do not invent a base type, Resources path, cache behavior, settings asset, or creation operation |

For the serialized-reference route, `AFCC-RFS-005` selects the installed owner's package-owned automatic `RequiredChildReference` contract for newly created or deliberately revised supported mandatory child Component fields. Deprecated `AFCC-RFS-003` `RequiredReference` plus `AutoWireChild` pairs and deprecated `AFCC-RFS-004` consumer-enqueued integrated declarations remain compatibility contracts, while external mandatory assets keep the owner-documented `RequiredReference` contract. This routing text does not redefine those APIs or authorize migration.

Third-party capabilities such as UniTask or DOTween still require installed/source evidence under `AFCC-PRO-002`. This package does not claim ownership of their APIs and does not install them.

## Reporting

For every concrete owner route, report the package ID, resolved guide path, installed version when evidenced, selected public contract, and any missing evidence. Keep project-specific type names and adapter paths in factual architecture rather than this portable routing table.
