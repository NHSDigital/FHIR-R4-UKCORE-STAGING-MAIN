## `{{page-title}}`

This is a backport from R5 to allow referencing to a Composition resource instance that provides structure for organizing the contents of the DiagnosticReport.

Note that the R5 element has the following rule that SHOULD be followed:

<table class="assets" title="Constraints list">
<tr>
<th class="width15">Key</th>
<th class="width15">Severity</th>
<th class="width30">Expression</th>
<th class="width40">Human Description</th>
</tr>
<tr>
<td>dgr-1</td>
<td>error</td>
<td>composition.exists() implies (composition.resolve().section.entry.reference.where(resolve() is Observation) in (result.reference|result.reference.resolve().hasMember.reference))</td>
<td>When a Composition is referenced in <code>Diagnostic.composition</code>, all Observation resources referenced in <code>Composition.entry</code> must also be referenced in <code>Diagnostic.entry</code> or in the references Observations in <code>Observation.hasMember</code>.</td>
</tr>
</table>