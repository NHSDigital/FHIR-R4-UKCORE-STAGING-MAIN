## `status`

The `MedicationAdministration.status` element SHALL be populated with a value from the International FHIR ValueSet [medication-admin-status](https://hl7.org/fhir/R4/valueset-medication-admin-status.html), which is shown expanded here with additional guidance.

Systems consuming the data SHOULD use `MedicationAdministration.status` to support workflow. 

The status can be used to determine the overall status of medication administration events. 

It is recommended that the `MedicationAdministration.status` is used to indicate the status at a high-level so that integrated systems can determine how to represent this information. 

<table class="assets" title="Status list">
    <thead>
        <tr>
            <th>Status</th>
            <th>FHIR Definition</th>
            <th>Implementation Guidance</th>
        </tr>
    </thead>
    <tbody>
        <!-- in-progress -->
        <tr>
            <td><code>in-progress</code></td>
            <td>
                The administration has started but has not yet completed.
            </td>
            <td>Would be a suitable status to use, for example, by an infusion pump device which is interoperable with the clinical system to denote an infusion is in progress.</td>
        </tr>
        <!-- not-done -->
        <tr>
            <td><code>not-done</code></td>
            <td>
                The administration was terminated prior to any impact on the subject (though preparatory actions may have been taken)
            </td>
            <td>Use this when there is not the intention to undertake the administration at a future time.</td>
        </tr>
        <!-- on-hold -->
        <tr>
            <td><code>on-hold</code></td>
            <td>
                Actions implied by the administration have been temporarily halted, but are expected to continue later. May also be called 'suspended'.
            </td>
            <td>Use this when there is the intention to administer the medication at a future time. For example, if the patient is temporarily unavailable.</td>
        </tr>
        <!-- completed -->
        <tr>
            <td><code>completed</code></td>
            <td>
                All actions that are implied by the administration have occurred.
            </td>
            <td>
                This would be a suitable trigger to share the medication administration event with shared records.
            </td>
        </tr>
        <!-- entered-in-error -->
        <tr>
            <td><code>entered-in-error</code></td>
            <td>
                The administration was entered in error and therefore nullified.
            </td>
            <td>There is limited value in sharing records that are entered in error.</td>
        </tr>
        <!-- stopped -->
        <tr>
            <td><code>stopped</code></td>
            <td>
                Actions implied by the administration have been permanently halted, before all of them occurred.
            </td>
            <td>
                A <code>MedicationAdministration.statusReason</code> SHOULD be populated with a coded reason for stopping the medication administration.
                <br><br>
                This is for things like patches and continuous infusions etc. where administration is over a period of time. The <code>MedicationAdministration.dosage</code> SHOULD reflect the amount administered (or whatever the source system has recorded).
            </td>
        </tr>
        <!-- unknown -->
        <tr>
            <td><code>unknown</code></td>
            <td>
                The authoring system does not know which of the status values currently applies for this request. Note: This concept is not to be used for 'other' - one of the statuses listed is presumed to apply, it's just not known which one.
            </td>
            <td>
                The patient may have had some encounter with this medication, but the current status is unknown. Avoid the use of this status value where possible.
            </td>
        </tr>    
    </tbody>
</table>

---
