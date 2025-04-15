## `identifier`

In England and Wales this SHOULD include the patient's NHS number, where this is not possible then a Medical Records Number (MRN) MAY be used.

If the identifier is an NHS number then the extension `Patient.identifier:nhsNumber.extension:nhsNumberVerificationStatus` SHOULD be populated to indicate the verification status with a code from the {{pagelink:ValueSet-UKCore-NHSNumberVerificationStatus}}.

<div markdown="span" class="alert alert-success" role="alert">
If the NHS number is unavailable, then a reason MAY be stated using the extension {{pagelink:Extension-UKCore-NHSNumberUnavailableReason}}.
</div>

---
