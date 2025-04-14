## Sending a SNOMED CT concept with its associated preferred term 

When sending a SNOMED CT Concept Id with its preferred term, and the SNOMED CT Description Id is known, then the HL7 core-defined extension <a href="https://hl7.org/fhir/R4/extension-coding-sctdescid.html" class="external">coding-sctdescid</a> SHALL be used and the element `sctdescid` SHALL be populated. Where the SNOMED CT Description Id is not known, then the codeable concept MAY be sent without it.

In the example below, the SNOMED CT Description Id is populated with the Id of the preferred term, but there is no display term, as the Concept Id was entered by the user and the preferred term was displayed to them when it was added.

<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Extension-CodingSCT-Myocardial-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Extension-CodingSCT-Myocardial-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Extension-CodingSCT-Myocardial-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Extension-CodingSCT-Myocardial-Example}}
</div>

---