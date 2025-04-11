## `Address`

An address expressed using postal conventions (as opposed to GPS or other location definition formats). This datatype may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery. There are a variety of postal address formats defined around the world.

The Address datatype has the following elements and this is an overview of the datatype with additional UK Core guidance. The full definition is available from the <a href="http://hl7.org/fhir/R4/datatypes.html#Address" class="external">FHIR standard</a>.

<div markdown="span" class="alert alert-warning" role="alert"><i class="fa fa-info-circle"></i> The address datatype has a UK Core extension {{pagelink:Extension-UKCore-AddressKey}}. This extension extends the Address datatype to support the exchange of the type of address key and the address key value.
</div>

<table class="assets" title="Address DataType details">
<tr>
<th>Element</th>
<th>type</th>
<th>Usage Guidance</th>
<th>Description</th>
</tr>
<tr>
<td><code>use</code></td>
<td>code</td>
<td>SHOULD be present</td>
<td>The purpose of this address</td>
</tr>
<tr>
<td><code>type</code></td>
<td>code</td>
<td>SHOULD be present</td>
<td>The type of address</td>
</tr>
<tr>
<td><code>text</code></td>
<td>string</td>
<td>MAY be present</td>
<td>Text representation of the address</td>
</tr>
<tr>
<td><code>line</code></td>
<td>string</td>
<td>SHOULD be present</td>
<td>Street name, number, direction & P.O. Box etc.This repeating element order: The order in which lines SHOULD appear in an address label</td>
</tr>
<tr>
<td><code>city</code></td>
<td>string</td>
<td>SHOULD be present</td>
<td>Name of city, town etc</td>
</tr>
<tr>
<td><code>district</code></td>
<td>string</td>
<td>MAY be present</td>
<td>District name (aka county)</td>
</tr>
<tr>
<td><code>state</code></td>
<td>string</td>
<td>MAY be present</td>
<td>Sub-unit of country (abbreviations ok)</td>
</tr>
<tr>
<td><code>postalCode</code></td>
<td>string</td>
<td>SHOULD be present</td>
<td>postalCode - Code for area</td>
</tr>
<tr>
<td><code>country</code></td>
<td>string</td>
<td>MAY be present</td>
<td>Country (e.g. can be ISO 3166 2 or 3 letter code)
</td>
</tr>
<tr>
<td><code>period</code></td>
<td>Period</td>
<td>MAY be present</td>
<td>Time period when the address was/is in use</td>
</tr>
</table>

---

### Unstructured Addresses

`text`

Text representation of the address. This SHOULD only be used if a structured address as detailed below cannot be supported. It MAY be present in addition to a structured address.

### Structured Addresses
Structured addresses SHOULD be used whenever possible as detailed below.

### `line`

Street name, number, direction & P.O. Box etc.
This repeating element order: The order in which lines SHOULD appear in an address label. Parts of the address that have distinct elements listed below SHOULD not appear in the address line elements.

The following elements SHOULD be used to carry the associated information. 
- `city` - Name of city, town etc
- `district` - District name (aka county)
- `state` - Sub-unit of country (abbreviations ok)
- `postalCode` - Postal code for area
- `country` - Country (e.g. can be ISO 3166 2 or 3 letter code)

---


	





	
