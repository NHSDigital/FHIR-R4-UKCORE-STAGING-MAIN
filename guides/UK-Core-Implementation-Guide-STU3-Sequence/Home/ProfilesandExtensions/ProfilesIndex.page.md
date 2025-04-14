---
topic: Library-Profiles
---
## Profiles and Extensions

---

## Profiles Index

This index contains all the profiles Clinically and Technically Assured for use with UK Core. 

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Important</h4>

The Profiles are rendered in several formats: 
<ul>
<li><b>Tree View - Snapshot:</b> a fully calculated tree view of the structure that is not dependent on any other structure</li>
<li><b>Tree View - Differential:</b> this tree view describes only the differences that the Profile makes relative to the structure definition (FHIR resource or profile) they constrain</li> 
<li><b>Tree View - Hybrid:</b> a hybrid view of the snapshot and differential views, with the differences highlighted</li>
<li><b>Detailed View:</b> a fully calculated form of the profile in table form</li>
<li><b>Table View:</b> a differential view of the profile, rendered in a tabular format</li>
<li><b>XML View:</b> a differential view of the profile, rendered in XML format</li>
<li><b>JSON View:</b> a differential view of the profile, rendered in JSON format</li> 
</ul>
In addition, each Profile also has the following: 
<ul>
<!--<li><b>Usage:</b> a listing of extensions and profiles that reference this asset</li>-->
<li><b>Examples:</b> one or more validated example of the profile in use</li>
<li><b>Feedback:</b> a link to Simplifier to raise issues regarding the asset</li> 
</ul>
<br>

<a href="https://hl7.org/fhir/R4/profiling.html" class="external">Further information from HL7 relating to profiling is available</a>.

</div>

<div class="tab">
<button class="tablinks active" onclick="openTab(event, 'Narrative')">Narrative</button>
<button class="tablinks" onclick="openTab(event, 'Alphabetical')">Alphabetical</button>
<button class="tablinks" onclick="openTab(event, 'Sprint')">By Sprint</button>
<button class="tablinks" onclick="openTab(event, 'Resource')">By Resource</button>
</div>

<div id="Narrative" class="tabcontent"  style="display:block">
<h3>Narrative Listing</h3>

