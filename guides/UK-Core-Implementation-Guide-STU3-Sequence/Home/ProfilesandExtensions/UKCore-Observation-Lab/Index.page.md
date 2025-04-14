---
topic: Profile-Observation-Lab
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-Lab
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-Lab
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation profile:

- Query and retrieve a patient's laboratory observations
- Record or update a patient's laboratory observations

<br>
The Observation-Lab profile is for individual laboratory tests (Observation-Lab) which may form a larger set of tests, for example a urea and electrolyte test that contains many sub tests, or as a single test, for example Serum ferritin level.
<br><br>
The workflow below shows a possible way to group a set of related laboratory observations into the derived {{pagelink:Profile-Observation-Group-Lab}}, which is then referenced within a diagnostic report. Seperate laboratory observations MAY be directly referenced within the diagnostic report.
<br>

<div id="renderParent" title="Dervied Lab profile structure">
{{render:Derived-Profiles-Lab-Example}}
</div>

<br><br>
Depending upon the countries or trusts workflow, an alternative is to have any separate laboratory observations referenced in a {{pagelink:Profile-Observation-Group-Lab}} before being referenced in the diagnostic report. Although this creates extra resources it standardises the workflow. 

<div id="renderParent" title="Dervied Lab profile alternative structure">
{{render:Derived-Profiles-Lab-Example-Extra-Group}}
</div>


<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---

