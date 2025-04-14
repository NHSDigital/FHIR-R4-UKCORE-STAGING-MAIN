---
topic: Profile-DiagnosticReport
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-DiagnosticReport
usage: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
issue: UKCore-DiagnosticReport
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Composition Reference</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to send a composition resource with a diagnostic report.<br>
  {{pagelink:Example-UKCore-Extension-CompositionReference}}
  <br><br>
  <b>CT Chest Scan Report</b> - An example to illustrate a diagnostic report containing an imaging study for a patient.<br/>
{{pagelink:Example-UKCore-DiagnosticReport-CTChestScan}}<br>
  NOTE: The above example references {{pagelink:Example-UKCore-ImagingStudy-CTChestScan}}
<br><br>
  <b>Diagnostic Report Note</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to add notes and annotations to a diagnostic report.<br>
  {{pagelink:Example-UKCore-Extension-Note}}
  <br><br>
  <b>Diagnostic Studies Report</b> - An example to illustrate a diagnostic studies report containing a specimen and observation for a patient.<br/>
{{pagelink:Example-UKCore-DiagnosticReport-Lab-DiagnosticStudiesReport}}
<br><br>
 <b>Device Reference</b> - An example to illustrate the extension which is used to indicate the performer of a Diagnostic Report was a device.<br>
  {{pagelink:Example-UKCore-Extension-DeviceReference}}<br>
  NOTE: The above example references {{pagelink:Example-UKCore-Device-SoftwareAsAMedicalDevice}}
<br><br>
  <b>ECG Report</b> - An example to illustrate a diagnostic report presented in pdf, for an ECG.<br/>
{{pagelink:Example-UKCore-DiagnosticReport-ECG}}
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios

The following are example usage scenarios for the UK Core DiagnosticReport profile:

- Query for a specific patient test result
- Query for recent test results
- Record or update a test result

Services that should consider using the  UK Core DiagnosticReport profile are:

- Pathology
- Genomics
- Lab Result

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---
