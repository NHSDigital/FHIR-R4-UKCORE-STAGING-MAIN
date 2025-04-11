---
topic: Guidance-MustSupport
---
## Guidance

---

## {{page-title}}

### Mandatory Elements

Mandatory elements are elements with a minimum cardinality of 1 (min=1). When an element is Mandatory, the data is expected to always be present. The convention in this guide is to mark all min=1 elements as MustSupport unless they are nested under an parent element that is already marked as MustSupport.

### Must Support Elements

For querying and reading UK Core Profiles, MustSupport on any profile data element SHALL be interpreted as follows:

- UK Core suppliers / providers SHALL be capable of populating all data elements marked MustSupport, as part of the query results as specified by the Capability Statement of the server implementation.

- UK Core suppliers / providers SHALL populate data elements marked as MustSupport where they have the information.

- In situations where information on a particular data element is not present, and the reason for absence is unknown, UK Core suppliers / providers SHALL NOT include the data elements in the resource instance returned as part of the query results.

- UK Core consumers SHALL be capable of processing resource instances containing the data elements without generating an error or causing the application to fail. In other words, UK Core consumers SHOULD be capable of displaying the data elements for human use or storing it for other purposes.

- When querying UK Core server implementations, UK Core consumers SHALL interpret missing data elements within resource instances as data not present in the suppliers / providers system.

- UK Core consumers SHALL be able to process resource instances containing data elements asserting missing information.

- Elements nested under a data element that is marked MustSupport SHALL be treated as if they are also MustSupport