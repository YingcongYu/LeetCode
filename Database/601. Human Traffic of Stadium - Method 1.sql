-- Write an SQL query to display the records with three or more rows with consecutive id's, 
-- and the number of people is greater than or equal to 100 for each.

-- Return the result table ordered by visit_date in ascending order.


# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT
        *
        ,id - ROW_NUMBER() OVER () AS consecutive
    FROM Stadium
    WHERE people >= 100
),
CTE2 AS (
    SELECT
        *
        ,COUNT(*) OVER (PARTITION BY consecutive) AS validation
    FROM CTE1
)

SELECT
    id
    ,visit_date
    ,people
FROM CTE2
WHERE validation >= 3
ORDER BY visit_date
