---
topic: Library-Extensions-HL7
---
## HL7 Core-defined Extensions

The following <a href="http://hl7.org/fhir/R4/extensibility-registry.html" class="external">HL7 Core-defined Extensions</a> have been agreed as suitable to be included for use with the UK Core {{pagelink:Library-Profiles,text:Profiles}} because the use case for an Extension is fully met by a pre-existing HL7 Core-defined Extension.

Implementers of the UK Core profiles MAY also use other HL7 core-defined extensions to extend the UK Core if required by the local implementation, but are encouraged to engage with the UK Core development process to add guidance into the UK Core for wider use by the UK FHIR Community.

<table class="assets" title="HL7 defined Extension list and context of use details">
<tr>
<th>HL7 Core-defined Extension</th>
<th>Context of Use</th>
<th>Related Profile</th>
<th>Modifier Extension</th>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-coding-sctdescid.html" class="external">Extension coding-sctdescid</a></td>
<td>Coding</td>
<td>Use on Element ID Coding</td>
<td>NO</td>
</tr>
<tr>
<td><a href="http://hl7.org/fhir/R4/extension-observation-bodyposition.html" class="external">Extension observation-bodyPosition</a></td>
<td>Observation</td>
<td>{{pagelink:UKCore-Observation-VitalSigns}}</td>
<td>NO</td>
</tr>
<tr>            
<td><a href="https://hl7.org/fhir/R4/extension-organization-period.html" class="external">Extension organization-period</a></td>
<td>Organization</td>
<td>{{pagelink:UKCore-Organization}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-patient-birthPlace.html" class="external">Extension patient-birthPlace</a></td>
<td>Patient</td>
<td>{{pagelink:UKCore-Patient}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-patient-birthTime.html" class="external">Extension patient-birthTime</a></td>
<td>Patient.birthDate</td>
<td>{{pagelink:UKCore-Patient}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-patient-cadavericDonor.html" class="external">Extension patient-cadavericDonor</a></td>
<td>Patient</td>
<td>{{pagelink:UKCore-Patient}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-patient-interpreterRequired.html" class="external">Extension patient-interpreterRequired</a></td>
<td>Patient</td>
<td>{{pagelink:UKCore-Patient}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-patient-proficiency.html">Core-defined Extension patient-proficiency</a></td>
<td>Patient</td>
<td>{{pagelink:UKCore-Patient}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R4/extension-specimen-specialhandling.html" class="external">Extension specimen-specialHandling</a></td>
<td>Specimen.collection</td>
<td>{{pagelink:UKCore-Specimen}}</td>
<td>NO</td>
</tr>

</table>

---