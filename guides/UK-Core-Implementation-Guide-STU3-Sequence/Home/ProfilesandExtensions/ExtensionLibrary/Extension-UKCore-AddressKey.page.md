---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-AddressKey
issue: Extension-UKCore-AddressKey
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>Address</td>
</tr>
</table>

{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Address Key</b>- An example to illustrate how the address key information is carried in a patient example. </br>
{{pagelink:UKCore-Extension-AddressKey-Example}}
<br><br>
</div>

<h3 id="guidance-addresskey">Extension Specific Guidance</h3>

There is a binding within this extension to a {{pagelink:ValueSet-UKCore-AddressKeyType}}.

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The datatype of the <code>type</code> element was changed from <code>valueCoding</code> in UK Core STU1 Sequence, to <code>valueCodeableConcept</code>, as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div> 

---
