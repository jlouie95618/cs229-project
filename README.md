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


### Preliminary Features:

## 2011:

Our `y` values:
- pa_reimb_hrr_2011:
    - `Total Medicare reimbursements per enrollee (Parts A and B) (2011): Price, age, sex & race-adjusted`

For our feature vectors `x`:
- 2011_phys_hrr:
    1. 
- DAP_hrr_data_2011:
    1. 
- PC_HRR_rates_2011:
    1. `Number of Medicare beneficiaries (Part B eligible (2011): Overall`
    2. `Average annual percent of Medicare enrollees having at least one ambulatory visit to a primary care clinician (2011): Overall: Rate`
    3. `Number of diabetic Medicare enrollees age 65-75 (2011): Overall`
    4. `Average annual percent of diabetic Medicare enrollees age 65-75 having hemoglobin A1c test (2011): Overall: Rate`
    5. `Average annual percent of diabetic Medicare enrollees age 65-75 having eye examination (2011): Overall: Rate`
    6. `Average annual percent of diabetic Medicare enrollees age 65-75 having blood lipids (LDL-C) test (2011): Overall: Rate`
    7. `Number of female Medicare enrollees age 67-69 (2011): Overall`
    8. `Average percent of female Medicare enrollees age 67-69 having at least one mammogram over a two-year period (2011): Overall: Rate`
    9. `Number of Medicare beneficiaries (Part A eligible) (2011): Overall`
    10. `Leg amputations per 1,000 Medicare enrollees (2011): Overall: Rate`
     `Discharges for ambulatory care sensitive conditions per 1,000 Medicare enrollees (2011): Overall: Rate`
- post_discharge_events_hrr_11:
    1.  
