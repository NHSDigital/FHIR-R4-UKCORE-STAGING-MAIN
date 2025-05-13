---
topic: UKCore-Observation
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Observation
usage: http://hl7.org/fhir/StructureDefinition/Observation
issue: UKCore-Observation
---

# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>24 hour monitoring</b> - An example to illustrate recording the average blood pressure over 24 hours.<br/>
{{pagelink:UKCore-Observation-24HourBloodPressure-Example}}<br><br>
  <b>Awareness of diagnosis</b> - An example to illustrate the observation of the awareness of a diagnosis.<br/>
{{pagelink:UKCore-Observation-AwarenessOfDiagnosis-Example}}<br><br>
<b>Blood Pressure</b> - An example to illustrate a vital signs blood pressure reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-BloodPressure-Example}}<br><br>
<b>BMI</b> - An example to illustrate a vital signs body mass index reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-BMI-Example}}<br><br>
<b>Body Height</b> - An example to illustrate a vital signs body height reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-BodyHeight-Example}}<br><br>
<b>Body Temperature</b> - An example to illustrate a vital signs body temperature reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-BodyTemperature-Example}}<br><br>
<b>Body Weight</b> - An example to illustrate a vital signs body weight reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-BodyWeight-Example}}<br><br>
<b>Breathing Normally</b> - An example to illustrate a patient breathing room air.<br/>
{{pagelink:UKCore-Observation-BreathingNormally-Example}}<br><br>
  <b>Drug Use</b> - An example to illustrate the observation of patient drug use.<br/>
{{pagelink:UKCore-Observation-DrugUse-Example}}<br><br>
<b>Fasting Test</b> - An example to illustrate recording the blood glucose level following a period of fasting.<br/>
{{pagelink:UKCore-Observation-FastingTest-Example}}<br><br>
<b>Finger Joint Inflammation</b> - An example to illustrate the observation of an inflammed finger joint.<br/>
{{pagelink:UKCore-Observation-FingerJointInflamed-Example}}<br><br>
<b>Full Blood count</b> - An example to illustrate a full blood count using multiple lab observation references.<br/>
{{pagelink:UKCore-Observation-Group-FullBloodCount-Example}}
<b>Head Circumference</b> - An example to illustrate a vital signs head circumference reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-HeadCircumference-Example}}<br><br>
<b>Heart Rate</b> - An example to illustrate a vital signs heart rate reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-HeartRate-Example}}<br><br>
<b>Heavy Drinker</b> - An example to illustrate the alcohol consumption of a heavy drinker.<br/>
{{pagelink:UKCore-Observation-HeavyDrinker-Example}}<br><br>
<b>NEWS2 Bundle</b> - An example to illustrate a full bundle of National Early Warning Score (NEWS) 2 observations, sub scores, and total score.<br/>
{{pagelink:UKCore-Bundle-NEWS2Observations-Example}}<br><br>
<b>NPEWS Total</b> - An example to illustrate a National Paediatric Early Warning System (NPEWS) total score.<br/>
{{pagelink:UKCore-Observation-NPEWSTotal-Example}}<br><br>
<b>Oxygen Saturation</b> - An example to illustrate a vital signs oxygen saturation reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-OxygenSaturation-Example}}<br><br>
<b>Pipe Smoker</b> - An example to illustrate recording a patient who smokes a pipe.<br/>
{{pagelink:UKCore-Observation-PipeSmoker-Example}}<br><br>
<b>Red cell count</b> - An example to illustrate the observation of a red cell count for a blood specimen.<br/>
{{pagelink:UKCore-Observation-Lab-RedCellCount-Example}}<br><br>
<b>Respiratory Rate</b> - An example to illustrate a vital signs respiration rate reading.<br/>
{{pagelink:UKCore-Observation-VitalSigns-RespiratoryRate-Example}}<br><br>
<b>Responds to Voice</b> - An example to illustrate recording a patients level of consiousness.<br/>
{{pagelink:UKCore-Observation-PatientConsciousness-Example}}<br><br>
  <b>Triggered By Drug Use</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to indicate a triggering observation.<br>
  {{pagelink:UKCore-Extension-TriggeredBy-Example}}<br><br>
<b>Using Oxygen Therapy</b> - An example to illustrate a patient on supplemental oxygen.<br/>
{{pagelink:UKCore-Observation-OxygenTherapy-Example}}<br><br>
<b>White cell count</b> - An example to illustrate the observation of a white cell count for a blood specimen.<br/>
{{pagelink:UKCore-Observation-Lab-WhiteCellCount-Example}}<br><br>
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
- {{pagelink:UKCore-Observation-ACVPU}}
- {{pagelink:UKCore-Observation-Alcoholconsumption}}
- {{pagelink:UKCore-Observation-AverageBloodPressure}}
- {{pagelink:UKCore-Observation-BloodGlucose}}
- {{pagelink:UKCore-Observation-EarlyWarningTotalScore}}
- {{pagelink:UKCore-Observation-InspiredOxygen}}
- {{pagelink:UKCore-Observation-TobaccoConsumption}}

The guidance on this page also applies to the Vital Signs parent profile, and the profiles that are derived from the UK Core Observation Vital Signs profile:
- {{pagelink:UKCore-Observation-VitalSigns}}

There are additional Lab related Observation profiles, that are not derived from the UK Core Observation profile:
- {{pagelink:UKCore-Observation-Lab}}
- {{pagelink:UKCore-Observation-Group-Lab}}

{{page:ProfileMustSupportTemplate}}

</div>

---
