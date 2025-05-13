---
topic: UKCore-Observation-ACVPU
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-ACVPU
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-ACVPU
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Responds to Voice</b> - An example to illustrate recording a patients level of consiousness.<br/>
{{pagelink:UKCore-Observation-PatientConsciousness-Example}}<br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation ACVPU profile:

- Query and retrieve a patient's level of consciousness
- Record or update a patient's level of consciousness

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

This is a derived profile of {{pagelink:UKCore-Observation,text:UKCore-Observation}} and this page only shows the differences between the two. Refer to the base Profile for more implementation guidance.

### Mandatory and Must Support Data Elements

The following elements, in addition to those in the corresponding {{pagelink:UKCore-Observation,text:UKCore-Observation}} parent profile, are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

<table class="assets" title="MustSupport element list">
<tr>
<th class="width30">Element</th>
<th class="width70">Reason</th>
</tr>
<tr>
<td><code>Observation.status</code></td>
<td>A status of <code>final</code> SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.category</code></td>
<td>A category SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.code</code></td>
<td>A SNOMED CT concept SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.subject</code></td>
<td>A UKCore-Patient SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.effective[x]</code></td>
<td>An effective time or date SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.value[x]</code></td>
<td>A SNOMED CT concept for the level of consciousness SHALL be present.</td>
</tr>
</table>

</div>

---
