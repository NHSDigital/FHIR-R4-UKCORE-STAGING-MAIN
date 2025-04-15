## `{{page-title}}`

This element has an open slice on `Observation.code.coding`, discriminated by the value of `Observation.code.coding.system`.

All Vital Signs observations SHALL consist of two `Observation.code.coding` elements, and one SHALL contain a LOINC "magic code" for the type of vital sign observation, and one SHALL be used to send a SNOMED CT concept for the type of observation.

### `Observation.code.coding:loinc`
The following SHALL be used for this profile:
- `Observation.code.coding.system` = `http://loinc.org`
- `Observation.code.coding.code` = A LOINC "magic code" from http://hl7.org/fhir/ValueSet/observation-vitalsignresult
- `Observation.code.coding.display` = The display value for the LOINC code

### `Observation.code.coding:snomedCT`
The following SHALL be used for this profile:
- `Observation.code.coding.system` = `http://snomed.info/sct`
- `Observation.code.coding.code` = A SNOMED CT concept Id from https://fhir.hl7.org.uk/ValueSet/UKCore-ObservationVitalSignsType
- `Observation.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

---