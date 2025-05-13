---
topic: UK-Core-Extensions
---
## UK Core Extensions

<p>The Extensions listed below have been defined as UK Core extensions. Also included in this library are some HL7 core-defined extensions which have been added to the UK Core profiles because they have been deemed to be "core" to UK FHIR data exchanges. These will have a page with guidance on usage in the UK and examples to illustrate usage.</p>

<p>Note: implementers of UK Core MAY use any HL7 core-defined extension from the HL7 standard regardless of whether the extension is included in this implementation guide. The list of core-defined extensions in FHIR R4 is available in the <a href="http://hl7.org/fhir/R4/extensibility-registry.html" class="external">HL7 Core-defined Extension Registry</a>.</p>

<p>Implementers of the UK Core profiles MAY also create their own Extensions where required, but are encouraged to engage with the UK Core development process to ensure that there is not an existing suitable extension available, and to assist in  guidance around the use of an extension with the UK Core, and with wider use by the UK FHIR Community.</p>



<fql>
from StructureDefinition
where
    type = 'Extension' and status != 'retired'
select
    'Id': id, 'Context of Use':context.expression, 'Status':status
</fql>


<script>
$(document).ready(function () {
    const queryString = window.location.search || "?version={{guide-version}}";
    
    // Detect if we are in a preview/unpublished guide by checking if .page.md is in the URL
    const isUnpublished = window.location.pathname.includes(".page.md");

    const extensionBase = "https://simplifier.net/guide/uk-core-implementation-guide-stu3-sequence/home/profilesandextensions/extensionlibrary/";
    const profileBase = "https://simplifier.net/guide/UK-Core-Implementation-Guide-STU3-Sequence/Home/ProfilesandExtensions/UKCore-";

    const extSuffix = isUnpublished ? ".page.md" : ""; // only use .page.md in preview

    const $table = $("table.table-bordered");
    if ($table.length === 0) return;

    $table.find("tbody tr").each(function () {
        const $cells = $(this).find("td");
        if ($cells.length < 2) return;

        const $extensionCell = $cells.eq(0);
        const $profilesCell = $cells.eq(1);

        // --- Extension Column ---
        const extText = $extensionCell.text().trim();
        if (extText) {
            const extHref = `${extensionBase}${extText}${extSuffix}${queryString}`;
            $extensionCell.html(`<a href="${extHref}">${extText}</a>`);
        }

        // --- Profiles Column ---
        const profilesRaw = $profilesCell.text().trim().split(";");
        const profileLinks = profilesRaw.map(profile => {
            const clean = profile.trim();
            if (!clean) return "";

            if (clean === "Coding") return "Coding";

            const resource = clean.split(".")[0];
            const profileHref = `${profileBase}${resource}${queryString}`;
            return `<a href="${profileHref}">${clean}</a>`;
        }).filter(link => link);

        $profilesCell.html(profileLinks.join("<br>"));
    });
});
</script>



---