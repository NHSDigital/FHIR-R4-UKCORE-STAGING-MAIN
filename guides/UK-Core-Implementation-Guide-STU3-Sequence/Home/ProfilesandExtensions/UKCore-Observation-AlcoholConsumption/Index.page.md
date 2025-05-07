---
topic: UKCore-Observation-AlcoholConsumption
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-AlcoholConsumption
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-AlcoholConsumption
---

# StructureDefinition {{variable:issue}}

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>

This Profile underwent Clinical and Technical Assurance during Sprint 7. This is a new Profile added to UK Core and should undergo review during the Sprint 7 review window.

Click here to <a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-AlcoholConsumption/~issues?level=File">Report Issue for UKCore-Observation-AlcoholConsumption</a>.
</div>

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Heavy Drinker</b> - An example to illustrate the alcohol consumption of a heavy drinker.<br/>
{{pagelink:UKCore-Observation-HeavyDrinker-Example}}<br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios 
The following are example usage scenarios for the UK Core Observation Alcohol Consumption profile:

- Query and retrieve a patient's alcohol consumption
- Record or update a patient's alcohol consumption

<hr class="thickline">

## Profile Specific Implementation Guidance: 

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
<td>A category of <code>social-history</code> SHALL be present.</td>
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
