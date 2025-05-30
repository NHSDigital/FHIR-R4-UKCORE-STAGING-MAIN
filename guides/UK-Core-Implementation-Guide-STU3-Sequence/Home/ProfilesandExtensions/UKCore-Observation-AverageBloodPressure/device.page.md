## <code>{{page-title}}</code>

The resource being referenced SHOULD conform to one of the following:

- {{pagelink:UKCore-Device-BloodPressure}}
- [DeviceMetric Resource](https://hl7.org/fhir/R4/devicemetric.html)

If the `Observation.device` is a reference to a {{pagelink:UKCore-Device-BloodPressure}}, it is expected that the {{pagelink:Extension-UKCore-CuffSize}} SHOULD be present, and populated with a SNOMED CT Concept Id from {{pagelink:ValueSet-UKCore-BloodPressure-CuffSize}}.

---