# Write a solution to find the second highest salary from the Employee table. 
# If there is no second highest salary, return null (return None in Pandas).


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    secondHighestSalary = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    
    return pd.DataFrame({'SecondHighestSalary' : [secondHighestSalary]})
