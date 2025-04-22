---
topic: Observation-VitalSigns-BloodPressure-Component
---
## `{{page-title}}`

This element has a closed slice on `Observation.component`, discriminated by the value of `Observation.component.code.text`. This closed slice allows Systolic and Diastolic measurements to be populated. 

<br>

The following values SHALL be used:

`Observation.component:SystolicBP` slice, discriminated by a `Observation.component.code.text` value of `Systolic blood pressure`, SHALL be used to record a systolic blood pressure measurement, which SHALL have a LOINC "magic code", and SHALL have a SNOMED CT concept used to record the type of systolic blood pressure measurement.

### `Observation.component:SystolicBP.code.text`
The following SHALL be used for this profile:
- `Observation.component.code.text` = `Systolic blood pressure`

### `Observation.component:SystolicBP.code.coding:loinc`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://loinc.org`
- `Observation.component.code.coding.code` = `8480-6`
- `Observation.component.code.coding.display` = `Systolic blood pressure`

### `Observation.component:SystolicBP.code.coding:snomedCT`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://snomed.info/sct`
- `Observation.component.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure-Systolic}}
- `Observation.component.code.coding.display` = The “preferred term” associated with the SNOMED CT concept, representing a systolic blood pressure measurement

### `Observation.component:SystolicBP.value[x]`
The following SHALL be a Quantity, and the following used for this profile:
- `Observation.component.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.component.valueQuantityg.code` = `mm[Hg]`
- `Observation.component.valueQuantity.unit` = `millimeter of mercury`

<br>

`Observation.component:DiastolicBP` slice, discriminated by a `Observation.component.code.text` value of `Diastolic blood pressure`, SHOULD be used to also record a diastolic blood pressure measurement where present, which SHALL have a LOINC "magic code", and SHALL have a SNOMED CT concept used to record the type of diastolic blood pressure measurement if used.

### `Observation.component:DiastolicBP.code.text`
The following SHALL be used for this profile:
- `Observation.component.code.text` = `Diastolic blood pressure`

### `Observation.component:DiastolicBP.code.coding:loinc`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://loinc.org`
- `Observation.component.code.coding.code` = `8462-4`
- `Observation.component.code.coding.display` = `Diastolic blood pressure`

### `Observation.component:DiastolicBP.code.coding:snomedCT`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://snomed.info/sct`
- `Observation.component.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure-Diastolic}}
- `Observation.component.code.coding.display` = The “preferred term” associated with the SNOMED CT concept, representing a diastolic blood pressure measurement

### `Observation.component:DiastolicBP.value[x]`
The following SHALL be a Quantity, and the following used for this profile:
- `Observation.component.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.component.valueQuantity.code` = `mm[Hg]`
- `Observation.component.valueQuantity.unit` = `millimeter of mercury`

---