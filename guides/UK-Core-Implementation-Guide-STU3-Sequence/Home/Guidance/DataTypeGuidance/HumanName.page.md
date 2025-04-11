## `HumanName`

A name of a human with text, parts and usage information.

Names may be changed or repudiated. People may have different names in different contexts. Names may be divided into parts of different types that have variable significance depending on context, though the division into parts is not always significant. With personal names, the different parts might or might not be imbued with some implicit meaning; various cultures associate different importance with the name parts and the degree to which systems do care about name parts around the world varies widely.

The HumanName datatype has the following elements and this is an overview of the datatype with additional UK Core guidance. The full definition is available from the <a href="http://hl7.org/fhir/R4/datatypes.html#HumanName" class="external">FHIR standard</a>.

<table class="assets" title="HumanName DataType details">
<tr>
<th>Element</th>
<th>Type</th>
<th>Usage Guidance</th>
<th>Description</th>
</tr>
<tr>
<td><code>use</code></td>
<td>code</td>
<td>SHOULD be present</td>
<td>Identifies the purpose for this name. Allows the appropriate name for a particular context of use to be selected from among a set of names. Applications can assume that a name is current unless it explicitly says that it is temporary or old.</td>
</tr>
<td><code>text</code></td>
<td>string</td>
<td>MAY be present</td>
<td>Text representation of the full name. Specifies the entire name as it SHOULD be displayed e.g. on an application UI. This MAY be provided instead of or as well as the specific parts. Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part.</td>
</tr>
<tr>
<td><code>family</code></td>
<td>string</td>
<td>SHOULD be present</td>
<td>Family name (often called 'Surname')</td>
</tr>
<tr>
<td><code>given</code></td>
<td>string</td>
<td>SHOULD be present</td>
<td>Given names (not always 'first'). Includes middle names. This repeating element order: Given Names appear in the correct order for presenting the name</td>
</tr>
<tr>
<td><code>prefix</code></td>
<td>string</td>
<td>MAY be present</td>
<td>Parts that come before the name. This repeating element order: Prefixes appear in the correct order for presenting the name</td>
</tr>
<tr>
<td><code>suffix</code></td>
<td>string</td>
<td>MAY be present</td>
<td>Parts that come after the name. This repeating element order: Suffixes appear in the correct order for presenting the name</td>
</tr>
<tr>
<td><code>period</code></td>
<td>Period</td>
<td>MAY be present</td>
<td>Time period when name was/is in use</td>
</tr>
</table>

---

### Unstructured Names

`text`

Text representation of the name. This can be used if a structured name as detailed below cannot be supported. It MAY be present in addition to a structured name.

### Structured Names
Structured names SHOULD be used whenever possible as detailed below.

The following elements SHOULD be used to construct structured names:

<table class="assets" title="Structured Name details">
<tr>
<th>Element</th>
<th>Example</th>
</tr>
<tr>
<td><code>family</code></td>
<td>smith</td>
</tr>
<tr>
<td><code>given</code></td>
<td>John</td>
</tr>
<tr>
<td><code>prefix</code></td>
<td>Mr</td>
</tr>
<tr>
<td><code>suffix</code></td>
<td>MBE</td>
</tr>
</table>

---












