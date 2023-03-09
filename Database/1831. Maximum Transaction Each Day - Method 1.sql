--- Write an SQL query to report the IDs of the transactions with the maximum amount on their respective day. 
--- If in one day there are multiple such transactions, return all of them.

--- Return the result table ordered by transaction_id in ascending order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        *
        ,RANK() OVER (PARTITION BY DAY(day) ORDER BY amount DESC) AS rk
    FROM Transactions
)

SELECT
    transaction_id
FROM CTE
WHERE rk = 1
ORDER BY transaction_id
