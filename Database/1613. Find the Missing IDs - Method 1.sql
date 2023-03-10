--- Write an SQL query to find the missing customer IDs. 
--- The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.

--- Notice that the maximum customer_id will not exceed 100.

--- Return the result table ordered by ids in ascending order.


# Write your MySQL query statement below
WITH RECURSIVE CTE AS (
    SELECT 1 AS ids FROM Customers
    UNION
    SELECT ids+1 FROM CTE WHERE ids < (SELECT MAX(customer_id) FROM Customers)
)

SELECT * FROM CTE
WHERE ids NOT IN (SELECT customer_id FROM Customers)
