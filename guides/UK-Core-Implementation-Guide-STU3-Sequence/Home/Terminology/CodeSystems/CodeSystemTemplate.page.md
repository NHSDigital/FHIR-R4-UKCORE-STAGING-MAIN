<fql>
from
	CodeSystem
where
	url = %subject
select
	Description: description
with header
</fql>

<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'html-view')">HTML View</button>
 <button class="tablinks" onclick="openTab(event, 'table-view')">Table View</button>
  <button class="tablinks" onclick="openTab(event, 'xml-view')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'json-view')">JSON View</button>
  <button class="tablinks feedback" onclick="openTab(event, 'Feedback')">Feedback</button>
</div>

<div id="html-view" class="tabcontent" style="display:block">
  <h3>HTML View</h3>
{{render}}
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

---