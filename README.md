# FHIR-R4-UKCORE-STAGING-MAIN
This repository is maintained by [Interoperability Team]( https://nhsd-confluence.digital.nhs.uk/pages/viewpage.action?spaceKey=IOPS&title=Interoperability+Standards) Any queries contact us via [email]( interoperabilityteam@nhs.net).

UK Core Repository of FHIR Assets for HL7 FHIR® UK Core Implementation Guide [Simplifier project](https://simplifier.net/hl7fhirukcorer4).

## Developers Information
### Validation Service
This repository uses the HAPI FHIR plain server to validate all assets and examples. See [IOPS-FHIR-Test-Scripts](https://github.com/NHSDigital/IOPS-FHIR-Test-Scripts/blob/main/README.md#iops-validation) for more information.
#### Validation Options
The `options.json` file gives the ability to customise the FHIR validator with options such a strict validation, ignore specific folders and files, and error if meta data is present. See [IOPS-FHIR-Test-Scripts README](https://github.com/NHSDigital/IOPS-FHIR-Test-Scripts/blob/main/README.md#options) for more information. 
### GitHub Actions
Information on the IG content spell / link / error checking can be found within the [IOPS-FHIR-Test-Scripts repo](https://github.com/NHSDigital/IOPS-FHIR-Test-Scripts/tree/main/IGPageContentValidator).

Information on the QualityControlChecker can be within the [IOPS-FHIR-Test-Scripts repo](https://github.com/NHSDigital/IOPS-FHIR-Test-Scripts/tree/main/QualityControlChecker).

## Main Branch Status

FHIR Validation with Terminology Checks 

 [![NHSDigital IOPS Validation)](https://github.com/NHSDigital/FHIR-R4-UKCORE-STAGING-MAIN/actions/workflows/terminology.yml/badge.svg)](https://github.com/NHSDigital/FHIR-R4-UKCORE-STAGING-MAIN/actions/workflows/terminology.yml)

## Develop Branch Status

FHIR Validation with Terminology Checks 

 [![NHSDigital IOPS Validation)](https://github.com/NHSDigital/FHIR-R4-UKCORE-STAGING-MAIN/actions/workflows/terminology.yml/badge.svg?branch=develop)](https://github.com/NHSDigital/FHIR-R4-UKCORE-STAGING-MAIN/actions/workflows/terminology.yml?branch=develop)

