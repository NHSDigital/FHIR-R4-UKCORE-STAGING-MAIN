## Rules for populating legacy coding 

### Read Code 

All Read Codes SHOULD be represented using a full five characters.
- Where 4-byte codes are used these SHALL be preceded by a full-stop as in the NHS Clinical Terms superset (e.g. 4-byte code "6521" is represented as ".6521").
- Trailing full-stops are significant and SHALL be included (e.g. "H43" is not a valid Read Code and SHALL be represented in full as "H43..").
    - Care should be taken in any environment where a Read Code may have been subjected to auto-correction because:
        - Upper/lower case is significant
        - Conversion of a sequence of three full-stops "..." to a single "…" (ASCII Hex "85" Unicode Hex "2026") special character occurs in some environments and creates invalid Read Codes.

### Read Code version 2 term code 

Read Codes Version 2 uses a "Term Code" to distinguish between some alternative terms associated with the same Read Code. A Term Code is represented as a two-digit string and is only unique within the context of a single Read Code. 
 
It is now widely recognised that many of the terms associated with a Read Code are not true synonyms. This issue was partially resolved in NHS Clinical Terms Version 3 and further disambiguation has occurred in development of SNOMED CT. However, in the meantime where Term Codes are stored these SHOULD be communicated with the Read Code.
 
A Read Code + Term Code combination is communicated as a single seven character code. Thus the code "7001200" represents the Term Code "00" associated with the Read Code "70012".
 
**Note:** that this specification requires the term to be conveyed in the message in addition to any coded representation. Therefore, safe communication is not dependent on use of the Term Code in all systems. Therefore, a sending system that does not support Term Codes for a particular item of information SHOULD NOT send a Term Code. Similarly a receiving system that does not support Term Code storage MAY ignore the Term Code when constructing a record entry. However, where a sending system stores the Term Code this SHOULD be included in the message and where a receiving system stores the Term Code this SHOULD be retrieved from the message.

### NHS Clinical Terms Version 3 – Term Id 

In NHS Clinical Terms Version 3 the Term Id is a five character string that uniquely identifies an associated term (or set of two or three terms of alternative lengths). Although it is globally unique it says nothing about the associated concept and thus SHALL be combined with the Read Code. There are no plans to use the Term Id in NHS Clinical Terms Version 3 and thus inclusion of Term Id is not permitted. 

#### Example of `Condition.code` usage for legacy coding:

<div class="tab">
 <button class="tablinks active" onclick="openTab(event, 'Table View')">Table View</button>
 <button class="tablinks" onclick="openTab(event, 'Tree View')">Tree View</button>
 <button class="tablinks" onclick="openTab(event, 'XML View')">XML View</button>
 <button class="tablinks" onclick="openTab(event, 'JSON View')">JSON View</button>
</div>

<div id="Table View" class="tabcontent" style="display:block">
  <h3>Table View</h3>
{{table:UKCore-Extension-CodingSCT-MoleOfSkin-Example}}
</div>

<div id="Tree View" class="tabcontent">
  <h3>Tree View</h3>
{{tree:UKCore-Extension-CodingSCT-MoleOfSkin-Example, expand:9}}
</div>

<div id="XML View" class="tabcontent">
  <h3>XML View</h3>
{{xml:UKCore-Extension-CodingSCT-MoleOfSkin-Example}}
</div>

<div id="JSON View" class="tabcontent">
  <h3>JSON View</h3>
{{json:UKCore-Extension-CodingSCT-MoleOfSkin-Example}}
</div>

---
