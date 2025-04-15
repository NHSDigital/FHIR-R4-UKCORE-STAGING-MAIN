## `code`

All medication SHOULD be represented using the NHS dm+d terminology.

- The `Medication.code.coding.system` SHOULD be `https://dmd.nhs.uk`.
- The `Medication.code.coding.code` SHOULD be the NHS dm+d concept code.
- The `Medication.code.coding.display` SHOULD be the NHS dm+d concept description.

---