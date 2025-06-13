<fql>
from
	StructureDefinition
where
	url = %subject
select
	Canonical_URL: url,
  Status: status,
  Current_Version: version,
  Last_Updated: date,
	Description: description
  with header 
</fql>

<div id="transpose">
</div>
<br>

<fql>
from
	StructureDefinition
where
	url = %subject
select
	Profile_Purpose: purpose
with header 
</fql>

<div class="tab fhirTree">
 <button class="tablinks active" onclick="openTab(event, 'tree-view')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'detailed-view')">Detailed View</button>
   <button class="tablinks" onclick="openTab(event, 'table-view')">Table View</button>
   <button class="tablinks" onclick="openTab(event, 'xml-view')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'json-view')">JSON View</button>
  <button class="tablinks" onclick="openTab(event, 'examples')">Examples</button>
  <button class="tablinks feedback" onclick="openTab(event, 'feedback')">Feedback</button>
</div>

<div id="tree-view" class="tabcontent expandedProfile" style="display:block">
{{tree, buttons}}
</div>

<div id="detailed-view" class="tabcontent">
  <h3>Detailed Descriptions</h3>
{{dict}}
</div>

<div id="table-view" class="tabcontent">
  <h3>Table View</h3>
{{table}}
</div>

<div id="xml-view" class="tabcontent">
  <h3>XML View</h3>
{{xml}}
</div>

<div id="json-view" class="tabcontent">
  <h3>JSON View</h3>
{{json}}
</div>

<div id="examples"
class="tabcontent">
  <h3>Examples</h3>
{{page:ExampleLinksFQL}}

<i>UK Core Extensions examples can be found on the relevant Extension page.</i>
</div>

<div id="feedback" class="tabcontent">
  <h3>Feedback</h3>
Click here to: {{page:FeedbackLink}}
</div>

