## `medication[x]`

### Medication WITH dm+d code

Where a dm+d code exists it SHALL be used either as `MedicationDispense.medicationCodeableConcept.coding` or as `MedicationDispense.medicationReference.Medication.code`

Where CodeableConcept is used, `MedicationDispense.medicationCodeableConcept.coding` is the dm+d code and `MedicationDispense.medicationCodeableConcept.text` is dm+d concept name/description. 

Can be either a dm+d code as a CodeableConcept or reference to UK Core {{pagelink:Profile-Medication}}
resource. Using a CodeableConcept is preferred unless additional data if required that would be contained within a UK Core {{pagelink:Profile-Medication}} resource.

The elements `MedicationDispense.medicationCodeableConcept.coding` and `MedicationDispense.medicationReference.Medication.code` are both bound to {{pagelink:ValueSet-UKCore-MedicationCode}}

Examples where a reference to a UK Core {{pagelink:Profile-Medication}} would be applicable include:

- Record a VTM with a specific form 
- Record manufacturer with a concept as described in {{pagelink:ValueSet-UKCore-MedicationCode}}
- Record batch number
- Record ingredients (for example with a magisterial prescription or an excipient).

### Medication WITHOUT dm+d code

Medication not published within the dm+d may be requested in the Acute care setting.

In this scenario it is recommended to use the `MedicationDispense.medicationCodeableConcept` variant for this element. 

If the prescribing system has both a locally assigned code and description for the medication then;

- The `MedicationDispense.medicationCodeableConcept.text` SHOULD be the description for the medication.  
- The `MedicationDispense.medicationCodeableConcept.coding.code` SHOULD be the code for the medication.  
- The `MedicationDispense.medicationCodeableConcept.coding.display` SHOULD be the description for the medication, i.e. the same value as `MedicationDispense.medicationCodeableConcept.text`.  

If the prescribing system only has a description for the medication then;  

- The `MedicationDispense.medicationCodeableConcept.text` SHOULD be the locally assigned description for the medication.  


---
