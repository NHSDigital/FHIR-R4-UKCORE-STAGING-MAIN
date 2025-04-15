## `identifier`

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star">Added links to identifier cells to make it easier to find more information.<br>
Added General Medical Practitioner to identifier</div>

The `Practitioner.identifier` can be populated using the examples given below.

<table class="assets" title="Common practitioner identifiers">
<tr>
<th class="width20">Role</th>
<th class="width30">Identifier</th>
<th class="width20">Format</th>
<th class="width30">System</th>
</tr>
<tr style="background-color: #dff0d8;">
<td>General Medical Practitioner</td>
<td><a href="https://www.datadictionary.nhs.uk/attributes/general_medical_practitioner_ppd_code.html">General Medical Practitioner (GMP) PPD Code</a></td>
<td><a href="https://www.datadictionary.nhs.uk/attributes/doctor_index_number.html">Doctor Index Number</a> prefixed with a leading character and with a check digit added.</td>
<td>https://fhir.hl7.org.uk/Id/gmp-number</td>
</tr>
<tr>
<td>Doctors</td>
<td><a href="https://www.datadictionary.nhs.uk/attributes/general_medical_council_reference_number.html">General Medical Council Information (GMC) registration number</a></td>
<td>7 digits OR L + 6 digits. </br>L prefix is for limited registrations.</td>
<td>https://fhir.hl7.org.uk/Id/gmc-number</td>
</tr>
<td>Pharmacist</td>
<td><a href="https://www.datadictionary.nhs.uk/nhs_business_definitions/general_pharmaceutical_council.html?hl=gphc">General Pharmaceutical Council (GPhC) registration number</a></td>
<td>7 digit number starting with the number 2.</td>
<td>https://fhir.hl7.org.uk/Id/gphc-number</td>
</tr>
<td>Nurses, Midwives, Health Visitors</td>
<td><a href="https://www.datadictionary.nhs.uk/nhs_business_definitions/nursing_and_midwifery_council.html?hl=nmc">Nursing and Midwifery Council (NMC) registration number</a></td>
<td>8 character alphanumeric pin.</td>
<td>https://fhir.hl7.org.uk/Id/nmc-number</td>
</tr>
<td>Other Health Care Professions (HCPs)</td>
<td><a href="https://www.datadictionary.nhs.uk/nhs_business_definitions/health_and_care_professions_council.html?hl=hcp">Health and Care Professions Council (HCPC) registration number</a></td>
<td>Up to 6 numbers, and starts with 2 letters. </br>For example **PH123456** </td>
<td>https://fhir.hl7.org.uk/Id/hcpc-number</td>
</tr>

<td>Other (England)</td>
<td><a href="https://digital.nhs.uk/services/gp-connect/develop-gp-connect-services/integrate-with-spine/spine-directory-service">Spine Directory Service (SDS) User ID</a></td>
<td>Refer to Spine Directory Service - FHIR API</td>
<td> NA</td>
</tr>
<td>Other</td>
<td>Other identifier e.g. local ID</td>
<td>Implementation specific</td>
<td>NA</td>
</tr>
</table>
<br>
More information about the GMC, GPhC, and NMC registration numbers can be found within the Glossary, under NHS Data Model and Dictionary.
<br>
More information about SDS can be found within the Glossary, under Spine Directory Service.
<br>
<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The minimum cardinality of <code>Practitioner.identifier.system</code> and <code>Practitioner.identifier.value</code>reset from 1 in UK Core STU1 Sequence, to 0 in this release, as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div> 

---