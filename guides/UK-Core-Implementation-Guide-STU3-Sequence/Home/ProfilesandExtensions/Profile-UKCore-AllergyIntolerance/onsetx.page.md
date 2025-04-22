## `onset[x]`

Record of the date and/or time of the onset of the reaction caused by the allergy or intolerance which can be recorded in one of five ways;
- `onsetDateTime`
- `onsetAge`
- `onsetPeriod`
- `onsetRange`
- `onsetString`.

<h3 id="providersystems-allergyintolerance-onset">Provider Systems</h3>

Provider systems are recommended to support at least `AllergyIntolerance.onsetDateTime` and `AllergyIntolerance.onsetAge` where this date is available.

It is recommended **not** to record the onset using an `AllergyIntolerance.onsetPeriod` or `AllergyIntolerance.onsetRange` as these data types are complex and less useful. If the exact onset date is not known, but was between two known dates, e.g. 2018 and 2019, then use the lower/older date as the `AllergyIntolerance.onsetDateTime` instead of using an `AllergyIntolerance.onsetPeriod`.

It is recommended **not** to record the onset using an `AllergyIntolerance.onsetString` as this data will not be machine processable.

<h3 id="consumersystems-allergyintolerance-onset">Provider Systems</h3>

Consumer systems SHALL be able to handle any of the `AllergyIntolerance.onset` data types.

---
