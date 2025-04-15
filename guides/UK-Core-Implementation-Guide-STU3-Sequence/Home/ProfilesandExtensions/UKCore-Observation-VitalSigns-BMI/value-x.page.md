## `{{page-title}}`

The cardinality of this element is 1..1, and SHALL be present.

For Adult BMI measurements, a <code>valueQuantity</code> SHALL be present, and the following used for this profile:
- `Observation.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.valueQuantity.code` = `kg/m2`
- `Observation.valueQuantity.unit` = `kilogram / (meter ^ 2)`

For Child BMI measurements, a <code>valueQuantity</code> SHALL be present, and the following used for this profile:
- `Observation.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.valueQuantity.code` = `{percentile}`
- `Observation.valueQuantity.unit` = `Percentile`

---