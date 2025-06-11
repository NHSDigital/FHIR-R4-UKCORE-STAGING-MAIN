---
topic: Guidance-FHIRVersions
---
# {{page-title}}

This section details the development of UK Core with regards to alignment with HL7 FHIR sequences and versions, see the [FHIR version history](https://hl7.org/fhir/directory.html) for further information on FHIR sequences and versions.

## R4 Sequence 
The current UK Core development sequences (STU1, STU2, STU3) are derived from and aligned with the HL7 FHIR R4 sequence version v4.0.1: R4. 

## R4B Sequence
There is at the current time no plan to move the UK Core to any of the FHIR versions from the R4B sequence. When, and if there is a business or clinical need identified that could require migration of the UK Core to R4B this would only be done following discussion and agreement at the UK FHIR Board and with full consultation with the UK FHIR community.

## R5 Sequence
There is at the current time no plan to move the UK Core to any of the FHIR versions from the R5 sequence. When, and if there is a business or clinical need identified that could require migration of the UK Core to R5 this would only be done following discussion and agreement at the UK FHIR Board and with full consultation with the UK FHIR community. This would potentially require having an R5 UK Core in addition to an R4 version with an agreed migration to R5 UK Core roadmap along with a deprecation strategy of R4 UK Core in place.

**Important note:** To meet some current business and clinical needs of current UK Core R4 use cases some of the functionally of R5 has been pre-adopted as extensions using a method known as “back porting”, within the current R4 UK Core. This is an accepted method commonly used by implementers of FHIR globally. See the {{pagelink:Library-Extensions-PreAdopt,text:section in UK Core}} for further information about back porting. 

## R6 Sequence
There is currently no adoptable R6 versions available in FHIR. 
