---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-VaccinationProcedure
issue: Extension-UKCore-VaccinationProcedure
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-Immunization,text:Immunization}}</td>
</tr>
</table>

{{page:ExtensionTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Vaccination Procedure</b> - An example to illustrate the extension for a vaccination procedure.<br>
   {{pagelink:UKCore-Extension-VaccinationProcedure-Example}}
   <br><br>
   <b>Covid Vaccination Procedure</b> - An example to illustrate the extension for a vaccination procedure for COVID.<br>
   {{pagelink:UKCore-Extension-VaccinationProcedure-Covid-Example}}
   <br><br>
</div>

<h3 id="guidance-vaccinationprocedure">Extension Specific Guidance</h3>

<div markdown="span" class="alert alert-warning" role="alert"><i class="fa fa-info-circle"></i>
Whilst there is a binding within this extension to a {{pagelink:ValueSet-UKCore-VaccinationProcedure}}
, an additional {{pagelink:ValueSet-UKCore-VaccinationProcedureSupplementary}} is available that essentially extends the UKCore-VaccinationProcedure ValueSet with SNOMED CT concepts that some systems may have used in the past on record entries that may also be relevant to the population of the UKCore-VaccinationProcedure extension within Immunization profile instances.
</div>

---
