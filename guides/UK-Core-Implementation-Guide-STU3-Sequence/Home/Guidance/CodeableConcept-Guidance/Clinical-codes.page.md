## Clinical codes 

<h3 id="clinical-codes-storage">Storage</h3>

When storing the item, the receiving system MAY choose to store any or all of the clinical codes associated with the item.

However, where the system supports SNOMED CT codes it SHALL store any SNOMED CT codes associated with the item.

Where the receiving system does not understand any of the supplied `coding.system` which a coding has been associated with the item (or no clinical codes were supplied), it MAY choose to record the item under a degraded code. The appropriate SNOMED CT degrade code SHOULD be used within the system to store the code.

<table class="assets" title="Degraded concept details">
<tr>
<th colspan="2">The following codes are available in SNOMED CT to represent degraded items and can be used when populating FHIR resources.</th>
</tr>
<tr>
<td>Degraded Drug Allergies</td>
<td>196461000000101 - Transfer-degraded drug allergy</td>
</tr>
<tr>
<td>Degraded Non-Drug Allergies</td>
<td>196471000000108 - Transfer-degraded non-drug allergy</td>
</tr>
<tr>
<td>Degraded Medications</td>
<td>196421000000109 - Transfer-degraded medication entry</td>
</tr>
<tr>
<td>Degraded Plan</td>
<td>196451000000104 - Transfer-degraded plan</td>
</tr>
<tr>
<td>Degraded Referral</td>
<td>196431000000106 - Transfer-degraded referral</td>
</tr>
<tr>
<td>Degraded Request</td>
<td>196441000000102 - Transfer-degraded request</td>
</tr>
<tr>
<td>Other degrade</td>
<td>196411000000103 - Transfer-degraded record entry</td>
</tr>
</table>

<br/>  

Where an item that is being degraded is contained within a resource that infers a particular type of degrade then the appropriate code SHALL be used e.g. a code in a FHIR medication resource SHALL use the ‘Transfer-degraded medication entry’ code. 

Clinical systems SHALL NOT attempt to infer a particular type of degrade code where there is no clear indication that a specific type of data has been degraded. In these scenarios the ‘Transfer-degraded record entry’ code SHALL be used.


<h3 id="clinical-codes-display">Display</h3>

When displaying the item to end users, it is the choice of the receiving system to design their system and user experience in a safe manner that best suits their users.

<h3 id="clinical-codes-propagation">Propagation</h3>

When propagating coded data to another system, the system which received the item MAY choose which clinical codes to include when sending the item.

If a receiving system receives a SNOMED CT code that it does not understand it SHOULD store this code and propagate it onwards if the data is exported. If systems decide to do this, a consideration that might be useful is what would happen if the data item is changed/edited.

---

