---
topic: Profile-Practitioner
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Practitioner
usage: http://hl7.org/fhir/StructureDefinition/Practitioner
issue: UKCore-Practitioner
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>General Practitioner</b> - An example to illustrate a practitioner who is the Patient's GP. 
<br>
{{pagelink:Example-UKCore-Practitioner-DoctorPaulRastall}}
<br><br>
<b>Consultant</b> - An example to illustrate a practitioner who is a Consultant. 
<br>
{{pagelink:Example-UKCore-Practitioner-ConsultantSandraGose}}
<br><br>
<b>Pharmacist</b> - An example to illustrate a practitioner who is a Pharmacist.
<br>
{{pagelink:Example-UKCore-Practitioner-PharmacistJimmyChuck}}
<br><br>
Note: the practitioner's role information is carried in the {{pagelink:Profile-PractitionerRole}}   <br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Practitioner profile:

- Query for practitioner information using the query parameter identifier (`Practitioner.identifier`) for a known SDS User Identifier.
- Exchange practitioner information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---