---
topic: UKCore-List
subject: https://fhir.hl7.org.uk/StructureDefinition/UKCore-List
usage: http://hl7.org/fhir/StructureDefinition/List
issue: UKCore-List
---
# StructureDefinition-UKCore-List

{{page:ProfileTemplate}}

<nocheck>
<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Empty List</b> - This example shows the use of an empty List to indicate that there is no content. This is not supposed to represent actual system behaviour.
  <br>{{pagelink:UKCore-List-EmptyList-Example}}
  <br><br>
  <b>Bundled Allergy List</b> - This example is an example FHIR Bundle that could be returned following a query for the allergies for a patient. Note: the use of List and Bundle is not mandated and is used to illustrate a possible use of the List Profile and is not expected system behaviour.<br>
  {{pagelink:UKCore-Bundle-AllergyList-Example}}
  <br><br>
  <b>List Warning Code</b> - An example to illustrate a warning being provided in a List resource.<br>
  {{pagelink:UKCore-Extension-ListWarningCode-Example}}
  <br><br>
</div>
</nocheck>

<div id="ProfileGuidance">

## Example Usage Scenarios ##

The following are example usage scenarios for the UK Core List profile:

- A list of allergies for a Patient
- A list of current medication for a Patient
- Record or update a list of information for Patient

<hr class="thickline">

## Profile Specific Implementation Guidance: ##

{{page:ProfileMustSupportTemplate}}

</div>

---
