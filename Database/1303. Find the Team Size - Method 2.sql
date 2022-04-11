---Write an SQL query to find the team size of each of the employees.

---Return result table in any order.

# Write your MySQL query statement below
SELECT employee_id, count(*) over (PARTITION BY team_id) AS team_size FROM Employee
