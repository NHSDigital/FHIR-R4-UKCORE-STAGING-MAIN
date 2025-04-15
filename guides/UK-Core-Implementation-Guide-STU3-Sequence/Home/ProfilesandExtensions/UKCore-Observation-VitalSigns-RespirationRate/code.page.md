## `{{page-title}}`

The following values SHALL be used:

### `Observation.code.coding:loinc`
The following SHALL be used for this profile:
- `Observation.code.coding.system` = `http://loinc.org`
- `Observation.code.coding.code` = `9279-1`
- `Observation.code.coding.display` = `Respiratory Rate`

### `Observation.code.coding:snomedCT`
The following SHALL be used for this profile:
- `Observation.code.coding.system` = `http://snomed.info/sct`
- `Observation.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-RespirationRate}}
- `Observation.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

---