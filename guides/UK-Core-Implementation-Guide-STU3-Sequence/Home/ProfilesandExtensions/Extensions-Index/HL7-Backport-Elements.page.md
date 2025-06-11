---
topic: Library-Extensions-PreAdopt
---
## Pre-adopted R5/R6 Elements


The following <a href="https://hl7.org/fhir/versions.html#extensions" class="external">R5 elements</a> have been agreed as suitable to be included for use with the UK Core {{pagelink:Library-Profiles,text:Profiles}} because the use case for pre-adopting an R5 element as an Extension, rather than creating a UK Core specific extension is fully met.

<div class="NewAddedItem">Rules and examples for creating and using extensions between versions can be found within <a href="https://build.fhir.org/versions.html#extensions class="external">FHIR Build - Version Management Policy</a>.</div><br>


<i>As of 19/05/2023, the package to enable pre-adopted elements to function as per the guidance, is not available. To enable rendering and validation of these pre-adopted elements, we have provided UK Core proxy extensions, as per the current threads on <a href="https://chat.fhir.org/#narrow/stream/179166-implementers/topic/R5.20Extensions.20for.20R4.3F" class="external">chat.fhir.org</a>, with the R5 canonical urls. These proxy extensions will be retired once the HL7 package is released.</i>

<fql>
from StructureDefinition
where
    type = 'Extension' 
    and status != 'retired'
    and url.contains('http://hl7.org/fhir/')
select
    'Id': id, 'Context of Use':context.expression, 'url': url,'Status':status
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