---
topic: UKCore-Observation-VitalSigns-BloodPressure
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-VitalSigns-BloodPressure
usage: http://hl7.org/fhir/StructureDefinition/Observation
---


<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Blood Pressure</b> - An example to illustrate recording a high blood pressure.<br/>
{{pagelink:UKCore-Observation-VitalSigns-BloodPressure-Example}}<br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation Vital Signs Blood Pressure profile:

- Query and retrieve a patient's blood pressure readings
- Record or update a patient's blood pressure readings

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

The UKCore-Observation-VitalSigns-BloodPressure profile further derives from {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} and this page only shows the differences between the two. Refer to {{pagelink:UKCore-Observation,text:UKCore-Observation}} and {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} for more implementation guidance.

An instance of the UKCore-Observation-VitalSigns-BloodPressure resource SHALL have the `Observation.code` element populated, with a LOINC "magic code" and SNOMED CT concept as detailed below. In addition, the individual Systolic and Diastolic readings SHALL be populated in `Observation.component` as detailed below.

<div id="renderParent" title="Blood Pressure Observation structure">
{{render:BloodPressure}}
</div>

### Mandatory and Must Support Data Elements

The following elements, in addition to those of the the corresponding {{pagelink:UKCore-Observation,text:UKCore-Observation}} and {{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}} parent profiles, are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

<table class="assets" title="MustSupport element list">
<tr>
<th class="width30">Element</th>
<th class="width70">Reason</th>
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
<td>A systolic blood pressure measurement SHALL be present, and that SHALL have a LOINC "magic code", in addition to the SNOMED CT concept for the systolic blood pressure observation.
<br>A diastolic blood pressure measurement SHOULD be present, and that SHALL have a LOINC "magic code", in addition to the SNOMED CT concept for the diastolic blood pressure observation.
</td>
</tr>
</table>
</div>

---

