---
topic: Library-Profiles
---
## Profiles and Extensions

---

## Profiles Index

This index contains all the profiles Clinically and Technically Assured for use with UK Core. 

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Important</h4>

The Profiles are rendered in several formats: 
<ul>
<li><b>Tree View - Snapshot:</b> a fully calculated tree view of the structure that is not dependent on any other structure</li>
<li><b>Tree View - Differential:</b> this tree view describes only the differences that the Profile makes relative to the structure definition (FHIR resource or profile) they constrain</li> 
<li><b>Tree View - Hybrid:</b> a hybrid view of the snapshot and differential views, with the differences highlighted</li>
<li><b>Detailed View:</b> a fully calculated form of the profile in table form</li>
<li><b>Table View:</b> a differential view of the profile, rendered in a tabular format</li>
<li><b>XML View:</b> a differential view of the profile, rendered in XML format</li>
<li><b>JSON View:</b> a differential view of the profile, rendered in JSON format</li> 
</ul>
In addition, each Profile also has the following: 
<ul>
<!--<li><b>Usage:</b> a listing of extensions and profiles that reference this asset</li>-->
<li><b>Examples:</b> one or more validated example of the profile in use</li>
<li><b>Feedback:</b> a link to Simplifier to raise issues regarding the asset</li> 
</ul>
<br>

<a href="https://hl7.org/fhir/R4/profiling.html" class="external">Further information from HL7 relating to profiling is available</a>.

</div>

<fql>
from
	StructureDefinition
where
	kind = 'resource'
select
	Profile:id, Purpose:purpose, Resource:type
</fql>

<script>
$(document).ready(function () {
    const queryString = window.location.search || "?version=current";

    // Detect if we're in unpublished preview mode (i.e., using .page.md links)
    const isUnpublished = window.location.pathname.includes(".page.md");
    const pageSuffix = isUnpublished ? ".page.md" : "";

    // Convert {{guide-title}} into a URL-safe format
    const guideTitleUrl = "{{guide-title}}"
        .replace(/[^a-zA-Z0-9 ]/g, "")
        .replace(/\s+/g, "-");

    const profileBase = `https://simplifier.net/guide/${guideTitleUrl}/home/profilesandextensions/`;

    const $table = $("table.table-bordered");
    if ($table.length === 0) return;

    $table.find("tbody tr").each(function () {
        const $cells = $(this).find("td");
        if ($cells.length === 0) return;

        const $resourceCell = $cells.eq(0);
        const resourceName = $resourceCell.text().trim();

        if (!resourceName || resourceName.toLowerCase() === "coding") return;

        // Remove sub-elements like .clinicalStatus
        const baseResource = resourceName.split(".")[0];

        const url = `${profileBase}UKCore-${baseResource}${pageSuffix}${queryString}`;
        $resourceCell.html(`<a href="${url}">${resourceName}</a>`);
    });
});
</script>


