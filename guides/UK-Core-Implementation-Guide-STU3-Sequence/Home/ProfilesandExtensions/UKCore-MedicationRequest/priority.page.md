## `priority`

**Recommendation**: not to be used within an implementation - or used with caution.

The stating of a priority, in any business context including healthcare, is often de-valued as given the choice, every clinician wants medication urgently for their patients.

If <code>MedicationRequest.priority</code> is used, consider only initially supporting the <code>routine</code> and <code>urgent</code> request priorities, and set clear criteria for when a <code>MedicationRequest</code> should be marked and handled as <code>urgent</code>.

### Usage of the value "stat"

The <code>stat</code> request priority is potentially confusing as it has two meanings:

1. to indicate a "<i>here and now</i>" order going to pharmacy
2. used within a <code>MedicationRequest.dosageInstruction</code> can also mean "<i>give once immediately</i>".

Avoid using `stat` and `asap` where possible.

---