<table title="Profile" class="assets">
<tr>
<th class="width25">Profile</th>
<th class="width10">Status</th>
<th class="width45">Description</th>
<th class="width10">C&TA Sprint</th>
</tr>
<tr>
<td>{{pagelink:Profile-AllergyIntolerance,text:UKCore-AllergyIntolerance}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the AllergyIntolerance resource for the minimal set of data to query and retrieve allergy information.</td>
<td>2</td>
</tr>
<tr>
<td>{{pagelink:Profile-Appointment,text:UKCore-Appointment}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Appointment resource for the minimal set of data to query and retrieve appointment information.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-Composition,text:UKCore-Composition}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Composition resource to enable a generic and flexible approach to FHIR document structures.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-Condition,text:UKCore-Condition}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Condition resource for the minimal set of data to query and retrieve problems and health concerns information.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-Device-BloodPressure,text:UKCore-Device-BloodPressure}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the active UK Core Device profile to define the minimal set of data to query and retrieve information about a device used to monitor blood pressure.</td>
<td>7</td>
</tr>
<tr>
<td>{{pagelink:Profile-DiagnosticReport,text:UKCore-DiagnosticReport}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the DiagnosticReport resource for the minimal set of data to query and retrieve the findings of diagnostic tests.<br>
<b>Note:</b> This profile SHALL NOT be used where a more specific UK Core profile exists.</td>
<td>6</td>
</tr>
<tr>
<td>{{pagelink:Profile-DiagnosticReport-Lab,text:UKCore-DiagnosticReport-Lab}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on theDiagnosticReport profile to define the minimal set of data to query and retrieve the findings specifically related to laboratory tests.</td>
<td>6</td>
</tr>
<tr>
<td>{{pagelink:Profile-Encounter,text:UKCore-Encounter}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Encounter resource for the minimal set of data to query and retrieve encounter information.</td>
<td>4</td>
</tr>
<tr>
<td>{{pagelink:Profile-FamilyMemberHistory,text:UKCore-FamilyMemberHistory}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the FamilyMemberHistory resource for the minimal set of data to query and retrieve information about health events and conditions for a person related to the patient relevant in the context of care.</td>
<td>6</td>
</tr>
<tr>
<td>{{pagelink:Profile-HealthcareService,text:UKCore-HealthcareService}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the HealthcareService resource for the minimal set of data to query and retrieve healthcare service information.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-Immunization,text:UKCore-Immunization}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Immunization resource for the minimal set of data to query and retrieve an individual's immunisation information.</td>
<td>3</td>
</tr>
<tr>
<td>{{pagelink:Profile-List,text:UKCore-List}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the List resource for the minimal set of data to query and retrieve a list of information.</td>
<td>4</td>
</tr>
<tr>
<td>{{pagelink:Profile-Location,text:UKCore-Location}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Location resource for the minimal set of data to query and retrieve location information</td>
<td>1</td>
</tr>
<tr>
<td>{{pagelink:Profile-Medication,text:UKCore-Medication}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Medication resource for the minimal set of data to query and retrieve medication information.</td>
<td>3</td>
</tr>
<tr>
<td>{{pagelink:Profile-MedicationAdministration,text:UKCore-MedicationAdministration}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the MedicationAdministration resource for the minimal set of data to query and retrieve medication administration information</td>
<td>3</td>
</tr>
<tr>
<td>{{pagelink:Profile-MedicationDispense,text:UKCore-MedicationDispense}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the MedicationDispense resource for the minimal set of data to query and retrieve dispensed medication information.
</td>
<td>3</td>
</tr>
<tr>
<td>{{pagelink:Profile-MedicationRequest,text:UKCore-MedicationRequest}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the MedicationRequest resource for the minimal set of data to query and retrieve prescription information.</td>
<td>3</td>
</tr>
<tr>
<td>{{pagelink:Profile-MedicationStatement,text:UKCore-MedicationStatement}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the MedicationStatement resource for the minimal set of data to query and retrieve medication statement information.</td>
<td>3</td>
</tr>
<tr>
<td>{{pagelink:Profile-Observation,text:UKCore-Observation}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Observation resource for the minimal set of data to query and retrieve information of measurements and simple assertions made about an individual, device or other subject.<br>
<b>Note:</b> This profile SHALL NOT be used where a more specific derived profile exists.</td>
<td>6</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-ACVPU,text:UKCore-Observation-ACVPU}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's level of consciousness.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-AlcoholConsumption,text:UKCore-Observation-AlcoholConsumption}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's alcohol consumption.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-AverageBloodPressure,text:UKCore-Observation-AverageBloodPressure}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's average blood pressure over a specific time period.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-BloodGlucose,text:UKCore-Observation-BloodGlucose}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's blood glucose level.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-EarlyWarningTotalScore,text:UKCore-Observation-EarlyWarningTotalScore}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's Early Warning Score, such as NEWS2.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-InspiredOxygen,text:UKCore-Observation-InspiredOxygen}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding whether a patient is breathing room air or is on oxygen.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-TobaccoConsumption,text:UKCore-Observation-TobaccoConsumption}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information regarding a patient's tobacco consumption.</td>
<td>7</td>
</tr>
<tr>
<td>{{pagelink:Profile-Observation-Group-Lab,text:UKCore-Observation-Group-Lab}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Observation resource for the minimal set of data to query and retrieve information related to laboratory test groups and panels.</td>
<td>6</td>
</tr>
<tr>
<td>{{pagelink:Profile-Observation-Lab,text:UKCore-Observation-Lab}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Observation resource for the minimal set of data to query and retrieve information related to individual laboratory test results.</td>
<td>6</td>
</tr>
<tr>
<td>{{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation profile to define the minimal set of data to query and retrieve information of a patient's Vital Signs measurements, in order to be FHIR compliant with the base "Vital Signs" guidance.<br>
<b>Note:</b> This profile SHALL NOT be used where a more specific derived profile exists, from those listed below.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BloodPressure,text:UKCore-Observation-VitalSigns-BloodPressure}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a single instance of a patient's blood pressure.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BMI,text:UKCore-Observation-VitalSigns-BMI}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's body mass index.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyHeight,text:UKCore-Observation-VitalSigns-BodyHeight}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's height.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyTemperature,text:UKCore-Observation-VitalSigns-BodyTemperature}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's temperature.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyWeight,text:UKCore-Observation-VitalSigns-BodyWeight}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's weight.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-HeadCircumference,text:UKCore-Observation-VitalSigns-HeadCircumference}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's head circumference.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-HeartRate,text:UKCore-Observation-VitalSigns-HeartRate}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's heart rate.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-OxygenSaturation,text:UKCore-Observation-VitalSigns-OxygenSaturation}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's level of oxygen saturation in their blood.</td>
<td>7</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-RespirationRate,text:UKCore-Observation-VitalSigns-RespirationRate}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core Observation Vital Signs profile to define the minimal set of data to query and retrieve information regarding a patient's breathing rate.</td>
<td>7</td>
</tr>
<tr>
<td>{{pagelink:Profile-Organization,text:UKCore-Organization}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Organization resource for the minimal set of data to query and retrieve organisation information.</td>
<td>1</td>
</tr>
<tr>
<td>{{pagelink:Profile-Patient,text:UKCore-Patient}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Patient resource for the minimal set of data to query and retrieve an individual’s demographic information.</td>
<td>1</td>
</tr>
<tr>
<td>{{pagelink:Profile-Practitioner,text:UKCore-Practitioner}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Practitioner resource for the minimal set of data to query and retrieve practitioner information.</td>
<td>1</td>
</tr>
<tr>
<td>{{pagelink:Profile-PractitionerRole,text:UKCore-PractitionerRole}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the PractitionerRole resource for the minimal set of data to query and retrieve practitioner role information.</td>
<td>1</td>
</tr>
<tr>
<td>{{pagelink:Profile-Procedure,text:UKCore-Procedure}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Procedure resource for the minimal set of data to query and retrieve the patient’s procedure information.</td>
<td>4</td>
</tr>
<tr>
<td>{{pagelink:Profile-RelatedPerson,text:UKCore-RelatedPerson}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the RelatedPerson resource for the minimal set of data to query and retrieve related person information.</td>
<td>4</td>
</tr>
<tr>
<td>{{pagelink:Profile-Schedule,text:UKCore-Schedule}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Schedule resource for the minimal set of data to query and retrieve schedule information.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-ServiceRequest,text:UKCore-ServiceRequest}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the ServiceRequest resource for the minimal set of data to query and retrieve service request information.<br>
<b>Note:</b> This profile SHALL NOT be used where a more specific UK Core profile exists.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-ServiceRequest-Lab,text:UKCore-ServiceRequest-Lab}}</td>
<td>active</td>
<td>A profile <i>derived</i> from the UK Core ServiceRequest profile to define the minimal set of data to query and retrieve the request for laboratory tests</td>
<td>6</td>
</tr>
<tr>
<td>{{pagelink:Profile-Slot,text:UKCore-Slot}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Slot resource for the minimal set of data to query and retrieve slot information.</td>
<td>5</td>
</tr>
<tr>
<td>{{pagelink:Profile-Specimen,text:UKCore-Specimen}}</td>
<td>active</td>
<td>Defines the UK Core constraints and extensions on the Specimen resource for the minimal set of data to query and retrieve information regarding samples used for analysis.</td>
<td>6</td>
</tr>
</table>
</div>

<div id="Alphabetical" class="tabcontent">
<h3>Alphabetical Listing</h3>

<table width="100%">
<tbody>
<tr class="a-to-z"><td>
<p><b>A-D:</b></p>
<ul>
<li>{{pagelink:Profile-AllergyIntolerance,text:UKCore-AllergyIntolerance}}</li>
<li>{{pagelink:Profile-Appointment,text:UKCore-Appointment}}</li>
<li>{{pagelink:Profile-Composition,text:UKCore-Composition}}</li>
<li>{{pagelink:Profile-Condition,text:UKCore-Condition}}</li>
<li>{{pagelink:Profile-Device-BloodPressure,text:UKCore-Device-BloodPressure}}</li>
<li>{{pagelink:Profile-DiagnosticReport,text:UKCore-DiagnosticReport}}</li>
<li>{{pagelink:Profile-DiagnosticReport-Lab,text:UKCore-DiagnosticReport-Lab}}</li>
</ul>
</td><td style="border-left: 1px solid #eeeeee">
<p><b>E-L:</b></p>
<ul>
<li>{{pagelink:Profile-Encounter,text:UKCore-Encounter}}</li>
<li>{{pagelink:Profile-FamilyMemberHistory,text:UKCore-FamilyMemberHistory}}</li>
<li>{{pagelink:Profile-HealthcareService,text:UKCore-HealthcareService}}</li>
<li>{{pagelink:Profile-Immunization,text:UKCore-Immunization}}</li>
<li>{{pagelink:Profile-List,text:UKCore-List}}</li>
<li>{{pagelink:Profile-Location,text:UKCore-Location}}</li>
</ul>
</td><td style="border-left: 1px solid #eeeeee">
<p><b>M-P:</b></p>
<ul>
<li>{{pagelink:Profile-Medication,text:UKCore-Medication}}</li>
<li>{{pagelink:Profile-MedicationAdministration,text:UKCore-MedicationAdministration}}</li>
<li>{{pagelink:Profile-MedicationDispense,text:UKCore-MedicationDispense}}</li>
<li>{{pagelink:Profile-MedicationRequest,text:UKCore-MedicationRequest}}</li>
<li>{{pagelink:Profile-MedicationStatement,text:UKCore-MedicationStatement}}</li>
<li>{{pagelink:Profile-Observation,text:UKCore-Observation}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-ACVPU,text:UKCore-Observation-ACVPU}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-AlcoholConsumption,text:UKCore-Observation-AlcoholConsumption}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-AverageBloodPressure,text:UKCore-Observation-AverageBloodPressure}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-BloodGlucose,text:UKCore-Observation-BloodGlucose}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-EarlyWarningTotalScore,text:UKCore-Observation-EarlyWarningTotalScore}}</li>
<li>{{pagelink:Profile-Observation-Group-Lab,text:UKCore-Observation-Group-Lab}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-InspiredOxygen,text:UKCore-Observation-InspiredOxygen}}</li>
<li>{{pagelink:Profile-Observation-Lab,text:UKCore-Observation-Lab}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-TobaccoConsumption,text:UKCore-Observation-TobaccoConsumption}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BloodPressure,text:UKCore-Observation-VitalSigns-BloodPressure}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BMI,text:UKCore-Observation-VitalSigns-BMI}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyHeight,text:UKCore-Observation-VitalSigns-BodyHeight}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyTemperature,text:UKCore-Observation-VitalSigns-BodyTemperature}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyWeight,text:UKCore-Observation-VitalSigns-BodyWeight}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-HeadCircumference,text:UKCore-Observation-VitalSigns-HeadCircumference}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-HeartRate,text:UKCore-Observation-VitalSigns-HeartRate}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-OxygenSaturation,text:UKCore-Observation-VitalSigns-OxygenSaturation}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-RespirationRate,text:UKCore-Observation-VitalSigns-RespirationRate}}</li>
<li>{{pagelink:Profile-Organization,text:UKCore-Organization}}</li>
<li>{{pagelink:Profile-Patient,text:UKCore-Patient}}</li>
<li>{{pagelink:Profile-Practitioner,text:UKCore-Practitioner}}</li>
<li>{{pagelink:Profile-PractitionerRole,text:UKCore-PractitionerRole}}</li>
<li>{{pagelink:Profile-Procedure,text:UKCore-Procedure}}</li>
</ul>
</td><td style="border-left: 1px solid #eeeeee">
<p><b>Q-Z:</b></p> 
<ul>  
<li>{{pagelink:Profile-RelatedPerson,text:UKCore-RelatedPerson}}</li>
<li>{{pagelink:Profile-Schedule,text:UKCore-Schedule}}</li>
<li>{{pagelink:Profile-ServiceRequest,text:UKCore-ServiceRequest}}</li>
<li>{{pagelink:Profile-ServiceRequest-Lab,text:UKCore-ServiceRequest-Lab}}</li>
<li>{{pagelink:Profile-Slot,text:UKCore-Slot}}</li>
<li>{{pagelink:Profile-Specimen,text:UKCore-Specimen}}</li>
</ul>
</td></tr>

