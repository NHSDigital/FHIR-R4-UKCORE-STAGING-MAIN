## `supportingInformation`

Where a UK Core profile exists, the resource being referenced SHOULD conform to the profile.

Some examples of use include:

- Reference an `Observation` resource to share data like the patient’s height and weight.
- Reference a `Condition` resource to share a patient’s condition if this influences the pharmacy dispensing process. For example; 105502003 Dependence on renal dialysis (finding) or 46177005 End stage renal disease (disorder) would justify an unusual dosage on a prescription.
- Reference an `AllergyIntolerance` resource to share a patient’s allergy to make it clear why certain medication is being requested. For example, a Penicillin allergy.
- Reference a `CarePlan` resource where medication dispensing is considered as part of a specific treatment regimen. For example, care plans for stroke patients.




---
