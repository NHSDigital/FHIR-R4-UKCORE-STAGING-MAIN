## `statusReason[x]`

A reason for why a dispense was not performed, either as a reference to a <a href="https://hl7.org/fhir/R4/detectedissue.html" class="external">DetectedIssue</a> resource, or a coded reason from the <a href="https://hl7.org/fhir/R4/valueset-medicationdispense-status-reason.html" class="external">medicationdispense-status-reason</a> valueset.

This SHOULD only be populated when the `MedicationDispense.status` is either `cancelled`, `stopped` or `declined`.

---