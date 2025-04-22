---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-CodingSCTDescDisplay
issue: Extension-UKCore-CodingSCTDescDisplay
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>Coding</td>
</tr>
</table>

{{page:Home/ProfilesandExtensions/ExtensionTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Coding SNOMED CT Description Id</b>- An example to illustrate the extension of adding a SNOMED CT description Id and display Term.<br>
{{pagelink:UKCore-Extension-CodingSCTDescId-Example}}
<br><br>
</div>

<h3 id="guidance-codingsctdescdisplay">Extension Specific Guidance</h3>

This extension is used alongside the HL7 core-defined <a href="https://hl7.org/fhir/R4/extension-coding-sctdescid.html" class="external">coding-sctdescid</a> to support the exchange of the selected description display term for a SNOMED CT concept, where the selected display term is different to the preferred term. Specific guidance on the usage of this extension can be found within the {{pagelink:Guidance-CodeableConcept}}

---