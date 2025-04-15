<h2 id="dataAbsentReason"> <code>{{page-title}}</code> </h2>

The inclusion of the coded reason for data being absent is optional, and not currently recommended, because the ValueSet defined in FHIR is of limited benefit to UK laboratory use cases. It is recommended that if a data absent reason is to be included, then a text representation SHOULD be used (i.e. `Observation.dataAbsentReason.text`).

#### Example of `Observation.dataAbsentReason` usage:

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Observation-Lab-Sn-AbsentData-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Observation-Lab-Sn-AbsentData-Example}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Observation-Lab-Sn-AbsentData-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Observation-Lab-Sn-AbsentData-Example}}
</div>
</div>

---