</tbody></table>
</div>



<div id="Sprint" class="tabcontent">
<h3>By Sprint</h3>

<p><b>C&TA Sprint 1:</b></p>
<ul>
<li>{{pagelink:Profile-Location,text:UKCore-Location}}</li>
<li>{{pagelink:Profile-Organization,text:UKCore-Organization}}</li>
<li>{{pagelink:Profile-Patient,text:UKCore-Patient}}</li>
<li>{{pagelink:Profile-Practitioner,text:UKCore-Practitioner}}</li>
<li>{{pagelink:Profile-PractitionerRole,text:UKCore-PractitionerRole}}</li>
</ul>

<p><b>C&TA Sprint 2:</b></p>
<ul>
<li>{{pagelink:Profile-AllergyIntolerance,text:UKCore-AllergyIntolerance}}</li>
</ul>

<p><b>C&TA Sprint 3:</b></p>
<ul>
<li>{{pagelink:Profile-Immunization,text:UKCore-Immunization}}</li>
<li>{{pagelink:Profile-Medication,text:UKCore-Medication}}</li>
<li>{{pagelink:Profile-MedicationAdministration,text:UKCore-MedicationAdministration}}</li>
<li>{{pagelink:Profile-MedicationDispense,text:UKCore-MedicationDispense}}</li>
<li>{{pagelink:Profile-MedicationRequest,text:UKCore-MedicationRequest}}</li>
<li>{{pagelink:Profile-MedicationStatement,text:UKCore-MedicationStatement}}</li>
</ul>

