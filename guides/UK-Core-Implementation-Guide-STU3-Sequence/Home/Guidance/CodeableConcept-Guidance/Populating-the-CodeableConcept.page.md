## Populating the CodeableConcept

This section shows you how to populate each field where the code carried is a SNOMED CT Concept and where it’s not a SNOMED CT Concept. It also includes population scenarios with examples.

### Field by field population guidance

#### SNOMED CT

<table class="assets">
<tr>
<th width="45%">Element</th>
<th width="55%">Definition</th>
</tr>
<tr>
<td><code>code.coding</code></td>
<td>Populate this group if a SNOMED CT Concept Id is stored for the item.</td>
</tr>
<tr>
<td><code>code.coding.extension</code><br/><small><small>Where <code>extension.url</code> = http://hl7.org/fhir/StructureDefinition/coding-sctdescid</small></small></td>
<td>The SNOMED CT Description Id recorded with the item. Only populated if a Description Id exists.</td>
</tr>
<tr>
<td><code>code.coding.extension</code><br/><small><small>Where <code>extension.url</code> = https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-CodingSCTDescDisplay</small></small></td>
<td>The display term of the Description Id. This SHOULD be populated if a Description Id exists, but implementers SHOULD NOT populate the extension if the selected display term is lexically identical to the text in <code>coding.display</code>.</td>
</tr>
<tr>
<td><code>code.coding.system</code></td>
<td>Set to <code>http://snomed.info/sct</code></td>
</tr>
<tr>
<td><code>code.coding.code</code></td>
<td>The SNOMED CT Concept Id stored for the item.</td>
</tr>
<tr>
<td><code>code.coding.display</code> </td>
<td>The text of the current preferred term of the SNOMED CT Concept Id according to the current NHS Realm Language Reference Sets.<br>
The preferred term is the description specified for the concept in the NHS realm description subset. The preferred term for a concept may change over time. The sending system SHOULD determine the current preferred term for the concept.</td>
</tr>
<tr>
<td><code>code.coding.userSelected</code></td>
<td>Indicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays).<br>
This should be set to <code>true</code> if a user selected the SNOMED CT Concept when creating/updating this item.</td>
</tr>
<tr>
<td><code>code.text</code></td>
<td>The original text selected / manually entered by the user for the item.</td>
</tr>
</table>           

<br/>

#### Other coding

<table class="assets">
<tr>
<th width="45%">Element</th>
<th width="55%">Definition</th>
</tr>
<tr>
<td><code>code.coding</code></td>
<td>Populate this group if a clinical code other than SNOMED CT is stored for the item. If there are multiple codes (that is, the item has been translated multiple times) there is a group entry per code.</td>
</tr>
<tr>
<td><code>code.coding.extension</code><br/><small><small>Where <code>extension.url</code> = http://hl7.org/fhir/StructureDefinition/coding-sctdescid</small></small></td>
<td><b>Note:</b> Do not use here if coding is not SNOMED CT.</td>
</tr>
<tr>
<td><code>code.coding.extension</code><br/><small><small>Where <code>extension.url</code> = https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-CodingSCTDescDisplay</small></small></td>
<td><b>Note:</b> Do not use here if coding is not SNOMED CT.</td>
</tr>
<tr>
<td><code>code.coding.system</code></td>
<td>The identification of the code system that defines the meaning of the symbol in the code.</td>
</tr>
<tr>
<td><code>code.coding.code</code></td>
<td>The clinical code associated with the item.</td>
</tr>
<tr>
<td><code>code.coding.display</code></td>
<td>The longest character length variant text associated with the current preferred term for the clinical code.</td>
</tr>
<tr>
<td><code><code>code.coding.userSelected</code></td>
<td>Indicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays).<br>
This should be set to <code>true</code> if a user selected this code when creating/updating this item.</td>
</tr>
<tr>
<td><code>code.text</code></td>
<td>The original text selected / manually entered by the user for the item.</td>
</tr>
</table>     

---