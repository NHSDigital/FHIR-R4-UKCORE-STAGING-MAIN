## `reasonReference`

Reference to `Condition` or `Observation` that supports why the prescription is being written by reference. 

Where possible, it is expected that the resource being referenced SHOULD conform to one of the following UK Core profiles:
- {{pagelink:Profile-Condition}}
- {{pagelink:Profile-Observation}}

If the clinical system has recorded the reason for medication (often known as the *indication*) as either a `Condition` or `Observation` resource then a logical link to that resource has business benefit.

---
