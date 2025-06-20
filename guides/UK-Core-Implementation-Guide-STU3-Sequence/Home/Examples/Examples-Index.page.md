---
topic: Library-Examples-Index
---

# Examples Index

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Examples Usage</h4>
Whilst every effort has been made to ensure that the examples are correct and useful, they are not a normative part of the specification.
</div>

<div class="tab">
<button class="tablinks active" onclick="openTab(event, 'Profiles')">Profile Examples</button>
<button class="tablinks" onclick="openTab(event, 'Extensions')">Extension Examples</button>
</div>
<div id="Profiles" class="tabcontent" style="display:block">
<h3>Profile Examples</h3>


{{page:Home/Examples/Examples-Index-Profile.page.md}}
</div>

<div id="Extensions" class="tabcontent">
<h3>Extension Examples</h3>

{{page:Home/Examples/Examples-Index-Extension.page.md}}
</div>

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

        const isExtension = baseResource.toLowerCase().includes("extension");
        const subPath = isExtension ? "extension-examples" : "profile-examples";

        const url = `https://simplifier.net/guide/${guideTitleUrl}/home/examples/${subPath}/${baseResource}${pageSuffix}${queryString}`;
        $resourceCell.html(`<a href="${url}" target="_blank">${resourceName}</a>`);
    });
});
</script>