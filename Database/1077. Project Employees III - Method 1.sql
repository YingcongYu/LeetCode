--- Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        project_id
        ,Project.employee_id AS employee_id
        ,RANK() OVER (PARTITION BY project_id ORDER BY experience_years DESC) AS rk
    FROM Project
    JOIN Employee
    ON Project.employee_id = Employee.employee_id
)

SELECT
    project_id
    ,employee_id
FROM CTE
WHERE rk = 1
