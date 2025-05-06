---
topic: Profile-ServiceRequest
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-ServiceRequest
usage: http://hl7.org/fhir/StructureDefinition/ServiceRequest
issue: UKCore-ServiceRequest
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:Home/ProfilesandExtensions/ProfileTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
   <b>Additional Contact</b> - An example to illustrate providing an additional contact with a service request.<br>
{{pagelink:Example-UKCore-Extension-AdditionalContact}}
<br><br>
  <b>Colonoscopy Request</b> - An example to illustrate a service request regarding a colonoscopy.<br/>
{{pagelink:Example-UKCore-ServiceRequest-ColonoscopyRequest}}
<br><br>
<b>Coverage</b> - An example to illustrate the extension for a service request, to state the the coverage of the funding for this request.<br>
{{pagelink:Example-UKCore-Extension-Coverage}}
<br/><br/>
  <b>CT Chest Scan Request</b> - An example to illustrate a service request for a CT scan.<br/>
{{pagelink:Example-UKCore-ServiceRequest-CTChestScan}}
<br><br>
  <b>ECG Request</b> - An example to illustrate a service request for an ECG.<br/>
{{pagelink:Example-UKCore-ServiceRequest-ECG}}
<br><br>
<b>Priority Reason</b> - An example to illustrate the priority reason extension, using a SNOMED CT concept, for a service request marked as urgent.<br>
{{pagelink:Example-UKCore-Extension-PriorityReason}}
<br><br>
  <b>Priority Reason</b> - An example to illustrate the priority reason extension, using a plain text reason, for a service request marked as urgent.<br>
{{pagelink:Example-UKCore-Extension-PriorityReason-SendingAsText}}
<br><br>
<b>Source of Service Request</b> - An example to illustrate the source of service request extension associated with a service request.<br/>
{{pagelink:Example-UKCore-Extension-SourceOfServiceRequest}}
<br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core ServiceRequest profile:
- Query for service request information for a given Patient
- Exchange service request information within a FHIR document or message.

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:Home/ProfilesandExtensions/ProfileMustSupportTemplate.page.md}}

</div>

---