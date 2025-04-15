## Description of elements (in terms of SNOMED CT)

<table class="assets" title="SNOMED CT details">
<tr>
<th class="width45">Element</th>
<th class="width55">Description</th>
</tr>
<tr>
<td><code>code</code></td>
<td>The wrapper element for the CodeableConcept.</td>
</tr>

<tr>
<td><code>code.coding</code></td>
<td>The wrapper element for the coded part of the CodeableConcept.</td>
</tr>

<tr>
<td><code>code.coding.extension.url</code></td>
<td>The HL7 core-defined extension for providing the SNOMED CT Description Id for the display.<br/><small>Value = <code>http://hl7.org/fhir/StructureDefinition/coding-sctdescid</code></small></td>
</tr>

<tr>
<td><code>code.coding.extension.valueId</code><br/><small><small>Where <code>extension.url</code> = http://hl7.org/fhir/StructureDefinition/coding-sctdescid</small></small></td>
<td>The SNOMED CT Description Id for the display.</td>
</tr>

<tr>
<td><code>code.coding.extension.url</code></td>
<td>A UK Core extension for providing a specific SNOMED CT Description display.<br/><small>Value = <code>https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-CodingSCTDescDisplay</code></small></td>
</tr>

<tr>
<td><code>code.coding.extension.valueString</code><br/><small><small>Where <code>extension.url</code> = https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-CodingSCTDescDisplay</small></small></td>
<td>The user selected SNOMED CT Description synonym, where this is different to the SNOMED CT Description preferred term.</td>
</tr>

<tr>
<td><code>code.coding.system</code></td>
<td>Holds the SNOMED CT system identifier <code>http://snomed.info/sct</code> </td>
</tr>

<tr>
<td><code>code.coding.version</code></td>
<td>Not used for SNOMED CT. </td>
</tr>

<tr>
<td><code>code.coding.code</code></td>
<td>Holds the SNOMED CT Concept identifier. </td>
</tr>

<tr>
<td><code>code.coding.display</code></td>
<td>Holds the SNOMED CT Concept preferred term.  </td>
</tr>

<tr>
<td><code>code.coding.userSelected</code></td>
<td>Indicates that this concept was chosen by the user.  </td>
</tr>

<tr>
<td><code>code.text</code></td>
<td>A plain text representation of the concept.</td>
</tr>
</table>


---