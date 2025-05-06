---
topic: Library-Extensions-PreAdopt
---
## Pre-adopted R5/R6 Elements


The following <a href="https://hl7.org/fhir/versions.html#extensions" class="external">R5 elements</a> have been agreed as suitable to be included for use with the UK Core {{pagelink:Library-Profiles,text:Profiles}} because the use case for pre-adopting an R5 element as an Extension, rather than creating a UK Core specific extension is fully met.

<div class="NewAddedItem">Rules and examples for creating and using extensions between versions can be found within <a href="https://build.fhir.org/versions.html#extensions class="external">FHIR Build - Version Management Policy</a>.</div><br>


<i>As of 19/05/2023, the package to enable pre-adopted elements to function as per the guidance, is not available. To enable rendering and validation of these pre-adopted elements, we have provided UK Core proxy extensions, as per the current threads on <a href="https://chat.fhir.org/#narrow/stream/179166-implementers/topic/R5.20Extensions.20for.20R4.3F" class="external">chat.fhir.org</a>, with the R5 canonical urls. These proxy extensions will be retired once the HL7 package is released.</i>

<table class="assets" title="Pre-adopted FHIR R5 elements list and context of use details">
<tr>
<th>R5 Element</th>
<th>Related Profile</th>
<th>Proxy Extension</th>
<th>Modifier Extension</th>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/diagnosticreport-definitions.html#DiagnosticReport.composition" class="external">DiagnosticReport.composition</a></td>
<td>{{pagelink:Profile-DiagnosticReport}}<br>
{{pagelink:Profile-DiagnosticReport-Lab}}</td>
<td>{{pagelink:Extension-UKCore-DiagnosticReportComposition}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/diagnosticreport-definitions.html#DiagnosticReport.note" class="external">DiagnosticReport.note</a></td>
<td>{{pagelink:Profile-DiagnosticReport}}<br>
{{pagelink:Profile-DiagnosticReport-Lab}}</td>
<td>{{pagelink:Extension-UKCore-DiagnosticReportNote}}</td>
<td>NO</td>
</tr>
<td><a href="https://hl7.org/fhir/R5/diagnosticreport-definitions.html#DiagnosticReport.media.link" class="external">DiagnosticReport.media</a></td>
<td>{{pagelink:Profile-DiagnosticReport}}<br>
{{pagelink:Profile-DiagnosticReport-Lab}}</td>
<td>{{pagelink:Extension-UKCore-DiagnosticReportMediaLink}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/diagnosticreport-definitions.html#DiagnosticReport.supportingInfo" class="external">DiagnosticReport.supportingInfo</a></td>
<td>{{pagelink:Profile-DiagnosticReport}}<br>
{{pagelink:Profile-DiagnosticReport-Lab}}</td>
<td>{{pagelink:Extension-UKCore-DiagnosticReportSupportingInfo}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/familymemberhistory-definitions.html#FamilyMemberHistory.participant" class="external">FamilyMemberHistory.participant</a></td>
<td>{{pagelink:Profile-FamilyMemberHistory}}</td>
<td>{{pagelink:Extension-UKCore-FamilyMemberHistoryParticipant}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/observation-definitions.html#Observation.bodyStructure" class="external">Observation.bodyStructure</a></td>
<td>{{pagelink:Profile-Observation}}<br>
{{pagelink:Profile-Observation-Lab}}<br>
{{pagelink:Profile-Observation-Group-Lab}}</td>
<td>{{pagelink:Extension-UKCore-ObservationBodyStructure}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/observation-definitions.html#Observation.triggeredBy" class="external">Observation.triggeredBy</a></td>
<td>{{pagelink:Profile-Observation}}<br>
{{pagelink:Profile-Observation-Lab}}<br>
{{pagelink:Profile-Observation-Group-Lab}}</td>
<td>{{pagelink:Extension-UKCore-ObservationTriggeredBy}}</td>
<td>NO</td>
</tr>
<tr>
<td><a href="https://hl7.org/fhir/R5/specimen-definitions.html#Specimen.collection.collector" class="external">Specimen.collection.collector</a></td>
<td>{{pagelink:Profile-Specimen}}</td>
<td>{{pagelink:Extension-UKCore-SpecimenCollectionCollector}}</td>
<td>NO</td>
</tr>
</table>
<br><br>

<table class="assets" title="Pre-adopted FHIR R6 elements list and context of use details">
<tr>
<th>R6 Element</th>
<th>Related Profile</th>
<th>Proxy Extension</th>
<th>Modifier Extension</th>
</tr>
<tr>
<td><a href="https://build.fhir.org/condition-definitions.html#Condition.bodyStructure" class="external">Condition.bodyStructure</a></td>
<td>{{pagelink:Profile-Condition}}</td>
<td>{{pagelink:Extension-UKCore-ConditionBodyStructure}}</td>
<td>NO</td>
</tr>
</table>

---