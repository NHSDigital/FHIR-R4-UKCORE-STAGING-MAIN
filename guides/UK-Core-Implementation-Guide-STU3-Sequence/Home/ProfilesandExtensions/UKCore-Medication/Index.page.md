---
topic: UKCore-Medication
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Medication
usage: http://hl7.org/fhir/StructureDefinition/Medication
---

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>

<b>COVID Vaccine</b> - An example to illustrate the batch element.  <br>
{{pagelink:UKCore-Medication-COVID-Vaccine-Example}}   <br><br>
<b>Medication Trade Family</b> - An example to illustrate the Medication Trade Family.  <br>
{{pagelink:Extension-UKCore-MedicationTradeFamily-Example}} <br><br>
<b>Timolol</b> - An example to illustrate the form element with a VTM.  <br>
{{pagelink:UKCore-Medication-TimololVTM-Example}}   <br><br>
<b>Timoptol Eye Drops</b> - An example to illustrate a representation of eye drops.  <br>
{{pagelink:UKCore-Medication-TimoptolEyeDrops-Example}}   <br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios

The UK Core Medication profile will likely not be used in isolation. It does not provide the context for the medication, e.g. the patient or medication related process. It will be typically used as a referenced resource within
- {{pagelink:UKCore-MedicationAdministration}}
- {{pagelink:UKCore-MedicationDispense}}
- {{pagelink:UKCore-MedicationRequest}}
- {{pagelink:UKCore-MedicationStatement}}

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---
