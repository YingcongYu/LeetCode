--- Write an SQL query to find the account_id of the accounts that should be banned from Leetflex. 
--- An account should be banned if it was logged in at some moment from two different IP addresses.

--- Return the result table in any order.


# Write your MySQL query statement below
SELECT DISTINCT
    t1.account_id AS account_id
FROM LogInfo t1, LogInfo t2
WHERE t1.account_id = t2.account_id
    AND t1.ip_address != t2.ip_address
    AND t1.login <= t2.login
    AND t1.logout >= t2.login
