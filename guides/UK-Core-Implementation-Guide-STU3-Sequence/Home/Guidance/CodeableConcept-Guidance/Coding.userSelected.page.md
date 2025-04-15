## <code>{{page-title}}</code>

<div id="newAsset" markdown="span" class="alert alert-success" role="alert"><h4><i class="fa fa-star"></i> Important</h4>

This page has been created in STU3 due to the following [issue](https://simplifier.net/hl7fhirukcorer4/~issues/3308)</div>

`Coding.userSelected` is to differentiate between the codes directly chosen by the user compared to codes that are fixed, mapped code or other data enrichment functions.

If:

- a code is fixed, then `userSelected` SHALL = `false`,
- the code has been mapped, the original and mapped codes SHALL both be present,
- two coding values are present then `userSelected` SHALL be present on each,
- the code is computerised then `userSelected` SHALL = `false`,
- a single coding and no `userSelected` present then it MAY be inferred as `true`.
