# EZlay automatic Gear reference

Revision 2 covers 3,085 Global items and 17,120 class/item rules across eight classes, with 58 stat mappings. Identical pools are shared to keep the download around 6.3 MB.

The app automatically scores received equipment and suggests legal best-roll replacements. Personal targets have been removed. Scores follow the active character and class. This feature is in the local Gear review build; the public installer is unchanged until an app release is approved.

## Model and provenance

Global roll caps, distinct stat/skill pools, line counts and skill limits were exported locally from Item.dat and ItemEquipSubstatSkill.dat in the installed Global client on November 17, 2026. This is a static client snapshot, not live server verification. The extraction report retains SHA-256 hashes. Raw tables, client keys, character data and app source are not published.

Class/slot weights are public CielUI ranked PvE usage counts divided by the slot sample, retrieved November 17. These are KOREA observations, separately labelled. They are popularity weights, not DPS coefficients. Only the public top lines are available: unlisted lines get zero model weight, which does not establish that they are useless. Global balance, character caps and PvP may differ.

Score = 100 times weighted current rolls divided by the legal ideal for the SAME ITEM. Each line contributes weight times current raw value divided by that item's cap. Skill limits are respected. A score of 100 means ideal rolls on that item; it does not mean best equipment across levels. These are EZlay scores, not Kisk's slot-wide scores or letter grades. Kisk's published methodology helped explain the approach: https://kisk.app/scoring .

Arcana, two unmapped bracelet pools, unknown or incomplete lines, duplicate lines and rolls above snapshot caps remain unscored. Arcana never receives normal reroll advice. Upgrade cards show best-roll score gains, without odds, cost estimates or promised DPS gains.

## Updates and privacy

Manifest: https://kinwan96.github.io/ezlay/gear/manifest.json . Immutable bundle: r2/gear-reference-r2.json . Clients check approved data daily, verify SHA-256 and ECDSA signatures, and retain a rollback copy.

The daily workflow collects eight public class aggregates, stages changed priorities for maintainer review, and retains the original Global cap observation date. It does not sign or publish automatically. Client caps must be re-exported from a newer installed Global patch, checked, and signed by the maintainer. No character uploads or signing key are used in this workflow.

Stat ID mappings originate in the bundled AionDPS gear mapping; four base attribute mappings retain inferred confidence. Attribution is included in AionDPS-LICENSE.txt. Game data and assets belong to NCSOFT.
