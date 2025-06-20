---
topic: UKCore-Device-BloodPressure
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Device-BloodPressure
usage: http://hl7.org/fhir/StructureDefinition/Device
---




<nocheck>
{{page:ProfileTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Electronic Sphygmomanometer</b> - An example to illustrate recording of a specific blood pressure device.<br/>
{{pagelink:UKCore-Device-Sphygmomanometer-Example}}<br><br>
<b>Cuff Size</b> - An example to illustrate recording of a cuff size used on a blood pressure device.<br/>
{{pagelink:Extension-UKCore-CuffSize-Example}}<br><br>
</div>
</nocheck>


<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Device for Blood Pressure profile:

- Retrieve information pertaining to a blood pressure monitoring/recording device through querying.
- Record or update the device used to measure a patient's blood pressure

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

This is a derived profile of [UKCore-Device (draft)](https://simplifier.net/guide/UKCoreImplementationGuideAssetsinDevelopment/Home/ProfilesandExtensions/Profile-UKCore-Device) and this page only shows the differences between the two. Refer to the base Profile for more implementation guidance.

### Mandatory and Must Support Data Elements

The following elements are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

<table class="assets" title="MustSupport element list">
<tr>
<th class="width30">Element</th>
<th class="width70">Reason</th>
</tr>
<tr>
<td><code>Device.status</code></td>
<td>The status of the Device.</td>
</tr>
<tr>
<td><code>Device.type</code></td>
<td>The type of the Device.</td>
</tr>
</table>
<div>

---
