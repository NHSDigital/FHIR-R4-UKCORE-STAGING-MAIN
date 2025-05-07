---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-ConditionEpisode
issue: Extension-UKCore-ConditionEpisode
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>{{pagelink:UKCore-Condition,text:Condition}}</td>
</tr>
</table>

{{page:ExtensionTemplate}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
  <b>Condition episode</b>- An example to illustrate the extension which is used to indicate the episodicity status of a condition.<br>
  {{pagelink:UKCore-Extension-ConditionEpisode-Example}}
</div>

<h3 id="guidance-conditionepisode">Extension Specific Guidance</h3>

There is a binding within this extension to a {{pagelink:ValueSet-UKCore-ConditionEpisodicity}}.

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The datatype of this extension was changed from <code>valueCode</code> in UK Core STU1 Sequence, to <code>valueCodeableConcept</code> , as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div> 

---