---
topic: UKCore-Observation-BloodGlucose
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-BloodGlucose
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-BloodGlucose
---

# StructureDefinition {{variable:issue}}

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>

This Profile underwent Clinical and Technical Assurance during Sprint 7. This is a new Profile added to UK Core and should undergo review during the Sprint 7 review window.

Click here to <a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-BloodGlucose/~issues?level=File">Report Issue for UKCore-Observation-BloodGlucose</a>.
</div>

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Fasting Test</b> - An example to illustrate recording the blood glucose level following a period of fasting.<br/>
{{pagelink:UKCore-Observation-FastingTest-Example}}<br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation Blood Glucose profile:

- Query and retrieve a patient's results of blood glucose tests
- Record or update a patient's blood glucose levels

#### Example for Continuous Glucose Monitoring
A continuous or flash glucose monitor will have an Observation resource created for each individual reading. All readings can be retrieved by searching on the `Observation.subject` and `Observation.device`.

{{render:CGM}}

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
<td>A quantity SHALL be present.</td>
</tr>
</table>
</div>

---
