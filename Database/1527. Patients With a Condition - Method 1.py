# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. 
# Type I Diabetes always starts with DIAB1 prefix.

# Return the result table in any order.


import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1')]
