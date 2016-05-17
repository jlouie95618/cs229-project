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
- HRR Details:
    HRR_ID
    HRR_Name
    State
- 2011_phys_hrr: 42 Total
    `Resident Population (2010)`
    `Total Physicians per 100,000 Residents (2011)`
    `Primary Care Physicians per 100,000 Residents (2011)`
    `Total Specialists per 100,000 Residents (2011)`
    `Medical Specialists per 100,000 Residents (2011)`
    `Hospital-Based Physicians per 100,000 Residents (2011)`
    `Surgeons per 100,000 Residents (2011)`
    `Resident Physicians per 100,000 Residents (2011)`
    `Allergists/ Immunologists per 100,000 Residents (2011)`
    `Anesthesiologists per 100,000 Residents (2011)`
    `Cardiologists per 100,000 Residents (2011)`
    `Cardiovascular/ Thoracic Surgeons per 100,000 Residents (2011)`
    `Critical Care Physicians per 100,000 Residents (2011)`
    `Dermatologists per 100,000 Residents (2011)`
    `Emergency Medicine Physicians per 100,000 Residents (2011)`
    `Endocrinologists per 100,000 Residents (2011)`
    `Family Practice Physicians per 100,000 Residents (2011)`
    `Geriatricians per 100,000 Residents (2011)`
    `General Surgeons per 100,000 Residents (2011)`
    `Gastroenterologists per 100,000 Residents (2011)`
    `Hematologists/ Oncologists per 100,000 Residents (2011)`
    `Infectious Disease Specialists per 100,000 Residents (2011)`
    `Internal Medicine Physicians per 100,000 Residents (2011)`
    `Neonatologists per 100,000 Residents (2011)`
    `Nephrologists per 100,000 Residents (2011)`
    `Neurosurgeons per 100,000 Residents (2011)`
    `Neurologists per 100,000 Residents (2011)`
    `Obstetrician/ Gynecologists per 100,000 Women Age 15-44 (2011)`
    `Ophthalmologists per 100,000 Residents (2011)`
    `Orthopedic Surgeons per 100,000 Residents (2011)`
    `Otolaryngologists per 100,000 Residents (2011)`
    `Pathologists per 100,000 Residents (2011)`
    `Pediatricians per 100,000 Residents (2011)`
    `Plastic & Reconstructive Surgeons per 100,000 Residents (2011)`
    `Psychiatrists per 100,000 Residents (2011)`
    `Pulmonologists per 100,000 Residents (2011)`
    `Radiologists per 100,000 Residents (2011)`
    `Radiation Oncologists per 100,000 Residents (2011)`
    `Physical Medicine/ Rehabilitation Physicians per 100,000 Residents (2011)`
    `Rheumatologists per 100,000 Residents (2011)`
    `Urologists per 100,000 Residents (2011)`
    `Vascular Surgeons per 100,000 Residents (2011)`
- PC_HRR_rates_2011: 11 Total
    `Number of Medicare beneficiaries (Part B eligible (2011):Overall`
    `Average annual percent of Medicare enrollees having at least one ambulatory visit to a primary care clinician (2011):Overall:Rate`
    `Number of diabetic Medicare enrollees age 65-75 (2011):Overall`
    `Average annual percent of diabetic Medicare enrollees age 65-75 having hemoglobin A1c test (2011):Overall:Rate`
    `Average annual percent of diabetic Medicare enrollees age 65-75 having eye examination (2011):Overall:Rate`
    `Average annual percent of diabetic Medicare enrollees age 65-75 having blood lipids (LDL-C) test (2011):Overall:Rate`
    `Number of female Medicare enrollees age 67-69 (2011):Overall`
    `Average percent of female Medicare enrollees age 67-69 having at least one mammogram over a two-year period (2011):Overall:Rate`
    `Number of Medicare beneficiaries (Part A eligible) (2011):Overall`
    `Leg amputations per 1,000 Medicare enrollees (2011):Overall:Rate`
    `Discharges for ambulatory care sensitive conditions per 1,000 Medicare enrollees (2011):Overall:Rate`
- post_discharge_events_hrr_11: 24 Total
    `Number of patients in medical cohort (2011)`
    `Medical:Percent readmitted within 30 days of discharge (2011):Rate`
    `Medical:Percent seeing a primary care clinician within 14 days of discharge to home (2011):Rate`
    `Medical:Percent having an ambulatory visit within 14 days of discharge to home (2011):Rate`
    `Medical:Percent having an emergency room visit within 30 days of discharge (2011):Rate`
    `Number of patients in surgical cohort (2011)`
    `Surgical:Percent readmitted within 30 days of discharge (2011):Rate`
    `Surgical:Percent seeing a primary care clinician within 14 days of discharge to home (2011):Rate`
    `Surgical:Percent having an emergency room visit within 30 days of discharge (2011):Rate`
    `Number of patients in CHF cohort (2011)`
    `CHF:Percent readmitted within 30 days of discharge (2011):Rate`
    `CHF:Percent seeing a primary care clinician within 14 days of discharge to home (2011):Rate`
    `CHF:Percent having an ambulatory visit within 14 days of discharge to home (2011):Rate`
    `CHF:Percent having an emergency room visit within 30 days of discharge (2011):Rate`
    `Number of patients in AMI cohort (2011)`
    `AMI:Percent readmitted within 30 days of discharge (2011):Rate`
    `AMI:Percent seeing a primary care clinician within 14 days of discharge to home (2011):Rate`
    `AMI:Percent having an ambulatory visit within 14 days of discharge to home (2011):Rate`
    `AMI:Percent having an emergency room visit within 30 days of discharge (2011):Rate`
    `Number of patients in pneumonia cohort (2011)`
    `Pneumonia:Percent readmitted within 30 days of discharge (2011):Rate`
    `Pneumonia:Percent seeing a primary care clinician within 14 days of discharge to home (2011):Rate`
    `Pneumonia:Percent having an ambulatory visit within 14 days of discharge to home (2011):Rate`
    `Pneumonia:Percent having an emergency room visit within 30 days of discharge (2011):Rate`
- DAP_hrr_data_2011:
    
