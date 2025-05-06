---
topic: Profile-Condition
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Condition
usage: http://hl7.org/fhir/StructureDefinition/Condition
issue: UKCore-Condition
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Bleeding From Ear</b> - An example to illustrate a patient bleeding from ear.<br/>
{{pagelink:Example-UKCore-Condition-BleedingFromEar}}
<br/><br/>
<b>CodingSCT DescId</b> - An example to illustrate the extension which adds a SNOMED CT description Id to CodeableConcept.<br/>
{{pagelink:Example-UKCore-Extension-CodingSCTDescId}}
<br/><br/>
<b>Condition Episode</b> - An example to illustrate the extension which is used to indicate the episodicity status of a condition.<br/>
{{pagelink:Example-UKCore-Extension-ConditionEpisode}}
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Condition profile:

- Query for a Patient’s current or historical conditions
- Record or update a Patient’s conditions

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---