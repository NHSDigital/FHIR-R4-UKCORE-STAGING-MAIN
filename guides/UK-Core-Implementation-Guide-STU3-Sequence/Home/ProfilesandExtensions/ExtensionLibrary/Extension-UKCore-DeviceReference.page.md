---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-DeviceReference
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-DiagnosticReport,text:DiagnosticReport.performer}}<br>
{{pagelink:UKCore-DiagnosticReport,text:DiagnosticReport.resultsInterpreter}}</td>
</tr>
</table>

{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Device Reference</b> - An example to illustrate the extension which is used to indicate the performer of a Diagnostic Report was software as a medical device.<br>
  {{pagelink:Extension-UKCore-DeviceReference-Example}}<br>
  NOTE: The above example references {{pagelink:UKCore-Device-SoftwareAsAMedicalDevice-Example}}
  <br><br>
</div>

<h3 id="guidance-devicereference">Extension Specific Guidance</h3>

Where possible, it is expected that the resource being referenced SHOULD conform to [UKCore-Device](https://simplifier.net/guide/UKCoreImplementationGuideAssetsinDevelopment/Home/ProfilesandExtensions/Profile-UKCore-Device).

---