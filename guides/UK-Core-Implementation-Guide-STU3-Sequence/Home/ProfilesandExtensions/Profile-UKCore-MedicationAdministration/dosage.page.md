## `dosage`

Consider aligning to the Implementation Guide for Digital Medicines, but as a minimum, `MedicationAdministration.dosage.text`.

A MedicationAdministration resource may be used to describe a period of no administration. The `MedicationAdministration.status` would be `on-hold` and either the dosage would be omitted, or a dosage would be recorded with a zero rate or quantity. For example; 

#### Example of `MedicationAdministration.dosage` usage:
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-MedicationAdministration-Sn-ZeroDosage-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-MedicationAdministration-Sn-ZeroDosage-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-MedicationAdministration-Sn-ZeroDosage-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-MedicationAdministration-Sn-ZeroDosage-Example}}
</div>


---