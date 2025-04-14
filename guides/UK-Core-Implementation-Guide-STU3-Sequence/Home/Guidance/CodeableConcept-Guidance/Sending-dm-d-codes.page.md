## Sending dm+d codes 

Where a supplier is using the dm+d codes which does not contain any data at the Description Id level, then we would not expect the <a href="https://hl7.org/fhir/R4/extension-coding-sctdescid.html" class="external">coding-sctdescid</a> and {{pagelink:Extension-UKCore-CodingSCTDescDisplay,text: UKCore-CodingSCTDescDisplay}} extensions to be populated. Where the Description Id is available then these SHALL be included. 

The example below demonstrates how a dm+d code SHOULD be sent where there is no Description Id available.

<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Medication-Sn-Amoxicillin-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Medication-Sn-Amoxicillin-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Medication-Sn-Amoxicillin-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Medication-Sn-Amoxicillin-Example}}
</div>


---