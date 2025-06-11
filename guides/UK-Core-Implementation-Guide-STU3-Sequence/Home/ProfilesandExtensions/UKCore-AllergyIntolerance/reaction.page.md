## `reaction`
Details about each adverse reaction event linked to exposure to the identified substance.

The `AllergyIntolerance.reaction` is optional, but where a `AllergyIntolerance.reaction.severity` is available in the provider system it SHALL be included to convey severity even if no other reaction details are explicitly available. If this is the case the `AllergyIntolerance.reaction.manifestation` SHALL be coded as the nullFlavor `NI`.

### `reaction.substance`

An element to record the specific substance or pharmaceutical product considered to be responsible for event using the {{pagelink:ValueSet-UKCore-AllergySubstance}}
<br><br>

### `reaction.manifestation`

A mandatory element if a `AllergyIntolerance.reaction` is recorded for the clinical symptoms and/or signs that are observed or associated with the adverse reaction event.

Use nullFlavor `NI` for the case when a `AllergyIntolerance.reaction.severity` needs to be shared but where a `AllergyIntolerance.reaction.manifestation` is not known.
<br><br>

### `reaction.severity`

An optional value from a required terminology binding containing the values;
- `mild`
- `moderate`
- `severe`

#### Provider Systems

Where a `severity` is available in the provider system it SHALL be included to convey severity even if no other reaction details are explicitly available.

Where the severity is not known, this element SHOULD be omitted.

#### Provider Systems

Use of this element when populated as `severe` MAY be used to express life threatening allergies, used in conjunction with the `AllergyIntolerance.criticality` element.

An omitted `AllergyIntolerance.reaction.severity` will either mean severity data is not available within the provider system or the severity is not known by the provider system.
<br><br>

### `reaction.exposureRoute`

An optional element to identify the route by which the patient was exposed to the substance.

#### Provider Systems

If this data is available the binding SHOULD be to the {{pagelink:ValueSet-UKCore-SubstanceOrProductAdministrationRoute}}.

#### Provider Systems

Consumer systems are recommended not to include this coded information within automated clinical decision support. This is because it could either mean two quite different things;
1. The reaction only occurs if the substance enters the body via the specified route, implying the use of other routes is safe.

OR

2. The reaction was identified when the substance entered the body via the specified route, but could also react when using other routes.
<br><br>

### `reaction.note`

An optional element for when the clinical user wishes to provide supporting textual information for the reaction that cannot be conveyed within other elements of the backbone element.

See the related guidance above for `AllergyIntolerance.note`.

---
