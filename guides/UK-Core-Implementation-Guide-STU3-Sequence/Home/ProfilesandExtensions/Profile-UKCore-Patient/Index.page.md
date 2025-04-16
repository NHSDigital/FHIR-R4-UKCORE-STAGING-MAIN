---
topic: Profile-Patient
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Patient
usage: http://hl7.org/fhir/StructureDefinition/Patient
issue: UKCore-Patient
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Address Key</b> - An example to illustrate the use of an address key used with the address datatype. </br>
{{pagelink:Example-UKCore-Extension-AddressKey}}   <br><br>

<b>Birth Sex</b> - An example to illustrate the extension for a patient's birth sex. </br>
{{pagelink:Example-UKCore-Extension-BirthSex}}   <br><br>

<b>Contact Rank</b> - An example to illustrate the extension for the patient's contact ranking. </br>
{{pagelink:Example-UKCore-Extension-ContactRank}}   <br><br>

<b>Contact Preference</b> - An example to illustrate the extension for a patient's contact preferences. </br>
{{pagelink:Example-UKCore-Extension-ContactPreference}}   <br><br>

<b>Copy Correspondence Indicator</b> - An Example to illustrate the extension for copy correspondence indicators. </br>
{{pagelink:Example-UKCore-Extension-CopyCorrespondenceIndicator}}   <br><br>

<b>Death Notification Status</b> - An example to illustrate the extension to indicate the death notification status of the patient. </br>
{{pagelink:Example-UKCore-Extension-DeathNotificationStatus}}   <br><br>

<b>Ethnic Category</b> - An example to illustrate patient Ethnic Category information. </br>
{{pagelink:Example-UKCore-Extension-EthnicCategory}}   <br><br>

<b>Melanie Jones</b> - An example of a baby patient. </br>
{{pagelink:Example-UKCore-Patient-BabyPatient}} <br><br>

<b>NHS Number Unavailable Reason</b>- An example of the extension which states the reason a patient's NHS number is unavailable.<br>
{{pagelink:Example-UKCore-Extension-NHSNumberUnavailableReason}} <br><br>

<b>NHS Number Verification Status</b> - An example of the extension which states the patient's NHS number verification status. </br>
{{pagelink:Example-UKCore-Extension-NHSNumberVerificationStatus}}   <br><br>

<b>Other Contact System</b> - An example to illustrate the extension to indicate other contact system(s) for a patient Richard Smith. </br>
{{pagelink:Example-UKCore-Extension-OtherContactSystem}}   <br><br>

<b>Residential Status</b> - An example to illustrate the extension to show the patient's residential status. </br>
{{pagelink:Example-UKCore-Extension-ResidentialStatus}}     <br><br> 

<b>Richard Smith</b> - An example to illustrate a male patient's demographics. </br>
{{pagelink:Example-UKCore-Patient-RichardSmith}}   <br><br>
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

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---
