---
topic: Library-Sprint7Proposals
---
## Profiles

This index contains all the draft assets proposed for Clinical and Technical Assurance Sprint 7 - Clinical Observations, for use with UK Core. 

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Important</h4>

The Profiles are rendered in several formats: 
<ul>
<li><b>Snapshot:</b> a fully calculated form of the structure that is not dependent on any other structure</li>
<li><b>Differential:</b> this describes only the differences that the Profile makes relative to the structure definition (FHIR resource or profile) they constrain</li> 
<li><b>Hybrid:</b> a hybrid view of the snapshot and differential views, with the differences highlighted</li>
<li><b>Table:</b> a differential view of the profile, rendered in a tabular format</li>
<li><b>XML:</b> a differential view of the profile, rendered in XML format</li>
<li><b>JSON:</b> a differential view of the profile, rendered in JSON format</li> 
</ul>
<br>

<a href="https://hl7.org/fhir/R4/profiling.html" class="external">Further information from HL7 relating to profiling is available</a>.

</div>

<h3>Profiles</h3>

<table class="assets">
<tr>
<th class="width25">Profile</th>
<th class="width40">Description</th>
<th class="width35">Report Issue</th>
</tr>
<tr>
<td>{{pagelink:UKCore-Device-BloodPressure,text:UKCore-Device-BloodPressure}}</td>
<td>A profile derived from the draft UK Core Device profile to define the minimal set of data to query and retrieve information regarding the specific blood pressure monitoring device used to record a Blood Pressure observation.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Device-BloodPressure/~issues?level=File">Report Issue for UKCore-Device-BloodPressure</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-ACVPU,text:UKCore-Observation-ACVPU}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's level of consciousness.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-ACVPU/~issues?level=File">Report Issue for UKCore-Observation-ACVPU</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-AlcoholConsumption,text:UKCore-Observation-AlcoholConsumption}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's alcohol consumption.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-AlcoholConsumption/~issues?level=File">Report Issue for UKCore-Observation-AlcoholConsumption</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-AverageBloodPressure,text:UKCore-Observation-AverageBloodPressure}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's average blood pressure over a specific time period.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-AverageBloodPressure/~issues?level=File">Report Issue for UKCore-Observation-AverageBloodPressure</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-BloodGlucose,text:UKCore-Observation-BloodGlucose}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's blood glucose level.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-BloodGlucose/~issues?level=File">Report Issue for UKCore-Observation-BloodGlucose</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-EarlyWarningTotalScore,text:UKCore-Observation-EarlyWarningTotalScore}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's Early Warning Score, such as NEWS2.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-EarlyWarningTotalScore/~issues?level=File">Report Issue for UKCore-Observation-EarlyWarningTotalScore</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-InspiredOxygen,text:UKCore-Observation-InspiredOxygen}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding whether a patient is breathing room air or is on oxygen.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-InspiredOxygen/~issues?level=File">Report Issue for UKCore-Observation-InspiredOxygen</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-TobaccoConsumption,text:UKCore-Observation-TobaccoConsumption}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's tobacco consumption.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-TobaccoConsumption/~issues?level=File">Report Issue for UKCore-Observation-TobaccoConsumption</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}}</td>
<td>A profile derived from the UK Core Observation profile to define the minimal set of data to query and retrieve information of a patient's Vital Signs measurements, in order to be FHIR compliant with the base "Vital Signs" guidance.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-BloodPressure,text:UKCore-Observation-VitalSigns-BloodPressure}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a single instance of a patient's blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-BloodPressure/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-BloodPressure</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-BMI,text:UKCore-Observation-VitalSigns-BMI}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's body mass index.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-BMI/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-BMI</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-BodyHeight,text:UKCore-Observation-VitalSigns-BodyHeight}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's height.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-BodyHeight/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-BodyHeight</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-BodyTemperature,text:UKCore-Observation-VitalSigns-BodyTemperature}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's temperature.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-BodyTemperature</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-BodyWeight,text:UKCore-Observation-VitalSigns-BodyWeight}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's weight.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-BodyTemperature/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-BodyWeight</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-HeadCircumference,text:UKCore-Observation-VitalSigns-HeadCircumference}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's head circumference.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-HeadCircumference/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-HeadCircumference</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-HeartRate,text:UKCore-Observation-VitalSigns-HeartRate}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's heart rate.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-HeartRate/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-HeartRate</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-OxygenSaturation,text:UKCore-Observation-VitalSigns-OxygenSaturation}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's level of oxygen saturation in their blood.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-OxygenSaturation/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-OxygenSaturation</td>
</tr>
<tr>
<td>{{pagelink:UKCore-Observation-VitalSigns-RespirationRate,text:UKCore-Observation-VitalSigns-RespirationRate}}</td>
<td>A profile derived from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's breathing rate.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/UKCore-Observation-VitalSigns-RespirationRate/~issues?level=File">Report Issue for UKCore-Observation-VitalSigns-RespirationRate</td>
</tr>
</table>