<p><b>C&TA Sprint 4:</b></p>
<ul>
<li>{{pagelink:Profile-Encounter,text:UKCore-Encounter}}</li>
<li>{{pagelink:Profile-List,text:UKCore-List}}</li>
<li>{{pagelink:Profile-Procedure,text:UKCore-Procedure}}</li>
<li>{{pagelink:Profile-RelatedPerson,text:UKCore-RelatedPerson}}</li>
</ul>

<p><b>C&TA Sprint 5:</b></p>
<ul>
<li>{{pagelink:Profile-Appointment,text:UKCore-Appointment}}</li>
<li>{{pagelink:Profile-Composition,text:UKCore-Composition}}</li>
<li>{{pagelink:Profile-Condition,text:UKCore-Condition}}</li>
<li>{{pagelink:Profile-HealthcareService,text:UKCore-HealthcareService}}</li>
<li>{{pagelink:Profile-ServiceRequest,text:UKCore-ServiceRequest}}</li>
<li>{{pagelink:Profile-Schedule,text:UKCore-Schedule}}</li>
<li>{{pagelink:Profile-Slot,text:UKCore-Slot}}</li>
</ul>

<p><b>C&TA Sprint 6:</b></p>
<ul>
<li>{{pagelink:Profile-DiagnosticReport,text:UKCore-DiagnosticReport}}</li>
<li>{{pagelink:Profile-DiagnosticReport-Lab,text:UKCore-DiagnosticReport-Lab}}</li>
<li>{{pagelink:Profile-FamilyMemberHistory,text:UKCore-FamilyMemberHistory}}</li>
<li>{{pagelink:Profile-Observation,text:UKCore-Observation}}</li>
<li>{{pagelink:Profile-Observation-Group-Lab,text:UKCore-Observation-Group-Lab}}</li>
<li>{{pagelink:Profile-Observation-Lab,text:UKCore-Observation-Lab}}</li>
<li>{{pagelink:Profile-ServiceRequest-Lab,text:UKCore-ServiceRequest-Lab}}</li>
<li>{{pagelink:Profile-Specimen,text:UKCore-Specimen}}</li>
</ul>

