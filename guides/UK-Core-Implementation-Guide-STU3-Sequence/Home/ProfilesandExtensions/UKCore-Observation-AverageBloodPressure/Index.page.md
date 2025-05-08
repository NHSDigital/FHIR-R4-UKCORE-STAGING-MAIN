---
topic: UKCore-Observation-AverageBloodPressure
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-AverageBloodPressure
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-AverageBloodPressure
---

# StructureDefinition {{variable:issue}}

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>

This Profile underwent Clinical and Technical Assurance during Sprint 7. This is a new Profile added to UK Core and should undergo review during the Sprint 7 review window.

Click here to <a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-AverageBloodPressure/~issues?level=File">Report Issue for UKCore-Observation-AverageBloodPressure</a>.
</div>

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>24 hour monitoring</b> - An example to illustrate recording the average blood pressure over 24 hours.<br/>
{{pagelink:UKCore-Observation-24HourBloodPressure-Example}}<br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation Average Blood Pressure profile:

- Query and retrieve a patient's average blood pressure over a specific time period
- Record or update a patient's average blood pressure over a specific time period

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
<td>An effective date/time, or period SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.device</code></td>
<td>A device SHOULD be present.</td>
</tr>
<tr>
<td><code>Observation.method</code></td>
<td>A measurement method SHOULD be present.</td>
</tr>
<tr>
<td><code>Observation.component.code.coding</code></td>
<td>An average systolic blood pressure measurement SHALL be present, and that SHALL have a SNOMED CT concept for the systolic blood pressure observation.
<br>An average diastolic blood pressure measurement SHOULD be present, and that SHALL have a SNOMED CT concept for the diastolic blood pressure observation.
</td>
</tr>
</table>
</div>

---

