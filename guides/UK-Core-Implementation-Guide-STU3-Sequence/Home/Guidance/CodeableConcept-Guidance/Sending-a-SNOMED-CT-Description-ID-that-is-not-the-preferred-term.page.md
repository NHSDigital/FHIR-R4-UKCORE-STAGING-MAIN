## Sending a SNOMED CT Description ID that is not the preferred term

In this case, the SNOMED CT Description ID represents a term that is different from the preferred term and therefore the description display will be different from that used to populate the <code>code.coding.display</code> element. Therefore the extension {{pagelink:Extension-UKCore-CodingSCTDescDisplay}} SHALL be populated with the term corresponding to the selected SNOMED CT Description ID, as per the example below.

<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Extension-CodingSCT-Heart-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Extension-CodingSCT-Heart-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Extension-CodingSCT-Heart-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Extension-CodingSCT-Heart-Example}}
</div>

---
