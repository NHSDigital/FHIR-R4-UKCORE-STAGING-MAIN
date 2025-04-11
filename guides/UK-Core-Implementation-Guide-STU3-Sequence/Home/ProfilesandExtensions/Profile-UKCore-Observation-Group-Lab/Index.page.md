---
topic: Profile-Observation-Group-Lab
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-Group-Lab
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-Group-Lab
---

# StructureDefinition {{variable:issue}}

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The <code>id</code> / <code>title</code> / <code>name</code> / <code>url</code> of this profile were changed in the STU2 Sequence release, as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div>

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Full Blood count</b> - An example to illustrate a full blood count using multiple lab observation references.<br/>
{{pagelink:Example-UKCore-Observation-Group-FullBloodCount}}
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###

The following are example usage scenarios for the UK Core Observation profile:

- Group specific laboratory observations together, for example Full Blood Count,
- Place laboratory observations in an ordered fashion.

<br>
The Observation-Group-Lab profile is used to reference multiple individual laboratory observations (Observation-Lab) which together form a larger test set.

The workflow below shows a possible way to group a set of related laboratory observations into the derived {{pagelink:Profile-Observation-Group-Lab}}, which is then referenced within a diagnostic report. Seperate laboratory observations MAY be directly referenced within the diagnostic report.
<br>

<div id="renderParent" title="Dervied Lab profile structure">
{{render: Derived-Profiles-Lab-Example }}
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
