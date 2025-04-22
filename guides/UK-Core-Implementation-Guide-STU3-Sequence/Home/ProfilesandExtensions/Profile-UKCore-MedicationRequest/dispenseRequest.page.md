## `dispenseRequest`
Used to convey specific dispensing requests to the pharmacy that are not otherwise detailed within the `MedicationRequest.dosageInstruction`.

For most medication requests the hospital pharmacy will typically dispense a quantity of medication appropriate for the medication and dosage, as per their local agreed best practice, to balance the quantity of medication held in pharmacy to that held on the ward.

The inclusion of a `MedicationRequest.dispenseRequest` MAY be useful when requesting discharge medication requests. 

<table class="assets" title="Use cases for dispenseRequest">
    <thead>
        </tr>
            <th>Use Case</th>
            <th>Original Medication</th>
            <th>Discharge Medication</th>
            <th>dispense Request</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Instruction to the pharmacy to dispense a specific quantity of medication, either expressed as a number of days or as a dose form quantity.</td>
            <td>Paracetamol - 1g - four times a day</td>
            <td>Paracetamol - 1g - four times a day<br/><br/>One week supplied on discharge.</td>
            <td>7 days <i>or</i> 28 tablets</td>
        </tr>
        <tr>
            <td>Any inpatient scenario where the pharmacy is instructed to dispense a specific quantity of medication. For example, if the patient is known to be discharged soon.</td>
            <td>Atenolol - 50mg - daily</td>
            <td>Atenolol - 50mg - daily<br/><br/>Two weeks supplied on discharge, GP to continue.</td>
            <td>14 days <i>or</i> 14 tablets</td>
        </tr>
    </tbody>
</table>

### `dispenseRequest.validityPeriod`
In electronic repeat dispensing, the `MedicationRequest.dispenseRequest.validityPeriod.end` is used to record when an eRD prescription cycle ends. This is different to the extension `medicationRepeatInformation.authorisationExpiryDate` which is the date the prescriber must review the prescription with the patient.

---
