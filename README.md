# cs229-project
Machine learning project to attempt to predict Medicare costs based on non-traditional metrics

### Short Glossary of Terms:

* HRR = Hospital referral regions
    - regional market areas for tertiary medical care. Each HRR contains at least ONE hospital that performs major cardiovascular procedures and neurosurgery.

* HSA = Hospital service areas
    - local healthcare markets for hospital care. An HSA is a collection of ZIP codes whose residents receive most of their hospitalizations from the hospitals in that area
    - offers great regional granularity than HRR

* Part A = Medicare's hospital insurance program
    - covers inpatient care in hospitals, nursing homes, etc.

* Part B
    - The coverage provided by Medicare Part B includes medically necessary doctor's services, outpatient care, and other services that Part A does not cover. Part B also covers preventive services.

* Part D
    - prescription drug coverage insurance that is provided by private companies approved by Medicare

# Notes on Data Files:

## Medicare Spending

## Demographics

## Hospital & Physician Capacity Metrics

## Primary Care Access & Quality

## Chronically Ill Patient Care

## Patient Post Discharge Events

# Misc Notes:

We'll have to stratify by either HSA, HRR, county or state. The learning granularity has to be consistent so we can really only predict on one of the four categories. The thing is, certain factors/features only are applicable at a certain granularity level; this needs to be accounted for.