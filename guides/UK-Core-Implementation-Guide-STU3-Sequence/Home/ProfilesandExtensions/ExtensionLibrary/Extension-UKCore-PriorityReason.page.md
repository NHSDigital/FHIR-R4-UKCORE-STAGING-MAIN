---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-PriorityReason
issue: Extension-UKCore-PriorityReason
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-ServiceRequest,text:ServiceRequest.priority}}</td>
</tr>
</table>

{{page:ExtensionTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Priority Reason</b> - An example to illustrate the priority reason extension, using a SNOMED CT concept, for a service request marked as urgent.<br>
{{pagelink:UKCore-Extension-PriorityReason-Example}}
<br><br>
  <b>Priority Reason</b> - An example to illustrate the priority reason extension, using a plain text reason, for a service request marked as urgent.<br>
{{pagelink:UKCore-Extension-PriorityReason-SendingAsText-Example}}
<br><br>
</div>

<h3 id="guidance-priorityreason">Extension Specific Guidance</h3>

There is a binding within this extension to a {{pagelink:ValueSet-UKCore-ServiceRequestReasonCode}}.

---
