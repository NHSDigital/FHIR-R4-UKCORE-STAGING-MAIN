---
topic: Encounter
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Encounter
usage: http://hl7.org/fhir/StructureDefinition/Encounter
issue: UKCore-Encounter
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>

  <b>Admission Method</b>- An example to illustrate the extension for an encounter to support the method by which an individual was admitted into hospital.<br>
  {{pagelink:UKCore-Extension-AdmissionMethod-Example}}
  <br><br>

  <b>Discharge Method</b>- An example to illustrate the extension for an encounter to support the method of discharge from a hospital.<br>
  {{pagelink:UKCore-Extension-DischargeMethod-Example}}
  <br><br>

  <b>Emergency Care Discharge Status</b>- An example to illustrate the extension which is used to indicate the status of an individual on discharge from an Emergency Care Department.<br>
  {{pagelink:UKCore-Extension-EmergencyCareDischargeStatus-Example}}
  <br><br>

<b>Inpatient Encounter</b> - An example to illustrate an inpatient encounter.
<br>{{pagelink:UKCore-Encounter-InpatientEncounter-Example}}
  <br><br>

  <b>Legal Status</b>- An example to illustrate the extension which is used to indicate a patient's legal status on admission or discharge.<br>
  {{pagelink:UKCore-Extension-LegalStatus-Example}}
  <br><br>
  
  <b>Outcome of Attendance</b>- An example to illustrate the extension which is used to indicate the outcome of an outpatient attendance.<br>
  {{pagelink:UKCore-Extension-OutcomeOfAttendance-Example}}
  <br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Encounter profile:

- Query for a specific patient encounter
- Query for recent patient encounters
- Record or update an encounter

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---