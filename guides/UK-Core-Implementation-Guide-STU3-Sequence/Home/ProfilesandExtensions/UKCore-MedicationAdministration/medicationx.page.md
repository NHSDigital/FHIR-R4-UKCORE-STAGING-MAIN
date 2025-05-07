## `medication[x]`  

### Medication WITH dm+d code

Where a dm+d code exists it SHALL be used either as `MedicationAdministration.medicationCodeableConcept.coding` or as `MedicationAdministration.medicationReference.Medication.code`.

Where CodeableConcept is used, `MedicationAdministration.medicationCodeableConcept.coding` is the dm+d code and `MedicationAdministration.medicationCodeableConcept.text` is dm+d concept name/description.

Can be either a dm+d code as a CodeableConcept or reference to a {{pagelink:UKCore-Medication}}. 

Using a CodeableConcept is preferred unless additional data is required that would be contained within a {{pagelink:UKCore-Medication}}.

The elements `MedicationAdministration.medicationCodeableConcept.coding` and `MedicationAdministration.medicationReference.Medication.code` are both bound to {{pagelink:ValueSet-UKCore-MedicationCode}}

Examples where a reference to a {{pagelink:UKCore-Medication}} would be applicable include:

- Record a VTM with a specific form 
- Record manufacturer with a concept as described in {{pagelink:ValueSet-UKCore-MedicationCode}}
- Record batch number
- Record ingredients (for example with a magisterial prescription or an excipient). 

### Medication WITHOUT dm+d code

Medication not published within the dm+d may be requested in the Acute care setting.

In this scenario it is recommended to use the CodeableConcept variant for this element. 

If the prescribing system has both a locally assigned code and description for the medication then;  

- The `MedicationAdministration.medicationCodeableConcept.text` SHOULD be the description for the medication.  
- The `MedicationAdministration.medicationCodeableConcept.coding.code` SHOULD be the code for the medication.  
- The `MedicationAdministration.medicationCodeableConcept.coding.display` SHOULD be the description for the medication, i.e. the same value as `MedicationAdministration.medicationCodeableConcept.text`.  

If the prescribing system only has a description for the medication then;  

- The `MedicationAdministration.medicationCodeableConcept.text` SHOULD be the locally assigned description for the medication.  

---
