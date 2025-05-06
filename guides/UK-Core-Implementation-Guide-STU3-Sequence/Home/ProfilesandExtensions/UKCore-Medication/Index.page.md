---
topic: Medication
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Medication
usage: http://hl7.org/fhir/StructureDefinition/Medication
issue: UKCore-Medication
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>

<b>COVID Vaccine</b> - An example to illustrate the batch element.  <br>
{{pagelink:UKCore-Medication-COVID-Vaccine-Example}}   <br><br>
<b>Medication Trade Family</b> - An example to illustrate the Medication Trade Family.  <br>
{{pagelink:UKCore-Extension-MedicationTradeFamily-Example}} <br><br>
<b>Timolol</b> - An example to illustrate the form element with a VTM.  <br>
{{pagelink:UKCore-Medication-TimololVTM-Example}}   <br><br>
<b>Timoptol Eye Drops</b> - An example to illustrate a representation of eye drops.  <br>
{{pagelink:UKCore-Medication-TimoptolEyeDrops-Example}}   <br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios

The UK Core Medication profile will likely not be used in isolation. It does not provide the context for the medication, e.g. the patient or medication related process. It will be typically used as a referenced resource within
- {{pagelink:Profile-MedicationAdministration}}
- {{pagelink:Profile-MedicationDispense}}
- {{pagelink:Profile-MedicationRequest}}
- {{pagelink:Profile-MedicationStatement}}

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---
