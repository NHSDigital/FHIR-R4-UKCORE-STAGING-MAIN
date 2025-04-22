## <code>{{page-title}}</code>

This SHOULD be from {{pagelink:Valueset-UKCore-ProcedureCode}} if possible.

Regarding this ValueSet:

- The "procedure with explicit context" hierarchy within the ValueSet will include "referral by [person/service]" and "referral to [person/service]" concepts where there is potentially overlap with other elements of the ServiceRequest resource. If any such concepts are not appropriate for the `ServiceRequest.code` element then it would be expected that systems would recognise this rather than it being appropriate to explicitly exclude parts of this hierarchy within a ValueSet definition.

- The use of concepts within this ValueSet which include context depends to some extent on whether the lifecycle of the ServiceRequest resource is covered by other elements within the resource (e.g. status, intent, doNotPerform).

- It is understood that the Procedure hierarchy SHOULD cover all things that are likely to be requested e.g. enrolment on a care plan, referral for physiotherapy.

As the ServiceRequest resource is intended to be used for general referrals, there could be duplication of context carried within the `ServiceRequest.code` element as well as other elements but this is not considered an issue.

---
