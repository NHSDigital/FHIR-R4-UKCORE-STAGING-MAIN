<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>
This CodeSystem has may be new or has been amended since the last ballot. Users are advised to review all content carefully. Details of the changes can be found within the <a href="https://simplifier.net/guide/UKCoreVersionHistory/Home/STU3-Sequence.page.md?version=current">UK Core Version History</a>.

{{page:Home/ProfilesandExtensions/DiffLinkTemplate.page.md}}
</div>

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
 <button class="tablinks active" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'Detailed View')">Detailed View</button>
   <button class="tablinks" onclick="openTab(event, 'Table View')">Table View</button>
   <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
  <!--<button class="tablinks" onclick="openTab(event, 'Usage')">Usage</button>-->
  <button class="tablinks" onclick="openTab(event, 'Examples')">Examples</button>
  <button class="tablinks feedback" onclick="openTab(event, 'Feedback')">Feedback</button>
</div>

<div id="Tree View" class="tabcontent expandedProfile" style="display:block">
{{tree, buttons}}
</div>

<div id="Detailed View" class="tabcontent">
  <h3>Detailed Descriptions</h3>
{{dict}}
</div>

<div id="Table View" class="tabcontent">
  <h3>Table View</h3>
{{table}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json}}
</div>

<div id="Feedback" class="tabcontent">
  <h3>Feedback</h3>
Click here to: {{page:Home/ProfilesandExtensions/FeedbackLink.page.md}}
</div>

