---
topic: Home-Guide
---
## Home 

---
## UK Core Implementation Guide Current Draft Build ##



<p>
<h3>Project Description and Scope</h3>

The FHIR UK Core Implementation Guide as a project aims to provide UK wide FHIR implementation guidance that has applicability across jurisdictions and care settings.
<br><br>
The guidance includes: 
<ul>
<li>FHIR resource components including Profiles and Extensions</li>
<li>FHIR terminology components including ValueSets and CodeSystems</li>
<li>Other general guidance useful to FHIR implementers in the UK</li>
</ul>
</p>
<p>
The guidance does not form the basis for a completely described deployable service in and of itself but is the basis from which other FHIR implementation guides can be derived.
</p>
<p>
The FHIR UK Core Implementation Guide shows only the differences between the base FHIR resources and the UK Core Profiles, and does not repeat base guidance. For this reason, it is expected to be used in conjunction with <a href="https://hl7.org/fhir/R4/" class="external">https://hl7.org/fhir/R4/</a>. 
<br><br>
The FHIR UK Core will never contradict the base FHIR standard but will restrict and extend resources, including amending of any ValueSets and CodeSystems, as necessary to bring in line the UK requirements. The content is relevant to the UK as a whole (4 Nations) although some nation specific CodeSystems are included and referenced in ValueSets. 
<br><br>
Any derived profiles will follow similar guidance, and will only show the differences between the base FHIR UK Core profile and the derived profile itself.
</p>

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Note about the label "STU3" for this FHIR implementation guide (IG)</h4>
The "3" refers to this being a third ballot of the UK Core, as a "Standard for Trial Use" (STU). It is based on, and provides extra UK specific guidance for use of, the international standard FHIR R4. The STU3 label of this Implementation Guide is not in any way related to earlier versions of FHIR itself, with coincidentally similar labels such as FHIR DSTU2 or FHIR STU3.
<br><br>
For additional guidance, see {{pagelink:Guidance-FHIRVersions}}.
</div>

---

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-folder-open-o"></i> Implementation Guidance Directory </h4>
The <a href="https://simplifier.net/guide/uk-core-implementation-guidance-directory?version=current">Implementation Guidance Directory</a> 
contains links to other guidance and documentation which is available to assist Implementers of the UK Core. 
This guidance covers items such as:
<ul>
<li>Version history and change control information.</li>
<li>Information around the design and approach of the UK Core.</li>
<li>Information to help identify clinical safety issues.</li>
<li>Further implementation guidance related to medication that has been developed by NHS England.</li>
</div>

---

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Reworded for clarity</h4>
<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Use of International and other FHIR IGs</h4>
Implementations are not restricted to only using the UK Core. International FHIR MAY be used to supplement the UK Core, for example where a particular resource is not yet supported by UK Core. Other FHIR IGs MAY be used as long as they conform to UK Core rules and guidance. 
<br><br>
</div>
</div>


---

### How to Read This Guide ###

This Guide is divided into several pages which are listed at the top of each page in the menu bar.
<ul>
<li>{{pagelink:Home-Guide}}: The home page provides the introduction and background for UK Core.</li>
<li>{{pagelink:Guidance-Sitemap}}: The Guidance page provides the sitemap of UK Core IG.
<ul>
  <li>{{pagelink:Guidance-DataType}}: This page gives guidance on the representation of constructs like Address, Name, and Telecom etc.</li>
  <li>{{pagelink:Guidance-CodeableConcept}}: This page gives guidance on the processing of CodeableConcept codes such as SNOMED CT concepts and descriptions.</li>
  <li>{{pagelink:Guidance-FHIRVersions}}: This page gives guidance on UK Core and FHIR Versions beyond R4.</li>
  <li>{{pagelink:Guidance-MustSupport}}: This page gives guidance on the use of MustSupport flags in UK Core.</li>
</ul>
</li>
<li>Profiles and Extensions: The  header for pages about Extensions and Profiles
<ul>
  <li>{{pagelink:Library-Extensions}}: The Extensions which have been defined for the UK Core.</li>
  <li>{{pagelink:Library-Extensions-All}}: This is the rendering of all Extensions defined for use within the UK Core.</li>
  <li>{{pagelink:Library-Profiles}}: The Profiles which have been defined for the UK Core.</li>
</ul>
</li>
<li>Terminology: This page lists all the Terminology assets defined as part of this Implementation Guide.
<ul>
  <li>{{pagelink:Library-ConceptMaps}}: This page lists all the ConceptMaps defined as part of this Implementation Guide.</li>
  <li>{{pagelink: Library-ValueSetsAndCodeSystems}}: This is the list of ValueSets and CodeSystems defined for use within the UK Core.</li>
  <li>{{pagelink:Library-ValueSets}}: This is the rendering of all ValueSets defined for use within the UK Core.</li>
  <li>{{pagelink:Library-CodeSystems}}: This is the rendering of all CodeSystems defined for use within the UK Core.</li>
</ul>
</li>
<li>Examples: The header for examples of UK Core FHIR assets.
<ul>
  <li>{{pagelink:Library-Examples-Index}}: This is the list of examples available in this implementation guide</li>
  <li>{{pagelink:Library-Examples-Profiles}}: This is the rendering of all Profile examples available in this implementation guide</li>
  <li>{{pagelink:Library-Examples-Extensions}}: This is the rendering of all Extension examples available in this implementation guide</li>
</ul>
</li>
<li>{{pagelink:Home-ContactUs}}:  How to Contact the key parties associated with this implementation guide.</li>
<li>{{pagelink:Home-Downloads}}:  List of downloads for this implementation guide</li>
<li>{{pagelink:Home-Glossary}}:  List of abbreviations and external links used in this implementation guide</li>
</ul>

---

<div markdown="span" class="alert alert-warning" role="alert"><h4 id="Licence"><i class="fa fa-legal"></i> Licensing and Publisher</h4>
<ul>
<li> 
Copyright &#169; 2021+ HL7 UK Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. HL7&#174; FHIR&#174; standard Copyright &#169; 2011+ HL7 The HL7&#174; FHIR&#174; standard is used under the FHIR license. You may obtain a copy of the FHIR license at https://www.hl7.org/fhir/license.html.
<li>
Developed and authored by UK Core Development Team and published by HL7 UK.
</ul>
</div> 

<div id="renderParent" title="The logos of organisations involved in developing and implementing UK Core">
{{render:ukcorelogos2023}}
</div>

---
