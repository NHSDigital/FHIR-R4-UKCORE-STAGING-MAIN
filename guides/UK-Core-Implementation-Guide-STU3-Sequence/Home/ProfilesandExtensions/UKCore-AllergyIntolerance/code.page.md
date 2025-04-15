## `code`

Identifies the causative agent for the allergy or intolerance.

When recording an allergy to a medication substance, the provider system SHOULD use a dm+d concept class or alternatively, when the allergy is not recorded against a medication substance, the relevant set of SNOMED CT. These can be found within the {{pagelink:ValueSet-UKCore-AllergyCode}}.

### Using transfer degraded drug / non-drug allergy codes
<br>
Degraded drug allergy codes can be used in three scenarios, with examples.
<br>

#### 1. If only a text representation of the allergy is known. 

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block" data-Snippet="AllergyIntolerance.code[0]">
  <h3>Table View</h3>
{{table:UKCore-AllergyIntolerance-Sn-NonDrugAllergy-Example}}
</div>

<div id="Tree View" class="tabcontent" data-SnippetStart="code" data-SnippetEnd="patient">
  <h3>Tree View</h3>
{{tree:UKCore-AllergyIntolerance-Sn-NonDrugAllergy-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent" >
  <h3>XML View</h3>
{{xml:UKCore-AllergyIntolerance-Sn-NonDrugAllergy-Example}}
</div>

<div id="JSON View" class="tabcontent" data-SnippetStart="code" data-SnippetEnd="patient">
  <h3>JSON View</h3>
{{json:UKCore-AllergyIntolerance-Sn-NonDrugAllergy-Example}}
</div>
</div>
<br>

#### 2. If a text representation of the allergy is known but any associated coding is not recognised by the system.

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block" data-Snippet="AllergyIntolerance.code[0]">
  <h3>Table View</h3>
{{table:UKCore-AllergyIntolerance-Sn-DrugAllergy-Example}}
</div>

<div id="Tree View" class="tabcontent" data-SnippetStart="code" data-SnippetEnd="patient">
  <h3>Tree View</h3>
{{tree:UKCore-AllergyIntolerance-Sn-DrugAllergy-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent" data-SnippetStart="code" data-SnippetEnd="patient">
  <h3>XML View</h3>
{{xml:UKCore-AllergyIntolerance-Sn-DrugAllergy-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-AllergyIntolerance-Sn-DrugAllergy-Example}}
</div>
</div>

**Note:** “Septrin” is a long discontinued brand name of an antibiotic.


#### 3. If a pre-coordinated allergy code is known which this is not part of the permitted value set for causative agent defined above.

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block" data-Snippet="AllergyIntolerance.code[0]"
  <h3>Table View</h3>
{{table:UKCore-AllergyIntolerance-Sn-DrugAllergyToEggProtein-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-AllergyIntolerance-Sn-DrugAllergyToEggProtein-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-AllergyIntolerance-Sn-DrugAllergyToEggProtein-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-AllergyIntolerance-Sn-DrugAllergyToEggProtein-Example}}
</div>
</div>

---

### Handling of 'No known allergies'

There can be an explicit assertion of ‘No Known Allergies’ using the SNOMED CT 'No known allergy' hierarchy 716186003 | No known allergy.  The parent concept, or any child concept MAY be used.

#### Example of `AllergyIntolerance.code` usage for 'No known drug allergy':

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block" data-Snippet="AllergyIntolerance.code[0]">
  <h3>Table View</h3>
{{table:UKCore-AllergyIntolerance-Sn-NegHandlNoKnownAllergies-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-AllergyIntolerance-Sn-NegHandlNoKnownAllergies-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-AllergyIntolerance-Sn-NegHandlNoKnownAllergies-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-AllergyIntolerance-Sn-NegHandlNoKnownAllergies-Example}}
</div>
</div>
<br>

If other `AllergyIntolerance` resources exist in the patient record with a `AllergyIntolerance.clinicalStatus` of `active` then the system SHALL ignore the 'No Known Allergies' resource instance. The existence of recorded and active allergies takes precedence over instances of 'No Known Allergies' records.

---

### Use of plain text only 

The representation of the causative agent as text is supported within the FHIR standard but this SHOULD only be used as a last resort if a suitable coded term does not exist within the SNOMED CT terminology or if using a degraded allergy code is not appropriate.

### Use of `nullFlavor`

The UK Core recommendation is that the `nullFlavor` is **not used** for the causative agent, even though it is permitted within the FHIR standard.

---
