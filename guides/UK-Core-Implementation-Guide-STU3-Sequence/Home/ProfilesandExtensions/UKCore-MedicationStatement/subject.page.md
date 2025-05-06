## `subject`

A reference to the patient.

Within a FHIR Messaging or FHIR Document implementation, include a {{pagelink:UKCore-Patient}} resource within the Bundle with at least the minimum dataset populated as defined within the UK Core standard. The `MedicationStatement.subject.reference` points to the resource in the Bundle.

Within a RESTful implementation a `MedicationStatement.subject.reference` and/or `MedicationStatement.subject.identifier` SHALL be provided that allows the consumer system to query another API if they need to access the complete {{pagelink:UKCore-Patient}} resource. 

For implementations within England and Wales, the `MedicationStatement.subject.identifier` could be the patient's **NHS Number**, allowing a consumer system to use the NHS England Personal Demographics Service FHIR API to return a Patient resource.

For implementations within Scotland, the `MedicationStatement.subject.identifier` could be the patient's **CHI Number**.

---