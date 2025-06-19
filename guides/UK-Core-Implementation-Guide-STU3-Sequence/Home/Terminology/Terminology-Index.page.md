---
topic: Library-ValueSetsAndCodeSystems
---
## Terminology

---



## ValueSets and CodeSystems

This is the list of ValueSets and CodeSystems defined for use within the UK Core. 

Other ValueSets are usable if the binding strength is defined as extensible. For more information see
[HL7 FHIR - Binding Strengths](http://hl7.org/fhir/R4/terminologies.html#strength).

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-warning"></i> Important note regarding ValueSet expansions:</h4>
Within this release of the UK Core, ValueSet expansions have been incorporated into the ValueSets. For some ValueSets containing SNOMED CT or dm+d data in particular, the number of concepts were deemed too large to expand. It should also be remembered that the expansions of SNOMED CT data in particular represent the content available at the time the expansion was generated, but that this content can subsequently change. For an up to date and complete list of values, suppliers SHOULD consult the latest SNOMED CT terminology release.
</div>


<style>
 [class*=override] {
 	background-color:#f2f2f2;
	 }
</style>

<div class="tab">
  <button class="tablinks active" onclick="openTab(event, 'valuesets')">ValueSets</button>
  <button class="tablinks" onclick="openTab(event, 'codesystems')">CodeSystems</button>
</div>

<div id="valuesets" class="tabcontent" style="display:block">
  <h3>ValueSets</h3>
  {{page:ValueSet-table}}
</div>

<div id="codesystems" class="tabcontent" style="display:none">
  <h3>CodeSystems</h3>
  {{page:CodeSystem-table}}
</div>

<script>
let valueSetsProcessed = false;
let codeSystemsProcessed = false;

function openTab(evt, tabName) {
    // Hide all tab contents
    $(".tabcontent").hide();
    // Remove active class from all tab buttons
    $(".tablinks").removeClass("active");

    // Show selected tab and mark it active
    $("#" + tabName).show();
    $(evt.currentTarget).addClass("active");

    // Run table logic as needed
    if (tabName === 'valuesets') {
        processValueSetsTable();
    } else if (tabName === 'codesystems') {
        processCodeSystemsTable();
    }
}

function processValueSetsTable() {
    if (valueSetsProcessed) return;
    valueSetsProcessed = true;

    const queryString = window.location.search || "?version=current";
    const isUnpublished = window.location.pathname.includes(".page.md");
    const pageSuffix = isUnpublished ? ".page.md" : "";
    const guideTitleUrl = "{{guide-title}}"
        .replace(/[^a-zA-Z0-9 ]/g, "")
        .replace(/\s+/g, "-");

    const baseUrl = `https://simplifier.net/guide/${guideTitleUrl}/Home/`;
    const vsBase = `${baseUrl}terminology/valuesets/valueset-`;
    const csBase = `${baseUrl}terminology/codesystems/codesystem-`;

    const $table = $("#valuesets table.table-bordered");
    if ($table.length === 0) return;

    const $headerCells = $table.find("thead tr th");
    if ($headerCells.length >= 4) {
        $headerCells.eq(2).text("Composed of");
        $headerCells.eq(3).remove();
    }

    $table.find("tbody tr").each(function () {
        const $cells = $(this).find("td");
        if ($cells.length < 4) return;

        const $nameTd = $cells.eq(0);
        const $systemTd = $cells.eq(2);
        const $valueSetTd = $cells.eq(3);

        const nameText = $nameTd.text().trim();
        if (nameText.startsWith("UKCore")) {
            const assetLower = nameText.toLowerCase();
            const href = `${vsBase}${assetLower}${pageSuffix}${queryString}`;
            $nameTd.html(`<a href="${href}">${nameText}</a>`);
        }

        const combinedLinks = [];
        const linkify = (text) => {
            text.split(";").forEach(item => {
                const trimmed = item.trim();
                if (!trimmed) return;

                let displayText = trimmed;
                let href = trimmed;

                if (trimmed.startsWith("https://fhir.hl7.org.uk/")) {
                    const parts = trimmed.split("/");
                    const assetType = parts[3];
                    const assetName = parts[4];
                    if (assetType && assetName) {
                        const section = assetType.toLowerCase() === "codesystem" ? csBase
                                     : assetType.toLowerCase() === "valueset" ? vsBase
                                     : null;

                        if (section) {
                            const lowerAsset = assetName.toLowerCase();
                            href = `${section}${lowerAsset}${pageSuffix}${queryString}`;
                        }
                    }
                }

                combinedLinks.push(`<a href="${href}">${displayText}</a>`);
            });
        };

        linkify($systemTd.text());
        linkify($valueSetTd.text());

        const uniqueLinks = Array.from(
            new Map(combinedLinks.map(link => {
                const textMatch = link.match(/>(.*?)</);
                return textMatch ? [textMatch[1], link] : null;
            }).filter(Boolean))
        ).map(pair => pair[1]);

        $systemTd.html(uniqueLinks.join("<br>"));
        $valueSetTd.remove();
    });
}

function processCodeSystemsTable() {
    console.log("Processing CodeSystems table...");

    const $table = $("#codesystems table");
    if ($table.length === 0) return;

    const baseUrl = "https://simplifier.net/guide/uk-core-implementation-guide-stu3-sequence/home/terminology/codesystems/codesystem-";

    $table.find("tbody tr").each(function () {
        const $cells = $(this).find("td");
        if ($cells.length < 1) return;

        const codeSystemId = $cells.eq(0).text().trim();
        const href = `${baseUrl}${codeSystemId}`; // casing preserved

        $cells.eq(0).html(`<a href="${href}">${codeSystemId}</a>`);
    });
}


// Optionally trigger default tab on page load
$(document).ready(function () {
    processValueSetsTable(); // If ValueSets is shown by default
});
</script>


<!--<fql>
from
	ValueSet
where
    status !='retired'
select
	ValueSet: id, Status: status, CodeSystem: compose.include.system, ValueSets: compose.include.valueSet
order by
	id
distinct
</fql>

<script>
$(document).ready(function () {
    const queryString = window.location.search || "?version=current";

    // Detect if we're in an unpublished guide (which uses .page.md links)
    const isUnpublished = window.location.search.includes("version=current");
    const pageSuffix = isUnpublished ? ".page.md" : "";

    // Convert {{guide-title}} into URL-safe form
    const guideTitleUrl = "{{guide-title}}"
        .replace(/[^a-zA-Z0-9 ]/g, "")   // remove special characters
        .replace(/\s+/g, "-");           // convert spaces to hyphens

    const baseUrl = `https://simplifier.net/guide/${guideTitleUrl}/Home/`;
    const vsBase = `${baseUrl}terminology/valuesets/valueset-`;
    const csBase = `${baseUrl}terminology/codesystems/codesystem-`;

    const $table = $("table.table-bordered");
    if ($table.length === 0) return;

    // Update header
    const $headerCells = $table.find("thead tr th");
    if ($headerCells.length >= 4) {
        $headerCells.eq(2).text("Composed of");
        $headerCells.eq(3).remove(); // remove 4th column (valueSet)
    }

    // Process each row
    $table.find("tbody tr").each(function () {
        const $cells = $(this).find("td");
        if ($cells.length < 4) return;

        const $nameTd = $cells.eq(0);
        const $statusTd = $cells.eq(1);
        const $systemTd = $cells.eq(2);
        const $valueSetTd = $cells.eq(3);

        // --- Linkify name column if UKCore ---
        const nameText = $nameTd.text().trim();
        if (nameText.startsWith("UKCore")) {
            const assetLower = nameText.toLowerCase();
            const href = `${vsBase}${assetLower}${pageSuffix}${queryString}`;
            $nameTd.html(`<a href="${href}">${nameText}</a>`);
        }

        // --- Merge & linkify systems and valueSets ---
        const combinedLinks = [];

        const linkify = (text) => {
            text.split(";").forEach(item => {
                const trimmed = item.trim();
                if (!trimmed) return;

                let displayText = trimmed;
                let href = trimmed;

                if (trimmed.startsWith("https://fhir.hl7.org.uk/")) {
                    const parts = trimmed.split("/");
                    const assetType = parts[3];
                    const assetName = parts[4];

                    if (assetType && assetName) {
                        const section = assetType.toLowerCase() === "codesystem" ? csBase
                                     : assetType.toLowerCase() === "valueset"   ? vsBase
                                     : null;

                        if (section) {
                            const lowerAsset = assetName.toLowerCase();
                            href = `${section}${lowerAsset}${pageSuffix}${queryString}`;
                        }
                    }
                }

                combinedLinks.push(`<a href="${href}">${displayText}</a>`);
            });
        };

        linkify($systemTd.text());
        linkify($valueSetTd.text());

        // Remove duplicates (based on text shown)
        const uniqueLinks = Array.from(
            new Map(combinedLinks.map(link => {
                const textMatch = link.match(/>(.*?)</);
                return textMatch ? [textMatch[1], link] : null;
            }).filter(Boolean))
        ).map(pair => pair[1]);

        $systemTd.html(uniqueLinks.join("<br>"));
        $valueSetTd.remove(); // cleanup 4th column
    });
});
</script>-->













