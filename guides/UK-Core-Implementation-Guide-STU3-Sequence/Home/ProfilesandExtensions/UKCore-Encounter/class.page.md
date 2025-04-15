## <code>{{page-title}}</code>

This element SHALL be present and the following values must be used. However, an alternative CodeSystem may be used if no suitable code is listed below. The binding is to the International FHIR ValueSet [v3 ActEncounterCode](https://hl7.org/fhir/R4/v3/ActEncounterCode/vs.html), and is shown expanded here due to the complexity of included and excluded codes.

<table class="assets" title="Class list">
<tr>
<th>Code</th>
<th>Display</th>
<th>Definition</th>
</tr>
<tr>
<td>AMB</td>
<td>ambulatory</td>	
<td>A comprehensive term for health care provided in a healthcare facility (e.g. a practitioners office, clinic setting, or hospital) on a nonresident basis. The term ambulatory usually implies that the patient has come to the location and is not assigned to a bed. Sometimes referred to as an outpatient encounter.</td>
</tr>
<tr>
<td>EMER</td>
<td>emergency</td>
<td>A patient encounter that takes place at a dedicated healthcare service delivery location where the patient receives immediate evaluation and treatment, provided until the patient can be discharged or responsibility for the patient's care is transferred elsewhere (for example, the patient could be admitted as an inpatient or transferred to another facility.)</td>
</tr>
<tr>
<td>FLD</td>	
<td>field</td>
<td>A patient encounter that takes place both outside a dedicated service delivery location and outside a patient's residence. Example locations might include an accident site and at a supermarket.</td>
</tr>
<tr>
<td>HH</td>	
<td>home health</td> 
<td>Healthcare encounter that takes place in the residence of the patient or a designee</td>
</tr>
<tr>
<td>IMP</td>	
<td>inpatient encounter</td>
<td>A patient encounter where a patient is admitted by a hospital or equivalent facility, assigned to a location where patients generally stay at least overnight and provided with room, board, and continuous nursing service.</td>
</tr>
<tr>
<td>ACUTE</td>
<td>inpatient acute</td>
<td>An acute inpatient encounter.</td>
</tr>
<tr>
<td>NONAC</td>
<td>inpatient</td> 
<td>non-acute	Any category of inpatient encounter except 'acute'</td>
</tr>
<tr>
<td>OBSENC</td>	
<td>observation encounter</td>
<td>An encounter where the patient usually will start in different encounter, such as one in the emergency department (EMER) but then transition to this type of encounter because they require a significant period of treatment and monitoring to determine whether or not their condition warrants an inpatient admission or discharge. In the majority of cases the decision about admission or discharge will occur within a time period determined by local, regional or national regulation, often between 24 and 48 hours.</td>
</tr>
<tr>
<td>PRENC</td>	
<td>pre-admission</td>	
<td>A patient encounter where patient is scheduled or planned to receive service delivery in the future, and the patient is given a pre-admission account number. When the patient comes back for subsequent service, the pre-admission encounter is selected and is encapsulated into the service registration, and a new account number is generated. Usage Note: This is intended to be used in advance of encounter types such as ambulatory, inpatient encounter, virtual, etc.</td>
</tr>
<tr>
<td>SS</td>	
<td>short stay</td>	
<td>An encounter where the patient is admitted to a health care facility for a predetermined length of time, usually less than 24 hours.</td>
</tr>
<tr>
<td>VR</td>	
<td>virtual</td>
<td>A patient encounter where the patient and the practitioner are not in the same physical location. Examples include telephone conference, email exchange, robotic surgery, and televideo conference.</td.
</tr>
</table>

---

