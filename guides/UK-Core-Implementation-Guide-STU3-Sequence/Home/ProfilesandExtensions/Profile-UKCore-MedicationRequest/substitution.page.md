## `substitution`


<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Important</h4>
Within UK healthcare, substitution is not the norm so the international FHIR definition where "_If nothing is specified substitution may be done._" does not align with UK healthcare prescribing best practice.<br/>

It could be unwise to assume all UK implementations will prevent substitution if not explicitly stated, especially if the same clinical system has been previously implemented outside the UK. <br/>

Within UK Core this element is mandatory and SHOULD have a boolean value of `false` to denote that substitution is not allowed, unless substitution can occur in a specific case.
</div>

### Allowing substitution

Where substitution to be be allowed, set to `true`. The inclusion of the coded reason is optional as the ValueSet defined in FHIR is of limited benefit to UK healthcare.

---