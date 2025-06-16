---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-ContactPreference
---
## StructureDefinition {{variable:topic}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-RelatedPerson,text:RelatedPerson}}<br/>
{{pagelink:UKCore-Patient,text:Patient}}</td>
</tr>
</table>

{{page:ExtensionTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Contact Preference</b>- An example to illustrate the extension for a patient's contact preferences.<br>
{{pagelink:Extension-UKCore-ContactPreference-Example}}
<br><br>
</div>

<h3 id="guidance-contactpreference">Extension Specific Guidance</h3>

There are two bindings within this extension. `PreferredContactMethod` element to {{pagelink:ValueSet-UKCore-PreferredContactMethod}}
, and `PreferredWrittenCommunicationFormat` element to {{pagelink:ValueSet-UKCore-PreferredWrittenCommunicationFormat}}.

---