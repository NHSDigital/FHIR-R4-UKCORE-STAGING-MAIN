## `authorizingPrescription`
This is a required element where the prescription is known and available when constructing the `MedicationDispense` resource.

**Supply Events**

Examples of where medications can be supplied without a prescription are shown below:

- Emergency supply
- Over The Counter (OTC)
- Patient Group Directions (PGD) 
- Minor Ailment Schemes.

**Dispense Events**

<div markdown="span" class="alert alert-warning" role="alert"><h4><i class="fa fa-info-circle"></i> Important</h4>
Where the prescription is available, it is recommended to reference via a URL - using the <code>MedicationDispense.authorizingPrescription.identifier</code> element rather than adding the <code>MedicationRequest</code> as a bundle - to avoid duplication.
</div>

Where possible, it is expected that the resource being referenced SHOULD conform to {{pagelink:UKCore-MedicationRequest}}

---
