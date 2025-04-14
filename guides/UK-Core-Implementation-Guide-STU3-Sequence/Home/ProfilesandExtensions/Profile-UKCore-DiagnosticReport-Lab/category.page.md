## `{{page-title}}`

This element has an open slice, differentiated by the value of `DiagnosticReport.category.coding.code`, and MAY be used to differentiate the specific laboratory's speciality. There is one defined mandatory slice `DiagnosticReport.category:laboratory`, with a fixed value, which SHALL be populated when this profile is used, and additional category code's can be populated.

### `DiagnosticReport.category:laboratory`
The following SHALL be used for this profile:
- `DiagnosticReport.category.coding.system` = `http://terminology.hl7.org/CodeSystem/v2-0074`
- `DiagnosticReport.category.coding.code` = `LAB`
- `DiagnosticReport.category.coding.display` = `Laboratory`.

---