---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-ContactPreference
issue: Extension-UKCore-ContactPreference
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:Profile-RelatedPerson,text:RelatedPerson}}<br/>
{{pagelink:Profile-Patient,text:Patient}}</td>
</tr>
</table>

{{page:Home/ProfilesandExtensions/ExtensionTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Contact Preference</b>- An example to illustrate the extension for a patient's contact preferences.<br>
{{pagelink:UKCore-Extension-ContactPreference-Example}}
<br><br>
</div>

<h3 id="guidance-contactpreference">Extension Specific Guidance</h3>

There are two bindings within this extension. `PreferredContactMethod` element to {{pagelink:ValueSet-UKCore-PreferredContactMethod}}
, and `PreferredWrittenCommunicationFormat` element to {{pagelink:ValueSet-UKCore-PreferredWrittenCommunicationFormat}}.

---