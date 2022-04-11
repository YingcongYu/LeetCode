---Write an SQL query to find the team size of each of the employees.

---Return result table in any order.

# Write your MySQL query statement below
SELECT employee_id, num AS team_size FROM Employee
JOIN
(SELECT team_id, count(*) AS num FROM Employee GROUP BY team_id) a
ON Employee.team_id = a.team_id
