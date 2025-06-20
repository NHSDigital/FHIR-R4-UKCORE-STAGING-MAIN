---
subject: http://hl7.org/fhir/5.0/StructureDefinition/extension-FamilyMemberHistory.participant
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-FamilyMemberHistory,text:FamilyMemberHistory}}</td>
</tr>
</table>

{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Participant Reference</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to indicate the performer of the family member history related activity.<br>
  {{pagelink:Extension-UKCore-Participant-Example}}
  <br><br>
</div>

<h3 id="guidance-fmhparticipant">Extension Specific Guidance</h3>

Where possible, it is expected that the resource being referenced SHOULD conform to one of the following UK Core profiles:

- [UKCore-CareTeam](https://simplifier.net/guide/ukcoreimplementationguideassetsindevelopment/home/profilesandextensions/profile-ukcore-careteam)
- [UKCore-Device](https://simplifier.net/guide/UKCoreImplementationGuideAssetsinDevelopment/Home/ProfilesandExtensions/Profile-UKCore-Device)
- {{pagelink:UKCore-Organization}}
- {{pagelink:UKCore-Patient}}
- {{pagelink:UKCore-Practitioner}}
- {{pagelink:UKCore-PractitionerRole}}
- {{pagelink:UKCore-RelatedPerson}}


---