## `communication`

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Breaking Change</h4>
The binding on <code>Patient.communication.language</code> was changed, from <code>ValueSet-UKCore-HumanLanguage</code> and rebound to the Core-defined ValueSet All Languages, and it's strength has been set to <i>Required</i>, as a result of the UK Core STU2 Sequence ballot reconciliation actions. This action was agreed in order to align UK Core with known changes in future FHIR versions.
</div>

`Patient.communication` has the Core-defined Extension <a href="https://hl7.org/fhir/R4/extension-patient-proficiency.html" class="external">patient-proficiency</a>.

One or more instances of this element can be used to list the languages the patient is able to communicate in.  

The <code>Patient.communication.language</code> element has a <i>Required</i> binding to the Core-defined ValueSet <a href="https://hl7.org/fhir/R4/valueset-all-languages.html" class="external">All Languages</a> which is derived from <code>urn:ietf:bcp:47</code>.

#### An example of a patient with a single language

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Patient-Sn-SingleLanguage-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Patient-Sn-SingleLanguage-Example}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Patient-Sn-SingleLanguage-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Patient-Sn-SingleLanguage-Example}}
</div>
</div>

#### An example of a patient with multiple languages, with different proficiencies

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Patient-Sn-MultipleLanguages-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Patient-Sn-MultipleLanguages-Example}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Patient-Sn-MultipleLanguages-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Patient-Sn-MultipleLanguages-Example}}
</div>
</div>

#### An example of a patient with British Sign Language and Makaton

<div>
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Patient-Sn-Makaton-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Patient-Sn-Makaton-Example}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Patient-Sn-Makaton-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Patient-Sn-Makaton-Example}}
</div>
</div>

<br>
NOTE: Makaton is a communication tool with speech, signs, and symbols to enable people with disabilities or learning disabilities to communicate. As such, it is not recognised as a language in <code>urn:ietf:bcp:47</code>, and should be populated as a CodeableConcept.coding element alongside the <code>urn:ietf:bcp:47</code> parent language from which its country specific adaptation is derived.

---