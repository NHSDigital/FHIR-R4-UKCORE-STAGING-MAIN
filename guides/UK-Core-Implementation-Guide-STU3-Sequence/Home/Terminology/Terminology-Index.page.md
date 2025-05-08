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

<fql>
from
	ValueSet
select
	ValueSet: id, Status: status, CodeSystem: compose.include.system, ValueSets: compose.include.valueSet
order by
	id
distinct
</fql>

<script>
$(document).ready(function () {
    const queryString = window.location.search || "?version=current";

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
            const href = `${vsBase}${assetLower}.page.md${queryString}`;
            $nameTd.html(`<a href="${href}" target="_blank">${nameText}</a>`);
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
                            href = `${section}${lowerAsset}.page.md${queryString}`;
                        }
                    }
                }

                combinedLinks.push(`<a href="${href}" target="_blank">${displayText}</a>`);
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
</script>












