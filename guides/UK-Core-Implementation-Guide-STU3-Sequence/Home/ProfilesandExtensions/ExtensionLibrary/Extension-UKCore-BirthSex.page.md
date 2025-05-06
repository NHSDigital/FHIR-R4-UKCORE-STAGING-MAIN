---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-BirthSex
issue: Extension-UKCore-BirthSex
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:Profile-Patient,text:Patient}}</td>
</tr>
</table>

{{page:Home/ProfilesandExtensions/ExtensionTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Birth Sex</b>- An example to illustrate the extension for a patient's birth sex.<br>
  {{pagelink:UKCore-Extension-BirthSex-Example}}
  <br><br>
</div>

<h3 id="guidance-birthsex">Extension Specific Guidance</h3>

There is a binding within this extension to a {{pagelink:ValueSet-UKCore-BirthSex}}.

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The datatype of this extension was changed from <code>valueCode</code> in UK Core STU1 Sequence, to <code>valueCodeableConcept</code>, as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div> 

---
