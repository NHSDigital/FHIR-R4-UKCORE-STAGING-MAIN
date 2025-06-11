## <fql output="inline" delimiter="">where id = %subject select id</fql>

### <fql output="inline" delimiter="">where id = %subject select text.div</fql>

<div class="tab">
  <button class="tablinks active" onclick="openTab(event, 'table-view')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'tree-view')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'xml-view')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'json-view')">JSON View</button>
</div>

<div id="table-view" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table}}
</div>

<div id="tree-view" class="tabcontent">
  <h3>Tree View</h3>
{{tree, expand:9}}
</div>

<div id="xml-view" class="tabcontent">
  <h3>XML View</h3>
{{xml}}
</div>

<div id="json-view" class="tabcontent">
  <h3>JSON View</h3>
{{json}}
</div>

---
