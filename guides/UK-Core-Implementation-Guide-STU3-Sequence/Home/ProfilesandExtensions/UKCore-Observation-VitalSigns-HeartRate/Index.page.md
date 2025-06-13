---
topic: UKCore-Observation-VitalSigns-HeartRate
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-VitalSigns-HeartRate
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-VitalSigns-HeartRate
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

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

The UKCore-Observation-VitalSigns-HeartRate profile further derives from {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} and this page only shows the differences between the two. Refer to {{pagelink:UKCore-Observation,text:UKCore-Observation}} and {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} for more implementation guidance.

### Mandatory and Must Support Data Elements

The following elements, in addition to those of the the corresponding {{pagelink:UKCore-Observation,text:UKCore-Observation}} and {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} parent profiles, are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

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
