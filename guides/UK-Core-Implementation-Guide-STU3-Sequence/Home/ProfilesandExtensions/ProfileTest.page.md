---
topic: UKCore-AllergyIntolerance
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-AllergyIntolerance
usage: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
issue: UKCore-AllergyIntolerance
examples: AllergyIntolerance
---
# StructureDefinition {{variable:issue}}

<nospellcheck>
{{page:ProfileTemplate_test}}
</nospellcheck>



<div id="ProfileGuidance">

### Example Usage Scenarios

The following are feasible use cases for the UK Core AllergyIntolerance profile:

- Query for patient allergy information
- Exchange patient allergy information within a FHIR Document or FHIR Message
- Migration of allergies data between systems. 

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

### Use Case: Query

The query against a clinical system or shared record to return recorded allergies as `AllergyIntolerance` resources.

Returned results could be ordered by `AllergyIntolerance.recordedDate` and/or `AllergyIntolerance.lastOccurrence`.

Returned results MAY include multiple instances of the same allergy, as per the causative agent (`AllergyIntolerance.code`), but with different `AllergyIntolerance.clinicalStatus` values. The newer of such records either by `AllergyIntolerance.recordedDate` or `AllergyIntolerance.lastOccurrence` SHOULD be deemed the latest or current record of the allergy.

### Use Case: Exchange

For when systems need to exchange allergy information within a point-to-point message. The `AllergyIntolerance` resources can be included within a FHIR Message (within the Bundle), or within a FHIR Document alongside other structured resources and text-based data.

Allergy information SHOULD NOT be duplicated between systems (and, in England, this aligns with the NHS Data Strategy). When exchanging allergies data between systems be mindful of whether the receiving system plans to persist the data. If persisted, processes SHALL be put in place to ensure the data is updated if/when the source record is updated.

### Use Case: Migration

When allergy records are migrated between systems, the `AllergyIntolerance` resource could be used as a data migration standard.

Where migrated data is not coded, uses retired / invalidated codes, or coded with a terminology which cannot be mapped to SNOMED CT, then refer to the guidance on using degraded drug / non-drug allergy codes.

---

{{page:ProfileMustSupportTemplate}}

</div>

---

