---
subject: http://hl7.org/fhir/5.0/StructureDefinition/extension-DiagnosticReport.media.link
---

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-DiagnosticReport,text:DiagnosticReport}}</td>
</tr>

</table>


{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>media.link R5 Backport extension</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to link a DocumentReference resource rather than a Media Resource<br>
  {{pagelink:Extension-UKCore-DiagnosticReportMediaLinkR5-Example}}
  <br><br>
</div>
<h3 id="guidance-diagnosticreportcomposition">Extension Specific Guidance</h3>
With <code>DiagnosticReport.media.link</code> being a mandatory element, the value SHALL be the extension <a href="http://hl7.org/fhir/StructureDefinition/data-absent-reason">http://hl7.org/fhir/StructureDefinition/data-absent-reason</a> with the valueCode of <code>unsupported</code>. See the example for more details.
</div>

---