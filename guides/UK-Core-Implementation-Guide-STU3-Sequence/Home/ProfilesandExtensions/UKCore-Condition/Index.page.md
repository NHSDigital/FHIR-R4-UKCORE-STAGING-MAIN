---
topic: UKCore-Condition
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Condition
usage: http://hl7.org/fhir/StructureDefinition/Condition
issue: UKCore-Condition
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Bleeding From Ear</b> - An example to illustrate a patient bleeding from ear.<br/>
{{pagelink:UKCore-Condition-BleedingFromEar-Example}}
<br/><br/>
<b>CodingSCT DescId</b> - An example to illustrate the extension which adds a SNOMED CT description Id to CodeableConcept.<br/>
{{pagelink:UKCore-Extension-CodingSCTDescId-Example}}
<br/><br/>
<b>Condition Episode</b> - An example to illustrate the extension which is used to indicate the episodicity status of a condition.<br/>
{{pagelink:UKCore-Extension-ConditionEpisode-Example}}
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Condition profile:

- Query for a Patient’s current or historical conditions
- Record or update a Patient’s conditions

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---