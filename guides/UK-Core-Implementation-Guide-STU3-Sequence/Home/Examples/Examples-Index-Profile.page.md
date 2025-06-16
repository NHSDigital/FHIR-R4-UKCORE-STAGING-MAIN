<fql>
from
	Example
select
	'id': id, 'Description': text.div
where
    id.contains('Extension').not()
    and id.contains('Sn-').not()
    and id.contains('Example')
</fql>

<script>
$(document).ready(function () {
    const queryString = window.location.search || "?version=current";

    // Detect if we're in unpublished preview mode (i.e., using .page.md links)
    const isUnpublished = window.location.search.includes("version=current");
    const pageSuffix = isUnpublished ? ".page.md" : "";

    // Convert {{guide-title}} into a URL-safe format
    const guideTitleUrl = "{{guide-title}}"
        .replace(/[^a-zA-Z0-9 ]/g, "")
        .replace(/\s+/g, "-");

    const profileBase = `https://simplifier.net/guide/${guideTitleUrl}/home/examples/profile-examples/`;

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

        const url = `${profileBase}${baseResource}${pageSuffix}${queryString}`;
        $resourceCell.html(`<a href="${url}" target="_blank">${resourceName}</a>`);
    });
});
</script>