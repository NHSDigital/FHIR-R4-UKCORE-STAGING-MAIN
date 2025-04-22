## `identifier`

It is recommended that the `Organization.identifier` value is odsOrganisationCode, but another identifier can be used. 

The organisation ODS code 

<table class="assets" title="ODS organisation code structure">
<tr>
<th class="width30">Element</th>
<th class="width70">Description</th>
</tr>
<tr>
<td><code>Organization.identifier:odsOrganisationCode.use</code></td>
<td>usual | official | temp | secondary | old (If known)</td>
</tr>
<tr>
<td><code>Organization.identifier:odsOrganisationCode.type</code></td>
<td>This is not required with ODS</td>
</tr>
<tr>
<td><code>Organization.identifier:odsOrganisationCode.system</code></td>
<td>The url is <code>https://fhir.nhs.uk/Id/ods-organisation-code</code></td>
</tr>
<tr>
<td><code>Organization.identifier:odsOrganisationCode.value</code></td>
<td>The ODS code</td>
</tr>
<tr>
<td><code>Organization.identifier:odsOrganisationCode.period</code></td>
<td>The period for which the code is valid - MAY be omitted</td>
</tr>
<tr>
<td><code>Organization.identifier:odsOrganisationCode.assigner</code></td>
<td>Implicit for ODS  codes - SHOULD be omitted</td>
</tr>
</table>

<br/>

The ODS site code for a specific site in the organisation

<table class="assets" title="ODS site code structure">
<tr>
<th class="width30">Element</th>
<th class="width70">Description</th>
</tr>
<tr>
<td><code>Organization.identifier:odsSiteCode.use</code></td>
<td>usual | official | temp | secondary | old (If known)</td>
</tr>
<tr>
<td><code>Organization.identifier:odsSiteCode.type</code></td>
<td>This is not required with ODS</td>
</tr>
<tr>
<td><code>Organization.identifier:odsSiteCode.system</code></td>
<td>The url is <code>https://fhir.nhs.uk/Id/ods-site-code</code></td>
</tr>
<tr>
<td><code>Organization.identifier:odsSiteCode.value</code></td>
<td>The ODS site code</td>
</tr>
<tr>
<td><code>Organization.identifier:odsSiteCode.period</code></td>
<td>The period for which the code is valid - MAY be omitted</td>
</tr>
<tr>
<td><code>Organization.identifier:odsSiteCode.assigner</code></td>
<td>Implicit for ODS site codes - SHOULD be omitted</td>
</tr>
</table>

---