<p><b>C&TA Sprint 7:</b></p>
<ul>
<li>{{pagelink:Profile-Device-BloodPressure,text:UKCore-Device-BloodPressure}}</li>
<li>{{pagelink:Profile-Observation-ACVPU,text:UKCore-Observation-ACVPU}}</li>
<li>{{pagelink:Profile-Observation-AlcoholConsumption,text:UKCore-Observation-AlcoholConsumption}}</li>
<li>{{pagelink:Profile-Observation-AverageBloodPressure,text:UKCore-Observation-AverageBloodPressure}}</li>
<li>{{pagelink:Profile-Observation-BloodGlucose,text:UKCore-Observation-BloodGlucose}}</li>
<li>{{pagelink:Profile-Observation-EarlyWarningTotalScore,text:UKCore-Observation-EarlyWarningTotalScore}}</li>
<li>{{pagelink:Profile-Observation-InspiredOxygen,text:UKCore-Observation-InspiredOxygen}}</li>
<li>{{pagelink:Profile-Observation-TobaccoConsumption,text:UKCore-Observation-TobaccoConsumption}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-BloodPressure,text:UKCore-Observation-VitalSigns-BloodPressure}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-BMI,text:UKCore-Observation-VitalSigns-BMI}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-BodyHeight,text:UKCore-Observation-VitalSigns-BodyHeight}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-BodyTemperature,text:UKCore-Observation-VitalSigns-BodyTemperature}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-BodyWeight,text:UKCore-Observation-VitalSigns-BodyWeight}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-HeadCircumference,text:UKCore-Observation-VitalSigns-HeadCircumference}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-HeartRate,text:UKCore-Observation-VitalSigns-HeartRate}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-OxygenSaturation,text:UKCore-Observation-VitalSigns-OxygenSaturation}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns-RespirationRate,text:UKCore-Observation-VitalSigns-RespirationRate}}</li>
</ul>