<h3>Extensions</h3>

<table class="assets">
<tr>
<th class="width25">Extension</th>
<th class="width40">Description</th>
<th class="width35">Report Issue</th>
</tr>
<tr>
<td>{{pagelink:Extension-UKCore-CuffSize,text:Extension-UKCore-CuffSize}}</td>
<td>An extension on the {{pagelink:UKCore-Device-BloodPressure}} to record the cuff size used on the device which was used to monitor the patient's blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/Extension-UKCore-CuffSize/~issues?level=File">Report Issue for Extension-UKCore-CuffSize</td>
</tr>
<tr>
<td>{{pagelink:Extension-UKCore-RecordingSetting,text:Extension-UKCore-RecordingSetting}}</td>
<td>An extension on the {{pagelink:UKCore-Observation-VitalSigns}} to record the setting in which the observation was made.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/Extension-UKCore-RecordingSetting/~issues?level=File">Report Issue for Extension-UKCore-RecordingSetting</td>
</tr>
<tr>
<td><a href="http://hl7.org/fhir/R4/extension-observation-bodyposition.html">observation-bodyPosition</a></td>
<td>A HL7 core-defined extension, on the {{pagelink:UKCore-Observation-VitalSigns}}, to record the body position at the time an observation was made. This has a binding to {{pagelink:ValueSet-UKCore-BodyPosition}}.</td>
<td></td>
</tr>
</table>

<h3>CodeSystems</h3>

<table class="assets">
<tr>
<th class="width25">CodeSystem</th>
<th class="width40">Description</th>
<th class="width35">Report Issue</th>
</tr>
<tr>
<td>{{pagelink:CodeSystem-UKCore-RecordingSetting,text:CodeSystem-UKCore-RecordingSetting}}</td>
<td>A CodeSystem to state if the observation was taken in a residential or a clinical setting.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/CodeSystem-UKCore-RecordingSetting/~issues?level=File">Report Issue for CodeSystem-UKCore-RecordingSetting</td>
</tr>
</table>


<h3>ValueSets</h3>

