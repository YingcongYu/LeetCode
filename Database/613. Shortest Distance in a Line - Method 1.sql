--- Write an SQL query to report the shortest distance between any two points from the Point table.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        x
        ,LAG(x) OVER (ORDER BY x) AS pre
    FROM Point
)

SELECT 
    MIN(ABS(x - pre)) AS shortest
FROM CTE
