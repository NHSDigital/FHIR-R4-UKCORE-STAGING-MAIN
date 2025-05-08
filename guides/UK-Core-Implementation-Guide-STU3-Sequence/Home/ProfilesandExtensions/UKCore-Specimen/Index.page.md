---
topic: UKCore-Specimen
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-Specimen
usage: http://hl7.org/fhir/StructureDefinition/Specimen
issue: UKCore-Specimen
---
# StructureDefinition {{variable:issue}}

<nocheck>
{{page:ProfileTemplate}}

<div id="Examples" class="tabcontent">
<h3>Examples</h3>
<b>Blood Specimen</b> - An example to illustrate a blood specimen for a patient.<br/>
{{pagelink:UKCore-Specimen-BloodSpecimen-Example}}
<br><br>
<b>Composition Reference</b> - An example to illustrate the pre-adopted R5 element via an extension, which is used to reference a Patient or RelatedPerson within Specimen.collection.collector.<br>
{{pagelink:UKCore-Extension-CollectionCollector-Example}}
<br><br>
<b>High Risk Specimen</b> - An example to illustrate using the HL7 core-defined Extension specimen-specialHandling to record why a specimen should be treated as a high risk.<br/>
{{pagelink:UKCore-Extension-SpecialHandling-Example}}
<br><br>
<b>Median Cubital Vein</b> - An example to illustrate the extension for a referenced body site.<br>
{{pagelink:UKCore-Extension-BodySiteReference-Example}}
<br><br>
<b>Sample Category</b> - An example to illustrate the extension to show the Genomics classification of a sample.<br>
{{pagelink:UKCore-Extension-SampleCategory-Example}}
<br><br>
<b>Urine Sample</b> - An example to illustrate a urine specimen for a patient.<br>
{{pagelink:UKCore-Specimen-UrineSpecimen-Example}}
</div>
</nocheck>

<div id="ProfileGuidance">

### Example Usage Scenarios ###
The following are example usage scenarios for the UK Core Specimen profile:

- Query for specimen information
- Exchange specimen information used in Observations and DiagnosticReport

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---