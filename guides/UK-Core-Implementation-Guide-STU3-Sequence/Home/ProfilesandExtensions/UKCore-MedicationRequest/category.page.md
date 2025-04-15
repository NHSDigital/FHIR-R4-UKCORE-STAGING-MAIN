## `category`


It is expected that any implementation will need to distinguish between medication orders for processes for dispensing and / or administration so this element is business required.

### Category values mapped to target use-cases

Example use cases for each category:

<table class="assets" title="Use cases for category">
    <thead>
        <tr>
            <th>Category</th>
            <th>Use-case</th>
            <th>Scenario</th>
        </tr>
    </thead>
    <tbody>
        <!-- inpatient -->
        <tr>
            <td><code>inpatient</code></td>
            <td>
                Inpatient medication requests, for a named patient, to be dispensed by the hospital pharmacy and intended for administration on a hospital ward.
            </td>
            <td>
                Patient Anne Teak is admitted as an inpatient is prescribed Amoxicillin 500mg orally three times daily for a suspected chest infection.
            </td>
        </tr>
        <!-- leave -->
        <tr>
            <td><code>leave</code></td>
            <td>
                Medication requests, for a named patient who is on short-term leave from an inpatient stay (but is not discharged), to be dispensed by the hospital pharmacy and intended for administration at home.
            </td>
            <td>
                Current inpatient Jackie Taitor is going home for weekend leave and is prescribed 3 days supply of Citalopram 20mg tablets one to be taken in the morning.
            </td>
        </tr>
        <!-- discharge -->
        <tr>
            <td><code>discharge</code></td>
            <td>
                Discharge medications requests, for a named patient, to be dispensed by the hospital pharmacy and issued on discharge for administration at home.
            </td>
            <td>
                Patient Bill Ding is discharged from hospital following an admission where they were diagnosed as being diabetic. They were prescribed 4 weeks quantity of Metformin 500mg tablets to take twice daily on an on-going basis. Their GP will be instructed to continue this course of medication within a discharge note.
            </td>
        </tr>
        <!-- outpatient -->
        <tr>
            <td><code>outpatient</code></td>
            <td>
                Outpatient medication requests, for a named patient, to be dispensed by the hospital pharmacy and intended for administration in the Outpatients department, Accident and Emergency department, or Day unit.
            </td>
            <td>
                Patient Moe DeGrasse is prescribed a Goserelin 3.6mg implant to be administered by IM injection in the Outpatients department on 1st May 2020.
            </td>
        </tr>
        <!-- community -->
        <tr>
            <td><code>community</code></td>
            <td>
                Outpatient medication requests, for a named patient, to be dispensed by the hospital pharmacy for administration at home.
            </td>
            <td>
                Patient Lorna Mower has attended the dermatology outpatients clinic and is prescribed Betamethasone 0.1% cream to be applied sparingly twice daily for 2 weeks.
            </td>
        </tr>
    </tbody>
</table>

<br/>

**Note**: A `community` medication request would trigger the printing and signing of a paper `FP10HNC` prescription, or (when implemented by the Trust) an electronic prescription sent to the NHS Electronic Prescription Service.

---