<table class="assets">
<tr>
<th class="width25">ValueSet</th>
<th class="width40">Description</th>
<th class="width35">Report Issue</th>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-ACVPU,text:ValueSet-UKCore-ACVPU}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's level of consciousness.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-ACVPU/~issues?level=File">Report Issue for ValueSet-UKCore-ACVPU</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-AlcoholConsumption,text:ValueSet-UKCore-AlcoholConsumption}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's level of alcohol consumption.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-AlcoholConsumption/~issues?level=File">Report Issue for ValueSet-UKCore-AlcoholConsumption</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodGlucose,text:ValueSet-UKCore-BloodGlucose}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's level of blood sugar.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodGlucose/~issues?level=File">Report Issue for ValueSet-UKCore-BloodGlucose</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure,text:ValueSet-UKCore-BloodPressure}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a panel of the patient's systolic and diastolic blood pressure readings.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-Average,text:ValueSet-UKCore-BloodPressure-Average}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a panel of the patient's average systolic and diastolic blood pressure readings.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-Average/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-Average</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-AverageDiastolic,text:ValueSet-UKCore-BloodPressure-AverageDiastolic}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's average diastolic blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-AverageDiastolic/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-AverageDiastolic</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-AverageSystolic,text:ValueSet-UKCore-BloodPressure-AverageSystolic}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's average systolic blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-AverageSystolic/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-AverageSystolic</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-CuffSize,text:ValueSet-UKCore-BloodPressure-CuffSize}}</td>
<td>A ValueSet of SNOMED CT concepts used to record the cuff size on a blood pressure monitoring device.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-CuffSize/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-CuffSize</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-DeviceType,text:ValueSet-UKCore-BloodPressure-DeviceType}}</td>
<td>A ValueSet of SNOMED CT concepts used to record the type of blood pressure monitoring device.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-DeviceType/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-DeviceType</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-Diastolic,text:ValueSet-UKCore-BloodPressure-Diastolic}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's diastolic blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-Diastolic/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-Diastolic</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-MeasurementMethod,text:ValueSet-UKCore-BloodPressure-MeasurementMethod}}</td>
<td>A ValueSet of SNOMED CT concepts used to record the method used to measure a patient's blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-MeasurementMethod/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-MeasurementMethod</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BloodPressure-Systolic,text:ValueSet-UKCore-BloodPressure-Systolic}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's systolic blood pressure.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BloodPressure-Systolic/~issues?level=File">Report Issue for ValueSet-UKCore-BloodPressure-Systolic</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BMI,text:ValueSet-UKCore-BMI}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's body mass index.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BMI/~issues?level=File">Report Issue for ValueSet-UKCore-BMI</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BodyHeightMeasurements,text:ValueSet-UKCore-BodyHeightMeasurements}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's height.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BodyHeightMeasurements/~issues?level=File">Report Issue for ValueSet-UKCore-BodyHeightMeasurements</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BodyPosition,text:ValueSet-UKCore-BodyPosition}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's body position when an observation was made.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BodyPosition/~issues?level=File">Report Issue for ValueSet-UKCore-BodyPosition</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BodyTemperature,text:ValueSet-UKCore-BodyTemperature}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's temperature.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BodyTemperature/~issues?level=File">Report Issue for ValueSet-UKCore-BodyTemperature</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-BodyWeightMeasurements,text:ValueSet-UKCore-BodyWeightMeasurements}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's weight.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-BodyWeightMeasurements/~issues?level=File">Report Issue for ValueSet-UKCore-BodyWeightMeasurements</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-DeviceType,text:ValueSet-UKCore-DeviceType}}</td>
<td>A ValueSet of SNOMED CT concepts used to record the type of device.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-DeviceType/~issues?level=File">Report Issue for ValueSet-UKCore-DeviceType</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-EarlyWarningTotalScore,text:ValueSet-UKCore-EarlyWarningTotalScore}}</td>
<td>A ValueSet of SNOMED CT concepts used to record the total of an Early Warning Score.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-EarlyWarningTotalScore/~issues?level=File">Report Issue for ValueSet-UKCore-EarlyWarningTotalScore</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-EarlyWarningSubScore,text:ValueSet-UKCore-EarlyWarningSubScore}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a sub score of an Early Warning Score.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-EarlyWarningSubScore/~issues?level=File">Report Issue for ValueSet-UKCore-EarlyWarningSubScore</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-HeadCircumferenceMeasurements,text:ValueSet-UKCore-HeadCircumferenceMeasurements}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's head circumference.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-HeadCircumferenceMeasurements/~issues?level=File">Report Issue for ValueSet-UKCore-HeadCircumferenceMeasurements</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-HeartRate,text:ValueSet-UKCore-HeartRate}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's heart rate.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-HeartRate/~issues?level=File">Report Issue for ValueSet-UKCore-HeartRate</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-InspiredOxygen,text:ValueSet-UKCore-InspiredOxygen}}</td>
<td>A ValueSet of SNOMED CT concepts used to record if a patient is breathing room air, or on oxygen.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-InspiredOxygen/~issues?level=File">Report Issue for ValueSet-UKCore-InspiredOxygen</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-ObservationVitalSignsType,text:ValueSet-UKCore-ObservationVitalSignsType}}</td>
<td>A ValueSet of SNOMED CT concepts used to record the type of vital signs observation.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-ObservationVitalSignsType/~issues?level=File">Report Issue for ValueSet-UKCore-ObservationVitalSignsType</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-OxygenSaturation,text:ValueSet-UKCore-OxygenSaturation}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's oxygen saturation.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-OxygenSaturation/~issues?level=File">Report Issue for ValueSet-UKCore-OxygenSaturation</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-RecordingSetting,text:ValueSet-UKCore-RecordingSetting}}</td>
<td>A ValueSet from {{pagelink:ValueSet-UKCore-RecordingSetting}} to record if a observation was recorded at home or in a clinical setting.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-RecordingSetting/~issues?level=File">Report Issue for ValueSet-UKCore-RecordingSetting</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-RespirationRate,text:ValueSet-UKCore-RespirationRate}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's breathing rate.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-RespirationRate/~issues?level=File">Report Issue for ValueSet-UKCore-RespirationRate</td>
</tr>
<tr>
<td>{{pagelink:ValueSet-UKCore-TobaccoConsumption,text:ValueSet-UKCore-TobaccoConsumption}}</td>
<td>A ValueSet of SNOMED CT concepts used to record a patient's tobacco consumption.</td>
<td><a href="https://simplifier.net/HL7FHIRUKCoreR4/ValueSet-UKCore-TobaccoConsumption/~issues?level=File">Report Issue for ValueSet-UKCore-TobaccoConsumption</td>
</tr>
</table>