</div>

<div id="Resource" class="tabcontent">
<h3>By Resource</h3>

<p><b>AllergyIntolerance:</b></p>
<ul>
<li>{{pagelink:Profile-AllergyIntolerance,text:UKCore-AllergyIntolerance}}</li>
</ul>
<p><b>Appointment:</b></p>
<ul>
<li>{{pagelink:Profile-Appointment,text:UKCore-Appointment}}</li>
</ul>
<p><b>Composition:</b></p>
<ul>
<li>{{pagelink:Profile-Composition,text:UKCore-Composition}}</li>
</ul>
<p><b>Condition:</b></p>
<ul>
<li>{{pagelink:Profile-Condition,text:UKCore-Condition}}</li>
</ul>
<p><b>Device:</b></p>
<ul>
<li>{{pagelink:Profile-Device-BloodPressure,text:UKCore-Device-BloodPressure}}</li>
</ul>
<p><b>DiagnosticReport:</b></p>
<ul>
<li>{{pagelink:Profile-DiagnosticReport,text:UKCore-DiagnosticReport}}</li>
<li>{{pagelink:Profile-DiagnosticReport-Lab,text:UKCore-DiagnosticReport-Lab}}</li>
</ul>
<p><b>Encounter:</b></p>
<ul>
<li>{{pagelink:Profile-Encounter,text:UKCore-Encounter}}</li>
</ul>
<p><b>FamilyMemberHistory:</b></p>
<ul>
<li>{{pagelink:Profile-FamilyMemberHistory,text:UKCore-FamilyMemberHistory}}</li>
</ul>
<p><b>HealthcareService:</b></p>
<ul>
<li>{{pagelink:Profile-HealthcareService,text:UKCore-HealthcareService}}</li>
</ul>
<p><b>Immunization:</b></p>
<ul>
<li>{{pagelink:Profile-Immunization,text:UKCore-Immunization}}</li>
</ul>
<p><b>List:</b></p>
<ul>
<li>{{pagelink:Profile-List,text:UKCore-List}}</li>
</ul>
<p><b>Location:</b></p>
<ul>
<li>{{pagelink:Profile-Location,text:UKCore-Location}}</li>
</ul>
<p><b>Medication:</b></p>
<ul>
<li>{{pagelink:Profile-Medication,text:UKCore-Medication}}</li>
</ul>
<p><b>MedicationAdministration:</b></p>
<ul>
<li>{{pagelink:Profile-MedicationAdministration,text:UKCore-MedicationAdministration}}</li>
</ul>
<p><b>MedicationDispense:</b></p>
<ul>
<li>{{pagelink:Profile-MedicationDispense,text:UKCore-MedicationDispense}}</li>
</ul>
<p><b>MedicationRequest:</b></p>
<ul>
<li>{{pagelink:Profile-MedicationRequest,text:UKCore-MedicationRequest}}</li>
</ul>
<p><b>MedicationStatement:</b></p>
<ul>
<li>{{pagelink:Profile-MedicationStatement,text:UKCore-MedicationStatement}}</li>
</ul>
<p><b>Observation:</b></p>
<ul>
<li>{{pagelink:Profile-Observation,text:UKCore-Observation}}</li>
<li>Derived Profiles from UK Core Observation</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-ACVPU,text:UKCore-Observation-ACVPU}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-AlcoholConsumption,text:UKCore-Observation-AlcoholConsumption}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-AverageBloodPressure,text:UKCore-Observation-AverageBloodPressure}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-BloodGlucose,text:UKCore-Observation-BloodGlucose}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-EarlyWarningTotalScore,text:UKCore-Observation-EarlyWarningTotalScore}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-InspiredOxygen,text:UKCore-Observation-InspiredOxygen}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-TobaccoConsumption,text:UKCore-Observation-TobaccoConsumption}}</li>
<li>{{pagelink:Profile-Observation-Group-Lab,text:UKCore-Observation-Group-Lab}}</li>
<li>{{pagelink:Profile-Observation-Lab,text:UKCore-Observation-Lab}}</li>
<li>{{pagelink:Profile-Observation-VitalSigns,text:UKCore-Observation-VitalSigns}}</li>
<li>Derived Profiles from UK Core Observation Vital Signs</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BloodPressure,text:UKCore-Observation-VitalSigns-BloodPressure}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BMI,text:UKCore-Observation-VitalSigns-BMI}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyHeight,text:UKCore-Observation-VitalSigns-BodyHeight}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyTemperature,text:UKCore-Observation-VitalSigns-BodyTemperature}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-BodyWeight,text:UKCore-Observation-VitalSigns-BodyWeight}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-HeadCircumference,text:UKCore-Observation-VitalSigns-HeadCircumference}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-HeartRate,text:UKCore-Observation-VitalSigns-HeartRate}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-OxygenSaturation,text:UKCore-Observation-VitalSigns-OxygenSaturation}}</li>
<li>&nbsp;&nbsp;{{pagelink:Profile-Observation-VitalSigns-RespirationRate,text:UKCore-Observation-VitalSigns-RespirationRate}}</li>
</ul>
<p><b>Organization:</b></p>
<ul>
<li>{{pagelink:Profile-Organization,text:UKCore-Organization}}</li>
</ul>
<p><b>Patient:</b></p>
<ul>
<li>{{pagelink:Profile-Patient,text:UKCore-Patient}}</li>
</ul>
<p><b>Practitioner:</b></p>
<ul>
<li>{{pagelink:Profile-Practitioner,text:UKCore-Practitioner}}</li>
</ul>
<p><b>PractitionerRole:</b></p>
<ul>
<li>{{pagelink:Profile-PractitionerRole,text:UKCore-PractitionerRole}}</li>
</ul>
<p><b>Procedure:</b></p>
<ul>
<li>{{pagelink:Profile-Procedure,text:UKCore-Procedure}}</li>
</ul>
<p><b>RelatedPerson:</b></p>
<ul>
<li>{{pagelink:Profile-RelatedPerson,text:UKCore-RelatedPerson}}</li>
</ul>
<p><b>Schedule:</b></p>
<ul>
<li>{{pagelink:Profile-Schedule,text:UKCore-Schedule}}</li>
</ul>
<p><b>ServiceRequest:</b></p>
<ul>
<li>{{pagelink:Profile-ServiceRequest,text:UKCore-ServiceRequest}}</li>
<li>{{pagelink:Profile-ServiceRequest-Lab,text:UKCore-ServiceRequest-Lab}}</li>
</ul>
<p><b>Slot:</b></p>
<ul>
<li>{{pagelink:Profile-Slot,text:UKCore-Slot}}</li>
</ul>
<p><b>Specimen:</b></p>
<ul>
<li>{{pagelink:Profile-Specimen,text:UKCore-Specimen}}</li>
</ul>

</div>

