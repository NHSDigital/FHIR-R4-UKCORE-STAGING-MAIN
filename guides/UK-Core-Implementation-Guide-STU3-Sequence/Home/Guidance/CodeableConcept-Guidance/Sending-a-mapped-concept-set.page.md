## Sending a mapped concept set 

In the case where a code was entered into the clinical system using a legacy coding system and the code was mapped to a SNOMED CT Concept, the following scenario SHALL be considered. 

In SNOMED CT, all Concept Ids always have more than one associated description: all have at least one fully specified name and at least one additional associated synonym. Of these, exactly one fully specified name and one synonym will be declared to be “preferred” at any point in time within a Realm Language Reference Set, but which terms are designated “preferred” can and does change over time.

Therefore, in most cases where such mappings have been created, they will have been mapped to an explicit pairing of one SNOMED CT Concept Id and one of its legitimate Description Ids. The particular Description ID selected might also correspond to the preferred term but often does not.

Exceptionally, mappings could correspond to a SNOMED CT Concept Id only and so no particular description is declared in the map. In these cases the description originally entered by the clinician in the legacy coding system SHALL be considered to be the clinically relevant text.

#### As per example below:
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:Extension-UKCore-CodingSCT-Potassium-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:Extension-UKCore-CodingSCT-Potassium-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:Extension-UKCore-CodingSCT-Potassium-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:Extension-UKCore-CodingSCT-Potassium-Example}}
</div>

---
