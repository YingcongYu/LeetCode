# Write a solution to find the users who have valid emails.

# A valid e-mail has a prefix name and a domain where:

# The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. 
# The prefix name must start with a letter.
# The domain is '@leetcode.com'.
# Return the result table in any order.


import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.contains('^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com')]
