---
subject: http://hl7.org/fhir/5.0/StructureDefinition/extension-Specimen.collection.collector
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-Specimen,text:Specimen}}</td>
</tr>
</table>

{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Composition Reference</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to reference a Patient or RelatedPerson within Specimen.collection.collector.<br>
  {{pagelink:Extension-UKCore-SpecimenCollectionCollector-Example}}
  <br><br>
</div>

<h3 id="guidance-specimencollectioncollector">Extension Specific Guidance</h3>

Where possible, it is expected that the resource being referenced SHOULD conform to one of the following UK Core profiles:

- {{pagelink:UKCore-Patient}}
- {{pagelink:UKCore-RelatedPerson}}


---