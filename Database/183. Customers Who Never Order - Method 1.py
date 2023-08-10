# Write a solution to find all customers who never order anything.

# Return the result table in any order.


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns = {'name':'Customers'}, inplace = True)
    return customers[~customers['id'].isin(orders['customerId'])][['Customers']]
