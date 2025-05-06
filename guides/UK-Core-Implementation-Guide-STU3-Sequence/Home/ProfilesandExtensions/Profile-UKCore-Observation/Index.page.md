---
topic: Profile-Observation
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>24 hour monitoring</b> - An example to illustrate recording the average blood pressure over 24 hours.<br/>
{{pagelink:Example-UKCore-Observation-24HourBloodPressure}}<br><br>
  <b>Awareness of diagnosis</b> - An example to illustrate the observation of the awareness of a diagnosis.<br/>
{{pagelink:Example-UKCore-Observation-AwarenessOfDiagnosis}}<br><br>
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
<b>Breathing Normally</b> - An example to illustrate a patient breathing room air.<br/>
{{pagelink:Example-UKCore-Observation-BreathingNormally}}<br><br>
  <b>Drug Use</b> - An example to illustrate the observation of patient drug use.<br/>
{{pagelink:Example-UKCore-Observation-DrugUse}}<br><br>
<b>Fasting Test</b> - An example to illustrate recording the blood glucose level following a period of fasting.<br/>
{{pagelink:Example-UKCore-Observation-FastingTest}}<br><br>
<b>Finger Joint Inflammation</b> - An example to illustrate the observation of an inflammed finger joint.<br/>
{{pagelink:Example-UKCore-Observation-FingerJointInflamed}}<br><br>
<b>Full Blood count</b> - An example to illustrate a full blood count using multiple lab observation references.<br/>
{{pagelink:Example-UKCore-Observation-Group-FullBloodCount}}
<b>Head Circumference</b> - An example to illustrate a vital signs head circumference reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-HeadCircumference}}<br><br>
<b>Heart Rate</b> - An example to illustrate a vital signs heart rate reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-HeartRate}}<br><br>
<b>Heavy Drinker</b> - An example to illustrate the alcohol consumption of a heavy drinker.<br/>
{{pagelink:Example-UKCore-Observation-HeavyDrinker}}<br><br>
<b>NEWS2 Bundle</b> - An example to illustrate a full bundle of National Early Warning Score (NEWS) 2 observations, sub scores, and total score.<br/>
{{pagelink:Example-UKCore-Bundle-NEWS2Observations}}<br><br>
<b>NPEWS Total</b> - An example to illustrate a National Paediatric Early Warning System (NPEWS) total score.<br/>
{{pagelink:Example-UKCore-Observation-NPEWSTotal}}<br><br>
<b>Oxygen Saturation</b> - An example to illustrate a vital signs oxygen saturation reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-OxygenSaturation}}<br><br>
<b>Pipe Smoker</b> - An example to illustrate recording a patient who smokes a pipe.<br/>
{{pagelink:Example-UKCore-Observation-PipeSmoker}}<br><br>
<b>Red cell count</b> - An example to illustrate the observation of a red cell count for a blood specimen.<br/>
{{pagelink:Example-UKCore-Observation-Lab-RedCellCount}}<br><br>
<b>Respiratory Rate</b> - An example to illustrate a vital signs respiration rate reading.<br/>
{{pagelink:Example-UKCore-Observation-VitalSigns-RespiratoryRate}}<br><br>
<b>Responds to Voice</b> - An example to illustrate recording a patients level of consiousness.<br/>
{{pagelink:Example-UKCore-Observation-PatientConsciousness}}<br><br>
  <b>Triggered By Drug Use</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to indicate a triggering observation.<br>
  {{pagelink:Example-UKCore-Extension-TriggeredBy}}<br><br>
<b>Using Oxygen Therapy</b> - An example to illustrate a patient on supplemental oxygen.<br/>
{{pagelink:Example-UKCore-Observation-OxygenTherapy}}<br><br>
<b>White cell count</b> - An example to illustrate the observation of a white cell count for a blood specimen.<br/>
{{pagelink:Example-UKCore-Observation-Lab-WhiteCellCount}}<br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Observation profile:

- Query and retrieve a patient's observations
- Record or update a patient's observations

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

The guidance on this page also applies to the following profiles, that are derived from the UK Core Observation profile:
- {{pagelink:Profile-Observation-ACVPU}}
- {{pagelink:Profile-Observation-Alcoholconsumption}}
- {{pagelink:Profile-Observation-AverageBloodPressure}}
- {{pagelink:Profile-Observation-BloodGlucose}}
- {{pagelink:Profile-Observation-EarlyWarningTotalScore}}
- {{pagelink:Profile-Observation-InspiredOxygen}}
- {{pagelink:Profile-Observation-TobaccoConsumption}}

The guidance on this page also applies to the Vital Signs parent profile, and the profiles that are derived from the UK Core Observation Vital Signs profile:
- {{pagelink:Profile-Observation-VitalSigns}}

There are additional Lab related Observation profiles, that are not derived from the UK Core Observation profile:
- {{pagelink:Profile-Observation-Lab}}
- {{pagelink:Profile-Observation-Group-Lab}}

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---
