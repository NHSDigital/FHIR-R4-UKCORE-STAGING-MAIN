## `{{page-title}}`

`Observation.code` SHALL be present and the following values SHALL be used:

### `Observation.code.coding`
The following SHALL be present and SHALL be used for this profile:
- `Observation.code.coding.system` = `http://snomed.info/sct`
- `Observation.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure-Average}}
- `Observation.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

---