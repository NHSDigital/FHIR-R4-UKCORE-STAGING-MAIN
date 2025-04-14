---
topic: FamilyMemberHistory
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-FamilyMemberHistory
usage: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
issue: UKCore-FamilyMemberHistory
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Associated Encounter</b> - An example to illustrate using the extension to indicate the encounter for which the family members condition was recorded.<br>
{{pagelink:UKCore-Extension-AssociatedEncounter-Example}}
  <br><br>
  <b>Father with Diabetes</b> - An example to illustrate the the use of FamilyMemberHistory to record a father with diabetes.
  <br>{{pagelink:UKCore-FamilyMemberHistory-FatherDiabetes-Example}}
  <br><br>
  <b>Participant Reference</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to indicate the performer of the family member history related activity.<br>
  {{pagelink:UKCore-Extension-Participant-Example}}
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core FamilyMemberHistory profile:
- Query for details of a FamilyMemberHistory
- Exchange FamilyMemberHistory information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>


---
