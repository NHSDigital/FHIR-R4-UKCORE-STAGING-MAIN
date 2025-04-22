## `{{page-title}}`

`Observation.code` SHALL be present and the following values SHALL be used to represent a set of blood pressure results:

### `Observation.code.coding:loinc`
The following SHALL be present and SHALL be used for this profile:
- `Observation.code.coding.system` = `http://loinc.org`
- `Observation.code.coding.code` = `85354-9`
- `Observation.code.coding.display` = `Blood pressure panel with all children optional`

### `Observation.code.coding:snomedCT`
The following SHALL be present and SHALL be used for this profile:
- `Observation.code.coding.system` = `http://snomed.info/sct`
- `Observation.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure}}
- `Observation.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

The SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure}} should represent the set of blood pressure reading and SHALL NOT be a systolic or diastolic reading concept, and SHALL NOT be an average or mean concept.

---