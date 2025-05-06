---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-LegalStatus
issue: Extension-UKCore-LegalStatus
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:Profile-Encounter,text:Encounter}}</td>
</tr>
</table>

{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Legal Status</b>- An example to illustrate the extension which is used to indicate a patient's legal status on admission or discharge.<br>
  {{pagelink:UKCore-Extension-LegalStatus-Example}}
  <br><br>
</div>

<h3 id="guidance-legalstatus">Extension Specific Guidance</h3>

There are two bindings within this extension. `legalStatusContext` element to {{pagelink:ValueSet-UKCore-LegalStatusContext}}
, and `legalStatusClassification` element to {{pagelink:ValueSet-UKCore-LegalStatusClassification}}.

---