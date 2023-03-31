--- A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

--- Keep hiring the senior with the smallest salary until you cannot hire any more seniors.
--- Use the remaining budget to hire the junior with the smallest salary.
--- Keep hiring the junior with the smallest salary until you cannot hire any more juniors.
--- Write an SQL query to find the ids of seniors and juniors hired under the mentioned criteria.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT
        *
        ,SUM(salary) OVER (PARTITION BY experience ORDER BY salary) AS total
        ,ROW_NUMBER() OVER (ORDER BY experience, salary) AS rk
    FROM Candidates
),
CTE2 AS (
    SELECT
        *
        ,SUM(salary) OVER (ORDER BY rk, salary) AS remains
    FROM CTE1
    WHERE total <= 70000
)

SELECT
    employee_id
FROM CTE2
WHERE remains <= 70000
