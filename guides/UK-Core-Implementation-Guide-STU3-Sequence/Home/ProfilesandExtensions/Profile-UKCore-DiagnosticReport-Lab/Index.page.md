---
topic: Profile-DiagnosticReport-Lab
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-DiagnosticReport-Lab
usage: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
issue: UKCore-DiagnosticReport-Lab
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Diagnostic Studies Report</b> - An example to illustrate a diagnostic studies report containing a specimen and observation for a patient.<br/>
{{pagelink:Example-UKCore-DiagnosticReport-Lab-DiagnosticStudiesReport}}
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core DiagnosticReport Lab profile:

- Query for a specific patient laboratory test result
- Query for recent laboratory test results
- Record or update a laboratory test result

Services that should consider using the  UK Core DiagnosticReport profile are:

- Lab Result



The DiagnosticReport-Lab profile is expected to reference either:
- a set of laboratory observations (Observation-Lab) that are grouped under one observation (Observation-LabGroup), for example a urea and electrolyte test that contains many sub tests,
- a single laboratory observation (Observation-Lab) that does not form part of a group of tests, for example Serum ferritin level,
- combinations of the above, for example a blood test may include multiple grouped tests such as Urea and electrolytes, Liver function tests, Full blood count, each having a single instance of Observation-LabGroup, along with single tests such as Serum C reactive protein level, eGFR using creatinine and Serum ferritin level, each having a single instance of Observation-Lab.

<br>
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
