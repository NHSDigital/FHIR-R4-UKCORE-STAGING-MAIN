---
topic: UKCore-Practitioner
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Practitioner
usage: http://hl7.org/fhir/StructureDefinition/Practitioner
issue: UKCore-Practitioner
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>General Practitioner</b> - An example to illustrate a practitioner who is the Patient's GP. 
<br>
{{pagelink:UKCore-Practitioner-DoctorPaulRastall-Example}}
<br><br>
<b>Consultant</b> - An example to illustrate a practitioner who is a Consultant. 
<br>
{{pagelink:UKCore-Practitioner-ConsultantSandraGose-Example}}
<br><br>
<b>Pharmacist</b> - An example to illustrate a practitioner who is a Pharmacist.
<br>
{{pagelink:UKCore-Practitioner-PharmacistJimmyChuck-Example}}
<br><br>
Note: the practitioner's role information is carried in the {{pagelink:UKCore-PractitionerRole}}   <br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Practitioner profile:

- Query for practitioner information using the query parameter identifier (`Practitioner.identifier`) for a known SDS User Identifier.
- Exchange practitioner information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---