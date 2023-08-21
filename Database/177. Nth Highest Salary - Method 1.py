# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.


import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending = False)
    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    return pd.DataFrame({'Nth Highest Salary' : [sorted_salaries.iloc[N - 1]]})
