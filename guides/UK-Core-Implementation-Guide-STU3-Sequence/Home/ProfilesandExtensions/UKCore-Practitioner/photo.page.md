## `photo`

A photograph relating to the practitioner. This can be included as either:

- An attachment encoded as base64Binary with a relevant MIME contentType: image/png, image/jpg or image/jpeg preferred.

#### Example of `Practitioner.photo` usage:
<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
  <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
  <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
  <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>


<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Practitioner-Sn-Photo-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Practitioner-Sn-Photo-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Practitioner-Sn-Photo-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Practitioner-Sn-Photo-Example}}
</div>
<br>
and/or

- URL where the data can be found.

If both are used, the URL SHALL point to the same data as that encoded in the attachment.

---
