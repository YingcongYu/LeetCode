--- Write an SQL query to find the rows that contain the median salary of each company. 
--- While calculating the median, when you sort the salaries of the company, break the ties by id.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        *
        ,ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary) AS rk
        ,CEIL((COUNT(*) OVER (PARTITION BY company)+1) / 2) AS median_one
        ,FLOOR((COUNT(*) OVER (PARTITION BY company)+1) / 2) AS median_two
    FROM Employee
)

SELECT
    id
    ,company
    ,salary
FROM CTE
WHERE rk = median_one
    OR rk = median_two
