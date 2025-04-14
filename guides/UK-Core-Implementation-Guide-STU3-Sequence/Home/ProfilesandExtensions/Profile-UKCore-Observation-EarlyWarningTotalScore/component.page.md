## `{{page-title}}`

This element SHOULD be used to record the component sub scores used to determine the total score

The following values SHALL be used:

### `Observation.component.code.coding`
The following SHALL be used for this profile:
- `Observation.component.code.coding.system` = `http://snomed.info/sct`
- `Observation.component.code.coding.code` = A SNOMED CT concept Id from {{pagelink:ValueSet-UKCore-EarlyWarningSubScore}}
- `Observation.component.code.coding.display` = The “preferred term” associated with the SNOMED CT concept

### `Observation.component.value[x]`
The following SHALL be a Quantity, and the following used for this profile:
- `Observation.component.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.component.valueQuantityg.code` = `{ScoreOf}`

---