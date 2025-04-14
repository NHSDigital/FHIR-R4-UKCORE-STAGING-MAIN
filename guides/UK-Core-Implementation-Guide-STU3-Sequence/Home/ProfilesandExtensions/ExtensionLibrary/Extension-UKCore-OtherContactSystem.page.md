---
subject: https://fhir.hl7.org.uk/StructureDefinition/Extension-UKCore-OtherContactSystem
issue: Extension-UKCore-OtherContactSystem
---
## StructureDefinition {{variable:issue}}

<table id="addToTranspose">
<tr><td>Context of Use</td>
<td>ContactPoint.system</td>
</tr>
</table>

{{page:Home/ProfilesandExtensions/ExtensionTemplate.page.md}}

<div id="Examples" class="tabcontent">
  <h3>Examples</h3>
<b>Other Contact System</b> - An example to illustrate other contact methods for a patient. </br>
{{pagelink:UKCore-Extension-OtherContactSystem-Example}}
<br><br>
</div>

<h3 id="guidance-othercomntactsystem">Extension Specific Guidance</h3>

There is a binding within this extension to a {{pagelink:ValueSet-UKCore-OtherContactSystem}}.

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The datatype of this extension was changed from <code>valueCoding</code> in UK Core STU1 Sequence, to <code>valueCodeableConcept</code>, as a result of the UK Core STU2 Sequence ballot reconciliation actions.
</div> 

---
