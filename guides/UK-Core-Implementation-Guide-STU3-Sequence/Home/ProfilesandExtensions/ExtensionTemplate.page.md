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
	Description: description,
	Profile_Purpose: purpose
  with header 
  
</fql>

<div id="transpose">
</div>
<br>

<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'tree-view')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'detailed-view')">Detailed View</button>
   <button class="tablinks" onclick="openTab(event, 'table-view')">Table View</button>
   <button class="tablinks" onclick="openTab(event, 'xml-view')">XML View</button>
   <button class="tablinks" onclick="openTab(event, 'json-view')">JSON View</button>
  <button class="tablinks" onclick="openTab(event, 'Examples')">Examples</button>
  <button class="tablinks feedback" onclick="openTab(event, 'Feedback')">Feedback</button>
</div>

<div id="tree-view" class="tabcontent" style="display:block">
  <h3>Tree View</h3>
{{tree}}
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

<div id="Feedback" class="tabcontent">
  <h3>Feedback</h3>
Click here to: {{page:Home/ProfilesandExtensions/FeedbackLink.page.md}}</a>
</div>