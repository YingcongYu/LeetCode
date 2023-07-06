-- Write an SQL query to calculate the cumulative salary summary for every employee in a single unified table.

-- The cumulative salary summary for an employee can be calculated as follows:
--   For each month that the employee worked, sum up the salaries in that month and the previous two months. 
--     This is their 3-month sum for that month. If an employee did not work for the company in previous months, their effective salary for those months is 0.
--   Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
--   Do not include the 3-month sum for any month the employee did not work.
  
-- Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.


# Write your MySQL query statement below
SELECT
    id
    ,month
    ,SUM(salary) OVER (PARTITION BY id ORDER BY month RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS salary
FROM Employee
WHERE (id, month) NOT IN (SELECT id, MAX(month) FROM Employee GROUP BY id)
ORDER BY id, month DESC
