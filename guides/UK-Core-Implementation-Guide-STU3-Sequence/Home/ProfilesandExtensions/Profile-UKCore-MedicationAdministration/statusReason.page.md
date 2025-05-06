## `statusReason`

A coded reason for why an administration was not performed.

SHOULD only be populated when the `MedicationAdministration.status` is either `stopped`, `not-done` or `on-hold`.
<br><br>

### Example scenarios for the use of `status` and `statusReason`.

#### Some medication was taken, but not all that was intended, for whatever reason, e.g. an infusion that was started, and finished prematurely.

- status = `stopped` <br>
- status reason = 416093006 | Allergic reaction to drug <br>
- dosage = Should reflect how much was actually administered, e.g. 150ml (instead of 200ml requested)
 
Note: For this example it would be expected that the originating MedicationRequest would be updated with a status of `stopped` which should prevent the system from scheduling an administration or delete any that have been scheduled. Where administration records are retained, use the status of `stopped`.
<br><br>
#### Patient refused to take the medication.

- status = `not-done` <br>
- statusReason = 182895007 | Drug declined by patient (finding) - or a child concept of the above

Where required use `MedicationAdministration.note` to capture additional notes for why the patient refused the medication.
<br><br>

#### Patient not available, e.g. on home leave for a couple of days, moved ward, location unknown, etc. and not recorded as `on-hold`.

- status = `not-done` <br>
- statusReason = 398090008 | Patient unavailable (finding)
<br><br>


#### Medication was taken but patient then vomited all/some of the medication.

- status = `on-hold` or `stopped` <br>
- statusReason = 419219000 | Drug-induced nausea and vomiting

Use `MedicationAdministration.note` for additional notes for what happened, provided the administration record can be amended after the vomiting episode.
<br><br>

#### An infusion for the patient is paused for a period based on blood test results. Or, a nutrition feed is paused for clinical reasons, to restart again later.

- status = `on-hold`<br>
- statusReason = Optional. Any valid SNOMED term.<br>
- dosage = The dosage would either be recorded with a zero rateRatio or rateQuantity or may be fully omitted. Both must be interpreted as a zero medication administration.

---