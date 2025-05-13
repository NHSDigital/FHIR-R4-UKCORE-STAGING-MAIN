---
topic: UKCore-Observation-VitalSigns-OxygenSaturation
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-VitalSigns-OxygenSaturation
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-VitalSigns-OxygenSaturation
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Oxygen Saturation</b> - An example to illustrate recording a patients blood oxygen saturation.<br/>
{{pagelink:UKCore-Observation-VitalSigns-OxygenSaturation-Example}}<br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation Vital Signs Oxygen Saturation profile:

- Query and retrieve a patient's blood oxygen saturation level
- Record or update a patient's percentage of oxygen in their blood

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

The UKCore-Observation-VitalSigns-OxygenSaturation profile further derives from {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} and this page only shows the differences between the two. Refer to {{pagelink:UKCore-Observation,text:UKCore-Observation}} and {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} for more implementation guidance.

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
</div>

---