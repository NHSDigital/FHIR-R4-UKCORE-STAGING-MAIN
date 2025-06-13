---
topic: UKCore-Observation-EarlyWarningTotalScore
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-EarlyWarningTotalScore
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-EarlyWarningTotalScore
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>NEWS2 Bundle</b> - An example to illustrate a full bundle of National Early Warning Score (NEWS) 2 observations, sub scores, and total score.<br/>
{{pagelink:UKCore-Bundle-NEWS2Observations-Example}}<br><br>
<b>NPEWS Total</b> - An example to illustrate a National Paediatric Early Warning System (NPEWS) total score.<br/>
{{pagelink:UKCore-Observation-NPEWSTotal-Example}}<br><br>
</div>
</nocheck>

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation Early Warning Total Score profile:

- Query and retrieve a patient's Early Warning Score
- Record or update a patient's Early Warning Score


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
<td>A category of <code>survey</code> SHALL be present.</td>
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
<td>A quantity SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.derivedFrom</code></td>
<td>References to the observations from which the component scores are derived SHOULD be present.</td>
</tr>
<tr>
<td><code>Observation.component</code></td>
<td>Components representing the codes and sub scores SHOULD be present.</td>
</tr>
</table>

---