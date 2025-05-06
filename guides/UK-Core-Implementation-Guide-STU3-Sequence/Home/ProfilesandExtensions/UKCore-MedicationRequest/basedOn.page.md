## `basedOn`

Where possible, it is expected that the resource being referenced SHOULD conform to one of the following UK Core profiles:

- [UKCore-CarePlan (draft)]("https://simplifier.net/guide/UKCoreImplementationGuideAssetsinDevelopment/Home/ProfilesandExtensions/Profile-UKCore-CarePlan)
- {{pagelink:Profile-MedicationRequest}}
- {{pagelink:Profile-ServiceRequest}}
- [ImmunizationRecommendation Resource](https://www.hl7.org/fhir/r4/immunizationrecommendation.html)

**Recommendation**: To reference a previous medication request use `MedicationRequest.priorPrescription` instead of this element.

If the clinical system has implemented the `CarePlan` resource, a logical link to the care plan for which the medication request is based has business benefit.



---
