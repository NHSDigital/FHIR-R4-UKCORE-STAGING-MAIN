<fql>
from
  Instance
where
  id.contains(%examples) and id.contains('Sn-').not()
select
  id, text.div
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

    function processExamplesTable() {
        const $examplesTab = $("#examples.tabcontent");
        const $table = $examplesTab.find("table.table-bordered");

        if ($table.length === 0) return;

        // Remove table header
        $table.find("thead").remove();

        $table.find("tbody tr").each(function () {
            const $cells = $(this).find("td");
            if ($cells.length === 0) return;

            const $resourceCell = $cells.eq(0);
            const resourceName = $resourceCell.text().trim();

            if (!resourceName || resourceName.toLowerCase() === "coding") return;

            const baseResource = resourceName.split(".")[0];
            const isExtension = baseResource.toLowerCase().includes("extension");
            const subPath = isExtension ? "extension-examples" : "profile-examples";

            const url = `https://simplifier.net/guide/${guideTitleUrl}/home/examples/${subPath}/${baseResource}${pageSuffix}${queryString}`;
            $resourceCell.html(`<a href="${url}" target="_blank">${resourceName}</a>`);
        });
    }

    // Process immediately
    processExamplesTable();

    // Hook into tab switch to re-process in case content is dynamic
    $('button.tablinks').on('click', function () {
        const targetId = $(this).attr('onclick').match(/'([^']+)'/)[1];
        if (targetId === "examples") {
            setTimeout(processExamplesTable, 50);
        }
    });
});
</script>
