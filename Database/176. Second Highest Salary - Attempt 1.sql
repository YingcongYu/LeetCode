---Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

# Write your MySQL query statement below
SELECT
(SELECT salary FROM
(SELECT salary, rank() over (ORDER BY salary DESC) as A FROM Employee) a
WHERE A = 2 LIMIT 1) AS SecondHighestSalary
