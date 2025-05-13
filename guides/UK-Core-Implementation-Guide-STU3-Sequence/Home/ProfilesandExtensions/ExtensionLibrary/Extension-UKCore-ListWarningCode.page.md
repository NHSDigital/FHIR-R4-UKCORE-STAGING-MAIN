---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-ListWarningCode
issue: Extension-UKCore-ListWarningCode
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-List,text:List}}</td>
</tr>
</table>

{{page:ExtensionTemplate_new}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>List Warning Code</b>- An example to illustrate a warning being provided in a List resource.<br>
  {{pagelink:UKCore-Extension-ListWarningCode-Example}}
  <br><br>
</div>

<h3 id="guidance-listwarningcode">Extension Specific Guidance</h3>

There is a binding within this extension to a {{pagelink:ValueSet-UKCore-ListWarningCode}}.

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The datatype of this extension was changed from <code>valueCode</code> in UK Core STU1 Sequence, to <code>valueCodeableConcept</code>, as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div> 

---