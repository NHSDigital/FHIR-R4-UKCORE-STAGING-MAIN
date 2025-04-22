## `status` 

**It is expected that most implementations will require the use of status to support workflow.**

The status can be used to determine the overall status of dispense request; however, it does not cater for the granularity that prescription tracking software can offer.

It is recommended that the `MedicationDispense.status` is used to indicate the status at a high-level so that integrated systems can determine how to represent this information.

<table class="assets" title="Status list">
    <thead>
        <tr>
            <th>Status</th>
            <th>FHIR Definition</th>
            <th>Implementation Guidance</th>
        </tr>
    </thead>
    <tbody>
        <!-- preparation -->
        <tr>
            <td><code>preparation</code></td>
            <td>
            	The core event has not started yet, but some staging activities have begun (e.g. initial compounding or packaging of medication). Preparation stages MAY be tracked for billing purposes.
            </td>
            <td>
                Consider how the status <code>preparation</code> is presented to the end-user to avoid confusion with <code>in-progress</code>.
            </td>
        </tr>
        <!-- in-progress -->
        <tr>
            <td><code>in-progress</code></td>
            <td>
                The dispensed product is ready for pickup.
            </td>
            <td>
                Consider how the status <code>in-progress</code> is presented to the end-user to avoid confusion with <code>complete</code> when dispensed medication is in-transit to a ward, or to a patient via a delivery service.
            </td>
        </tr>
        <!-- cancelled -->
        <tr>
            <td><code>cancelled</code></td>
            <td>
                The dispensed product was not and will never be picked up by the patient.
            </td>
            <td>
                Avoid the use of this status value where possible as very similar to <code>stopped</code> and therefore potentially confusing.
            </td>
        </tr>
        <!-- on-hold -->
        <tr>
            <td><code>on-hold</code></td>
            <td>
                The dispense process is paused while waiting for an external event to reactivate the dispense. For example, new stock has arrived or the prescriber has called.
            </td>
            <td>
                Probably most useful as a pharmacy-facing status. If exposed to users outside the pharmacy, such users may want to know how long the dispensing event will be on hold in case alternative dispensing arrangements need to be identified.
            </td>
        </tr>
        <!-- completed -->
        <tr>
            <td><code>completed</code></td>
            <td>
                The dispensed product has been picked up.
            </td>
            <td>
                This would be a suitable trigger to post / share the medication dispense with the requesting ePMA system.
            </td>
        </tr>
        <!-- entered-in-error -->
        <tr>
            <td><code>entered-in-error</code></td>
            <td>
                The dispense was entered in error and therefore nullified.
            </td>
            <td>
                Not to be used unless specific use-cases can be identified.
            </td>
        </tr>
        <!-- stopped -->
        <tr>
            <td><code>stopped</code></td>
            <td>
                Actions implied by the dispense have been permanently halted, before all of them occurred.
            </td>
            <td>
                A <code>MedicationDispense.statusReason</code> SHOULD be populated with a coded reason for stopping the medication administration. This would be a suitable trigger to post / share the medication dispense with the requesting ePMA system.
            </td>
        </tr>
        <!-- declined -->
        <tr>
            <td><code>declined</code></td>
            <td>
                The dispense was declined and not performed
            </td>
            <td>
                This would be a suitable trigger to post / share the declined medication dispense event with the requesting ePMA system.
            </td>
        </tr>
        <!-- unknown -->
        <tr>
            <td><code>unknown</code></td>
            <td>
                The authoring system does not know which of the status values applies for this medication dispense. Note: this concept is not to be used for other - one of the listed statuses is presumed to apply, it's just not known which one.
            </td>
            <td>
                Avoid the use of this status value where possible.
            </td>
        </tr>
    </tbody>
</table>

<br />

<div id="renderParent" title="Medication Dispense flowchart">
{{render: medication-dispense-status-flow }}
</div>

---
