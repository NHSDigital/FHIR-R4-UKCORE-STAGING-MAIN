## <code>{{page-title}}</code>

The `Encounter.participant.type` element SHOULD include the role of the participant in the encounter using the following values which may be extended. The binding is to the International FHIR ValueSet <a href="https://hl7.org/fhir/R4/valueset-encounter-participant-type.html" class="external">encounter-participant-type</a>, which is shown expanded here due to the complexity of included codes and systems.

<table class="assets" title="Participant type list">
<tr>
<th>Code</th>
<th>System</th>	
<th>Display</th>
<th>Definition</th>
</tr>
<tr>
<td>ADM</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>admitter</td>	
<td>The practitioner who is responsible for admitting a patient to a patient encounter.</td>
</tr>
<tr>
<td>ATND</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>
<td>attender</td>	
<td>The practitioner that has responsibility for overseeing a patient's care during a patient encounter.</td>
</tr>
<tr>
<td>CALLBCK</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>callback contact</td>	
<td>A person or organization who should be contacted for follow-up questions about the act in place of the author.</td>
</tr>
<tr>
<td>CON</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>consultant</td>
<td>An advisor participating in the service by performing evaluations and making recommendations.</td>
</tr>
<tr>
<td>DIS</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>discharger</td>	
<td>The practitioner who is responsible for the discharge of a patient from a patient encounter.</td>
</tr>
<tr>
<td>ESC</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>escort</td>	
<td>Only with Transportation services. A person who escorts the patient.</td>
</tr>
<tr>
<td>REF</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>referrer</td>	
<td>A person having referred the subject of the service to the performer (referring physician). Typically, a referring physician will receive a report.</td>
</tr>
<tr>
<td>SPRF</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>secondary performer</td>	
<td>A person assisting in an act through his substantial presence and involvement This includes: assistants, technicians, associates, or whatever the job titles may be.</td>
</tr>
<tr>
<td>PPRF</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>primary performer</td>	
<td>The principal or primary performer of the act.</td>
</tr>
<tr>
<td>PART</td>	
<td><code>http://terminology.hl7.org/CodeSystem/v3-ParticipationType</code></td>	
<td>Participation</td>	
<td>Indicates that the target of the participation is involved in some manner in the act, but does not qualify how.</td>
</tr>
<tr>
<td>translator</td>	
<td><code>http://terminology.hl7.org/CodeSystem/participant-type</code></td>	
<td>Translator</td>	
<td>A translator who is facilitating communication with the patient during the encounter.</td>
</tr>
<tr>
<td>emergency</td>	
<td><code>http://terminology.hl7.org/CodeSystem/participant-type</code></td>	
<td>Emergency</td>	
<td>A person to be contacted in case of an emergency during the encounter.</td>
</tr>
</table>

<br><br>
Where possible, the `Encounter.participant.individual` is expected that the resource being referenced SHOULD conform to one of the following UK Core profiles:
- {{pagelink:Profile-Practitioner}}
- {{pagelink:Profile-PractitionerRole}}
- {{pagelink:Profile-RelatedPerson}}

---
