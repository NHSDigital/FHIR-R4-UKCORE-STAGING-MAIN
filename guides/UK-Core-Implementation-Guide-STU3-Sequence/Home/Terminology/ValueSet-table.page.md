<fql>
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
</script>