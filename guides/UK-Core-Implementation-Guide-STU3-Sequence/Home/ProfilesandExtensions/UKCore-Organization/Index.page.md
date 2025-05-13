---
topic: UKCore-Organization
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Organization
usage: http://hl7.org/fhir/StructureDefinition/Organization
issue: UKCore-Organization
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>General Practice</b> - Example to illustrate a General Practice organisation.
</br>{{pagelink:UKCore-Organization-WhiteRoseMedicalCentre-Example}}   <br><br>

<b>Hospital</b> - Example to illustrate a Hospital organisation.
</br>{{pagelink:UKCore-Organization-LeedsTeachingHospital-Example}}   <br><br>

<b>Main Location</b> - Example to illustrate the mainLocation extension.
</br>{{pagelink:UKCore-Extension-MainLocation-Example}}   <br><br>

<b>Organization Period</b> - Example to illustrate the core-defined organization-period extension.
</br>{{pagelink:UKCore-Extension-OrganizationPeriod-Example}}
</div>

</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###

- Query for organisation information using the query parameter identifier `Organization.identifier` for a known ODS code.
- Exchange organisation information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---