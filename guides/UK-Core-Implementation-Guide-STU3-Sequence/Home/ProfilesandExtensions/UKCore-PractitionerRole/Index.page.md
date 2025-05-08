---
topic: UKCore-PractitionerRole
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-PractitionerRole
usage: http://hl7.org/fhir/StructureDefinition/PractitionerRole
issue: UKCore-PractitionerRole
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Patient's GP</b>- An example to illustrate the role of General Practitioner.
<br>
{{pagelink:UKCore-PractitionerRole-GP-Example}}
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core PractitionerRole profile:

- Query for a Practitioner role using the query parameter identifier `PractitionerRole.identifier` for a known SDS Role Id.
- Query for a Practitioner using query parameters such as specialty `PractitionerRole.specialty` for a known specialty.
- Exchange Practitioner role information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---