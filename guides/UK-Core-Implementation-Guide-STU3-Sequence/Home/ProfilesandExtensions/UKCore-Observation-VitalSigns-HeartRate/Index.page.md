---
topic: Observation-VitalSigns-HeartRate
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-VitalSigns-HeartRate
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-VitalSigns-HeartRate
---

# StructureDefinition {{variable:issue}}

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>

This Profile underwent Clinical and Technical Assurance during Sprint 7. This is a new Profile added to UK Core and should undergo review during the Sprint 7 review window.

Click here to <a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-HeartRate/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-HeartRate</a>.
</div>

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Heart Rate</b> - An example to illustrate recording an elevated heart rate.<br/>
{{pagelink:UKCore-Observation-VitalSigns-HeartRate-Example}}<br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation Vital Signs Heart Rate profile:

- Query and retrieve a patient's heart rate
- Record or update a patient's heart rate

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

The UKCore-Observation-VitalSigns-HeartRate profile further derives from {{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} and this page only shows the differences between the two. Refer to {{pagelink:Profile-Observation,text:UKCore-Observation}} and {{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} for more implementation guidance.

### Mandatory and Must Support Data Elements

The following elements, in addition to those of the the corresponding {{pagelink:Profile-Observation,text:UKCore-Observation}} and {{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} parent profiles, are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

<table class="assets" title="MustSupport element list">
<tr>
<th class="width30">Element</th>
<th class="width70">Reason</th>
</tr>
<tr>
<td><code>Observation.value[x]</code></td>
<td>A quantity SHALL be present.</td>
</tr>
</table>
