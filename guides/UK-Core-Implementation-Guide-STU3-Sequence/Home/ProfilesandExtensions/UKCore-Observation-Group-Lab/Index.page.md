---
topic: UKCore-Observation-Group-Lab
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-Group-Lab
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-Group-Lab
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Full Blood count</b> - An example to illustrate a full blood count using multiple lab observation references.<br/>
{{pagelink:UKCore-Observation-Group-FullBloodCount-Example}}
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###

The following are example usage scenarios for the UK Core Observation profile:

- Group specific laboratory observations together, for example Full Blood Count,
- Place laboratory observations in an ordered fashion.

<br>
The Observation-Group-Lab profile is used to reference multiple individual laboratory observations (Observation-Lab) which together form a larger test set.

The workflow below shows a possible way to group a set of related laboratory observations into the derived {{pagelink:UKCore-Observation-Group-Lab}}, which is then referenced within a diagnostic report. Seperate laboratory observations MAY be directly referenced within the diagnostic report.
<br>

<div id="renderParent" title="Dervied Lab profile structure">
{{render: Derived-Profiles-Lab-Example }}
</div>

<br><br>
Depending upon the countries or trusts workflow, an alternative is to have any separate laboratory observations referenced in a {{pagelink:UKCore-Observation-Group-Lab}} before being referenced in the diagnostic report. Although this creates extra resources it standardises the workflow. 

<div id="renderParent" title="Dervied Lab profile alternative structure">
{{render:Derived-Profiles-Lab-Example-Extra-Group}}
</div>


<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---
