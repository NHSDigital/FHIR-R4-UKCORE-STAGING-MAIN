---
topic: UKCore-Patient
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Patient
usage: http://hl7.org/fhir/StructureDefinition/Patient
---

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Address Key</b> - An example to illustrate the use of an address key used with the address datatype. </br>
{{pagelink:Extension-UKCore-AddressKey-Example}}   <br><br>

<b>Birth Sex</b> - An example to illustrate the extension for a patient's birth sex. </br>
{{pagelink:Extension-UKCore-BirthSex-Example}}   <br><br>

<b>Contact Rank</b> - An example to illustrate the extension for the patient's contact ranking. </br>
{{pagelink:Extension-UKCore-ContactRank-Example}}   <br><br>

<b>Contact Preference</b> - An example to illustrate the extension for a patient's contact preferences. </br>
{{pagelink:Extension-UKCore-ContactPreference-Example}}   <br><br>

<b>Copy Correspondence Indicator</b> - An Example to illustrate the extension for copy correspondence indicators. </br>
{{pagelink:Extension-UKCore-CopyCorrespondenceIndicator-Example}}   <br><br>

<b>Death Notification Status</b> - An example to illustrate the extension to indicate the death notification status of the patient. </br>
{{pagelink:Extension-UKCore-DeathNotificationStatus-Example}}   <br><br>

<b>Ethnic Category</b> - An example to illustrate patient Ethnic Category information. </br>
{{pagelink:Extension-UKCore-EthnicCategory-Example}}   <br><br>

<b>Melanie Jones</b> - An example of a baby patient. </br>
{{pagelink:UKCore-Patient-BabyPatient-Example}} <br><br>

<b>NHS Number Unavailable Reason</b>- An example of the extension which states the reason a patient's NHS number is unavailable.<br>
{{pagelink:Extension-UKCore-NHSNumberUnavailableReason-Example}} <br><br>

<b>NHS Number Verification Status</b> - An example of the extension which states the patient's NHS number verification status. </br>
{{pagelink:Extension-UKCore-NHSNumberVerificationStatus-Example}}   <br><br>

<b>Other Contact System</b> - An example to illustrate the extension to indicate other contact system(s) for a patient Richard Smith. </br>
{{pagelink:Extension-UKCore-OtherContactSystem-Example}}   <br><br>

<b>Residential Status</b> - An example to illustrate the extension to show the patient's residential status. </br>
{{pagelink:Extension-UKCore-ResidentialStatus-Example}}     <br><br> 

<b>Richard Smith</b> - An example to illustrate a male patient's demographics. </br>
{{pagelink:UKCore-Patient-RichardSmith-Example}}   <br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Patient profile:

- Query for Patient demographic information using the query parameter `Patient.identifier` for a known NHS number.
- Query for Patient demographic information using query parameters such as `Patient.name.family`, `Patient.name.given`, `Patient.birthDate`, and `Patient.gender`.
- Exchange Patient demographic information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---
