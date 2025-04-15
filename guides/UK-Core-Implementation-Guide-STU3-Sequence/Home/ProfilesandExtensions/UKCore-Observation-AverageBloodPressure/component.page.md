## `{{page-title}}`


This element has a closed slice on `Observation.component`, discriminated by the value of `Observation.component.code.text`. This closed slice allows average Systolic and Diastolic blood pressure measurements to be populated. 

<br>

The following values SHALL be used:

`Observation.component:SystolicBP` slice, discriminated by a `Observation.component.code.text` value of "Systolic blood pressure", SHALL be used to record an average systolic blood pressure measurement, which SHALL have a SNOMED CT concept used to record the type of average systolic blood pressure measurement.


### `Observation.component:SystolicBP.code.text`
The following SHALL be used for this profile:
- `Observation.component.code.text` = `Systolic blood pressure`

### `Observation.component:SystolicBP.code.coding:snomedCT`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://snomed.info/sct`
- `Observation.component.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure-AverageSystolic}}
- `Observation.component.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

### `Observation.component:SystolicBP.value[x]`
The following SHALL be a Quantity, and the following used for this profile:
- `Observation.component.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.component.valueQuantityg.code` = `mm[Hg]`
- `Observation.component.valueQuantity.unit` = `millimeter of mercury`

<br>

`Observation.component:DiastolicBP` slice, discriminated by a `Observation.component.code.text` value of "Diastolic blood pressure", SHOULD be used to also record an average diastolic blood pressure measurement, which SHALL have a SNOMED CT concept used to record the type of diastolic blood pressure measurement if used.

### `Observation.component:DiastolicBP.code.text`
The following SHALL be used for this profile:
- `Observation.component.code.text` = `Diastolic blood pressure`

### `Observation.component:DiastolicBP.code.coding:snomedCT`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://snomed.info/sct`
- `Observation.component.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-BloodPressure-AverageDiastolic}}
- `Observation.component.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

### `Observation.component:DiastolicBP.value[x]`
The following SHALL be a Quantity, and the following used for this profile:
- `Observation.component.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.component.valueQuantity.code` = `mm[Hg]`
- `Observation.component.valueQuantity.unit` = `millimeter of mercury`