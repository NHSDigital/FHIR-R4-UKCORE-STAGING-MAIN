## `{{page-title}}`

This element has an open slice, differentiated by the value of `Observation.category.coding.code`, and MAY be used to differentiate the specific laboratory's speciality. There is one defined mandatory slice `Observation.category:laboratory`, with a fixed value, which SHALL be populated when this profile is used, and additional category code's can be populated.

### `Observation.category:laboratory`
The following SHALL be used:
- `Observation.category.coding.system` = `http://terminology.hl7.org/CodeSystem/observation-category`
- `Observation.category.coding.code` = `laboratory`
- `Observation.category.coding.display` = `Laboratory`

---