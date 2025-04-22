## `ContactPoint`

Details for all kinds of technology-mediated contact points for a person or organisation, including telephone, email, etc.

The ContactPoint datatype has the following elements and this is an overview of the datatype with additional UK Core guidance. The full definition is available from the <a href="http://hl7.org/fhir/R4/datatypes.html#ContactPoint" class="external">FHIR standard</a>.

<div markdown="span" class="alert alert-warning" role="alert"><i class="fa fa-info-circle"></i> The ContactPoint datatype has a UK Core extension {{pagelink:Extension-UKCore-OtherContactSystem}}. This extension provides information about other contact methods which could be used in addition to those listed in ContactPoint.system.
</div>

<table class="assets" title="ContactPoint DataType details">
<tr>
<th>Element</th>
<th>type</th>
<th>Usage Guidance</th>
<th>Description</th>
</tr>
<tr>
<td><code>system</code></td>
<td>code</td>
<td>SHALL be present</td>
<td>Details for all kinds of technology-mediated contact points for a person or organisation, including telephone, email, etc. </td>
</tr>
<tr>
<td><code>value</code></td>
<td>string</td>
<td>SHALL be present</td>
<td>The actual contact point details</td>
</tr>
<tr>
<td><code>use</code></td>
<td>code</td>
<td>MAY be present</td>
<td>Identifies the purpose for the contact point.</td>
</tr>
<tr>
<td><code>rank</code></td>
<td>positiveInt</td>
<td>MAY be present</td>
<td>Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values.</td>
</tr>
<tr>
<td><code>period</code></td>
<td>Period</td>
<td>MAY be present</td>
<td>Time period when the contact point was/is in use.</td>
</tr>
</table>

---



