## `status`


<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Important:</h4>
This is the next most important element of a <code>MedicationStatement</code> after the <code>Medication</code>.<br/>

It provides the consumer with information to determine if the medication is relevant for their use case.<br/>

For example: whether the medication is deemed <code>active</code> (current).
</div>

<table class="assets" title="Status list">
    <thead>
        <tr>
            <th>Status</th>
            <th>FHIR Definition</th>
            <th>Recommendation</th>
        </tr>
    </thead>
    <tbody>
        <!-- active -->
        <tr>
            <td><code>active</code></td>
            <td>
                The medication is still being taken.
            </td>
            <td>
                It is believed the medication is active in the patient's
                system.
            </td>
        </tr>
        <!-- completed -->
        <tr>
            <td><code>completed</code></td>
            <td>
            	The medication is no longer being taken.
            </td>
            <td>
                A course of medication has been completed and the medication is not active in the patient's system.
            </td>
        </tr>
        <!-- entered-in-error -->
        <tr>
            <td><code>entered-in-error</code></td>
            <td>
                Some of the actions that are implied by the medication statement may have occurred. For example, the patient may have taken some of the medication. Clinical decision support systems SHOULD take this status into account.
            </td>
            <td>
                Indicates the <code>MedicationStatement</code> is INVALID. It is not expected that a <code>MedicationStatement</code> with this status would be included in exchanges.
            </td>
        </tr>
        <!-- intended -->
        <tr>
            <td><code>intended</code></td>
            <td>
                The medication may be taken at some time in the future.
            </td>
            <td>
                It is intended that the medication will be given to the patient. When this is used <code>effective[x]</code> SHALL indicate when it is intended that the medication is to be taken.
            </td>
        </tr>
        <!-- stopped -->
        <tr>
            <td><code>stopped</code></td>
            <td>
                Actions implied by the statement have been permanently halted, before all of them occurred. This SHOULD NOT be used if the statement was entered in error.
            </td>
            <td>
                Medication has been stopped before the completion of the prescribed course and there is no plan to restart it. When used the reason SHALL be indicated in <code>MedicationStatement.statusReason</code>.
            </td>
        </tr>
        <!-- on-hold -->
        <tr>
            <td><code>on-hold</code></td>
            <td>
                Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be called "suspended".
            </td>
            <td>
                Medication has been temporarily stopped.
                <br />
                When used the reason SHALL be indicated in <code>MedicationStatement.statusReason</code>.
                <br />
                Where it is known when it is intended to restart it this MAY be indicated in <code>MedicationStatement.statusReason</code>.
            </td>
        </tr>
        <!-- unknown -->
        <tr>
            <td><code>unknown</code></td>
            <td>
                The state of the medication use is not currently known.
            </td>
            <td>
                The patient may have had some encounter with this medication, but the current status is unknown. Avoid the use of this status value where possible.
            </td>
        </tr>
        <!-- not-taken -->
        <tr>
            <td><code>not-taken</code></td>
            <td>
                The medication was not consumed by the patient
            </td>
            <td>
                Use this when there is certainty that the patient has not consumed any of the intended medication.
            </td>
        </tr>        
    </tbody>
</table>

<br/>
<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Important:</h4>
Determining the value of this element when constructing the resource.<br/>
The status will need to be calculated if the <code>MedicationStatement.basedOn</code> or <code>MedicationStatement.partOf</code> elements within the profile are defined.
</div>

A `MedicationStatement` represents a snapshot in time of a patient medication - and if the status is not available in the source system, then the following business rule MAY apply to compute the state.

<table class="assets" title="Determining status">
    <thead>
        <tr>
            <th>Status</th>
            <th>How it can be determined</th>
        </tr>
    </thead>
    <tbody>
        <!-- active -->
        <tr>
            <td><code>active</code></td>
            <td>
                A completed <code>MedicationRequest</code> (if known) where the current date is between the <code>MedicationRequest.dispenseRequest.validityPeriod</code> element. The <code>MedicationStatement.effectivePeriod</code> element SHOULD reflect this information.
                <br />
                <strong>or</strong>
                <br />
                Where the current date is between the <code>MedicationStatement.effectivePeriod</code>
            </td>
        </tr>
        <!-- completed -->
        <tr>
            <td><code>completed</code></td>
            <td>
                Where the current date is after the <code>MedicationStatement.effectivePeriod</code>
                <br />
                <strong>or</strong>
                <br />
                A completed <code>MedicationRequest</code> (if known) where the <code>MedicationRequest.dispenseRequest</code> element is either not defined, or the current date is greater than the <code>dispenseRequest.validityPeriod</code>.
            </td>
            <!-- entered in error -->
            <tr>
                
            </tr>
        </tr>
    </tbody>
</table>

---
