---
topic: UKCore-DiagnosticReport
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-DiagnosticReport
usage: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
issue: UKCore-DiagnosticReport
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Composition Reference</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to send a composition resource with a diagnostic report.<br>
  {{pagelink:UKCore-Extension-CompositionReference-Example}}
  <br><br>
  <b>CT Chest Scan Report</b> - An example to illustrate a diagnostic report containing an imaging study for a patient.<br/>
{{pagelink:UKCore-DiagnosticReport-CTChestScan-Example}}<br>
  NOTE: The above example references {{pagelink:UKCore-ImagingStudy-CTChestScan-Example}}
<br><br>
  <b>Diagnostic Report Note</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to add notes and annotations to a diagnostic report.<br>
  {{pagelink:UKCore-Extension-Note-Example}}
  <br><br>
  <b>Diagnostic Studies Report</b> - An example to illustrate a diagnostic studies report containing a specimen and observation for a patient.<br/>
{{pagelink:UKCore-DiagnosticReport-Lab-DiagnosticStudiesReport-Example}}
<br><br>
 <b>Device Reference</b> - An example to illustrate the extension which is used to indicate the performer of a Diagnostic Report was a device.<br>
  {{pagelink:UKCore-Extension-DeviceReference-Example}}<br>
  NOTE: The above example references {{pagelink:UKCore-Device-SoftwareAsAMedicalDevice-Example}}
<br><br>
  <b>ECG Report</b> - An example to illustrate a diagnostic report presented in pdf, for an ECG.<br/>
{{pagelink:UKCore-DiagnosticReport-ECG-Example}}
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

{{page:ProfileMustSupportTemplate}}

</div>

---
