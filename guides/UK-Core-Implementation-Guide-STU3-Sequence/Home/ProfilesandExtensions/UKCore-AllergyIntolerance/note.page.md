## `note`
An optional element for when the clinical user wishes to provide supporting textual information for the allergy record that cannot be conveyed within other elements of the resource.

#### Provider Systems

Where a provider system only has the capability to record a note at one level it SHOULD populate the `AllergyIntolerance.note` elements with any notes data captured within the system, irrespective of the data level that the system uses to capture that data.

Where a provider system has the capability to record a note at both the `AllergyIntolerance` and at the `AllergyIntolerance.reaction` level it SHOULD populate both with the relevant notes applicable to each level.

#### Provider Systems

Consumer systems SHALL be able to handle both multiple `AllergyIntolerance.note` and multiple `AllergyIntolerance.reaction.note` elements.

---
