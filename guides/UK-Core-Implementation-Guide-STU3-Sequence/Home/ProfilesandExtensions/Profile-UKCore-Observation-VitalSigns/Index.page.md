---
topic: Profile-Observation-VitalSigns
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation-VitalSigns
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation-VitalSigns
---

# StructureDefinition {{variable:issue}}

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>

This Profile underwent Clinical and Technical Assurance during Sprint 7. This is a new Profile added to UK Core and should undergo review during the Sprint 7 review window.

Click here to <a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns</a>.
</div>

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Blood Pressure</b> - An example to illustrate a vital signs blood pressure reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-BloodPressure}}<br><br>
<b>BMI</b> - An example to illustrate a vital signs body mass index reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-BMI}}<br><br>
<b>Body Height</b> - An example to illustrate a vital signs body height reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-BodyHeight}}<br><br>
<b>Body Temperature</b> - An example to illustrate a vital signs body temperature reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-BodyTemperature}}<br><br>
<b>Body Weight</b> - An example to illustrate a vital signs body weight reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-BodyWeight}}<br><br>
<b>Head Circumference</b> - An example to illustrate a vital signs head circumference reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-HeadCircumference}}<br><br>
<b>Heart Rate</b> - An example to illustrate a vital signs heart rate reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-HeartRate}}<br><br>
<b>Oxygen Saturation</b> - An example to illustrate a vital signs oxygen saturation reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-OxygenSaturation}}<br><br>
<b>Respiratory Rate</b> - An example to illustrate a vital signs respiration rate reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-RespiratoryRate}}<br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###

The following are example usage scenarios for the UK Core Observation Vital Signs profile:

- Query and retrieve a patient's vital signs
- Record or update a patient's vital signs

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

This is a derived profile of {{pagelink:Profile-Observation,text:UKCore-Observation}} and this page only shows the differences between the two. Refer to the base Profile for more implementation guidance.

This guidance is also designed to align with [https://hl7.org/fhir/R4/observation-vitalsigns.html](HL7 Observation Vital Signs guidance) where possible.

The guidance on this page also applies to the following profiles, that are derived from the UK Core Observation Vital Signs profile:
- {{pagelink:Profile-Observation-VitalSigns-BloodPressure}}
- {{pagelink:Profile-Observation-VitalSigns-BMI}}
- {{pagelink:Profile-Observation-VitalSigns-BodyHeight}}
- {{pagelink:Profile-Observation-VitalSigns-BodyTemperature}}
- {{pagelink:Profile-Observation-VitalSigns-BodyWeight}}
- {{pagelink:Profile-Observation-VitalSigns-HeadCircumference}}
- {{pagelink:Profile-Observation-VitalSigns-HeartRate}}
- {{pagelink:Profile-Observation-VitalSigns-OxygenSaturation}}
- {{pagelink:Profile-Observation-VitalSigns-RespirationRate}}

### Mandatory and Must Support Data Elements

The following elements, in addition to those in the corresponding {{pagelink:Profile-Observation,text:UKCore-Observation}} parent profile, are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

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
<td>A category of <code>vital-signs</code> SHALL be present.</td>
</tr>
<tr>
<td><code>Observation.code.coding</code></td>
<td>A LOINC "magic code" SHALL be present, in addition to the SNOMED CT concept for the observation type.</td>
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
<td><code>Observation.component.code.coding</code></td>
<td>If a component is present, a LOINC "magic code" SHALL be present, in addition to the SNOMED CT concept for the observation type.</td>
</tr>
</table>
</div>

---

