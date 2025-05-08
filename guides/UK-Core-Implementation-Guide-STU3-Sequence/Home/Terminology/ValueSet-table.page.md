<fql>
from
	ValueSet
select
	ValueSet: id, Status: status, CodeSystem: compose.include.system, name
order by
	name
distinct
</fql>

<!-- JQuery to seperate CodeSystems onto seperate lines per ValueSet and remove dulicate CodeSystems-->
<script>
$(document).ready(function () {
  $(".table tbody tr").each(function () {
    var $systemCell = $(this).find("td:eq(2)");
    var $links = $systemCell.find("a");

    let seen = new Set();
    let uniqueLinks = [];

    $links.each(function () {
      var href = $(this).attr("href");
      if (!seen.has(href)) {
        seen.add(href);
        uniqueLinks.push($(this).clone());
      }
    });

    if (uniqueLinks.length > 1) {
      $systemCell.empty();
      uniqueLinks.forEach(function ($link, index) {
        if (index > 0) $systemCell.append("<br>");
        $systemCell.append($link);
      });
    }
  });
});

function rewriteFQLTableLinks() {
    const fullUrl = window.location.href;
    const guideBase = fullUrl.split("/home/")[0] + "/home/";
    const queryString = window.location.search || "";

    $("table.table tbody tr").each(function () {
        const $tds = $(this).find("td");
        const $nameTd = $tds.eq(0);
        const $statusTd = $tds.eq(1);
        const $systemTd = $tds.eq(2);

        // --- Update 'name' column to be a link to the ValueSet page ---
        const nameValue = $nameTd.text().trim();
        if (nameValue.startsWith("UKCore")) {
            const assetLower = nameValue.toLowerCase();
            const href = `${guideBase}terminology/valuesets/valueset-${assetLower}.page.md${queryString}`;
            $nameTd.html(`<a href="${href}" target="_blank">${nameValue}</a>`);
        }

        // --- Rewrite 'system' column: remove duplicates, format links, split by <br> ---
        const $links = $systemTd.find("a");
        if ($links.length === 0) return;

        const seen = new Set();
        const newSystemContent = [];

        $links.each(function () {
            const $a = $(this);
            const text = $a.text().trim();
            if (seen.has(text)) return;
            seen.add(text);

            let finalHref = $a.attr("href"); // fallback

            if (text.startsWith("https://fhir.hl7.org.uk/")) {
                const urlParts = text.split("/");
                const assetType = urlParts[3]; // CodeSystem or ValueSet
                const assetName = urlParts[4]; // UKCore-...

                if (assetType && assetName) {
                    const sectionPath = (assetType.toLowerCase() === "codesystem")
                        ? "terminology/codesystems/codesystem-"
                        : (assetType.toLowerCase() === "valueset")
                            ? "terminology/valuesets/valueset-"
                            : null;

                    if (sectionPath) {
                        const lowerAsset = assetName.toLowerCase();
                        finalHref = `${guideBase}${sectionPath}${lowerAsset}.page.md${queryString}`;
                    }
                }
            }

            newSystemContent.push(`<a href="${finalHref}" target="_blank">${text}</a>`);
        });

        $systemTd.html(newSystemContent.join("<br>"));
    });
}

$(document).ready(function () {
    rewriteFQLTableLinks();
});
</script>