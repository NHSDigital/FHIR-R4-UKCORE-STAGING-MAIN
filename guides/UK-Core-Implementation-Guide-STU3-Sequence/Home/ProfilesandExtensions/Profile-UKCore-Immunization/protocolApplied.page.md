## `protocolApplied`
The protocol (set of recommendations) being followed by the provider who administered the dose.

### `protocolApplied.targetDisease` 
It is recommended for international/EU interoperability that `Immunization.protocolApplied.targetDisease` is populated. The SNOMED CT concept SHOULD be from EU COVID-19 Diseases or Vaccine Target Diseases (GPS) - IPS

<table class="assets" title="Target Disease list">
<tr>
<th class="width50">Disease</th>
<th class="width50">UK SNOMED self</th>
<tr>
<td>COVID-19</td>
<td>840539006</td>
</tr>
<tr>
<td>Others</td>
<td>See "Vaccine Target Diseases (GPS) - IPS"</td>
</tr>
</table>
<br>

### `protocolApplied.doseNumberPositiveInt` 
Nominal position in a series of vaccines, N.B. This field will not always be reliable, therefore for Covid vaccinations, the vaccination procedure code or situation code SHOULD be used as that includes the dose number.
<br>
<br>

#### Example of `Immunization.protocolApplied` usage:
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
  <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Immunization-Sn-ProtocolApplied-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Immunization-Sn-ProtocolApplied-Example}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Immunization-Sn-ProtocolApplied-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Immunization-Sn-ProtocolApplied-Example}}
</div>

---