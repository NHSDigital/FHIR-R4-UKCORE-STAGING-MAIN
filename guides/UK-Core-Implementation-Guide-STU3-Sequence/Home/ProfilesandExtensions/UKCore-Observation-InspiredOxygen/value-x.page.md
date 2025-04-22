## `{{page-title}}`

A <code>valueQuantity</code> with the following values SHOULD be used for this profile if the <code>Observation.code</code> value is 371825009 | Patient on oxygen.

One of the following values SHOULD be used:

### Litres per minute

- `Observation.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.valueQuantity.code` = `l/min`
- `Observation.valueQuantity.unit` = `litre per minute`

### Percentage of oxygen being delivered / Fraction of inspired oxygen (FiO2)

- `Observation.valueQuantity.system` = `http://unitsofmeasure.org`
- `Observation.valueQuantity.code` = `%`
- `Observation.valueQuantity.unit` = `percent`

---