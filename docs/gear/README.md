# EZlay Gear reference data

This feed supplies the Gear preview in EZlay. The application remains closed source and free. Reference data is versioned independently of Windows installers.

## Current coverage

Revision 1 contains 58 gear-stat definitions: IDs, English display names, numeric scaling and mapping confidence. It contains **zero benchmark or reroll rules**. It cannot supply class grades, maximum-roll comparisons, reroll probabilities or expected costs yet. The application labels unsupported equipment as reference needed and keeps user-entered personal targets separate.

The metadata comes from the AionDPS project's gear-stat table, not its species-knowledge table. Four base-attribute mappings retain the source's inferred status. The upstream attribution is included in AionDPS-LICENSE.txt.

## Feed

- `manifest.json` identifies the approved current reference, its SHA-256 checksum and ECDSA signature.
- `r1/gear-reference-r1.json` is the immutable revision 1 bundle.
- Trusted clients verify the bundle with the publisher key shipped with the app. The private signing key is not published or stored in the collection workflow.

The scheduled Gear reference review workflow checks the public stat source daily and stages changed metadata as an unsigned review artifact. It does not publish new scores, replace approved reference data, or refresh a date merely to make old data appear new. Reviewed releases are validated and signed by the maintainer before the manifest is changed.

## Adding benchmark coverage

Every rule requires an exact item and class, Global patch context, traceable source, supported line count, legal stat/skill pool, verified raw-unit caps and scoring weights. A rule's option pool must permit any distinct set of the stated line count; configurations with extra exclusive groups or item-specific restrictions need explicit engine support before publication. Regular reroll advice is disabled for Arcana.

Missing information stays unavailable. Korea-only observations must not be relabelled as Global benchmarks. Do not infer success odds, prices, maximum rolls or class weights from a few character snapshots.

Reference data is advisory. A score is not combat power or a measured DPS increase.
