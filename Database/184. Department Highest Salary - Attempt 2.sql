---Write an SQL query to find employees who have the highest salary in each of the departments.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT a.name AS Department, b.name AS Employee, b.salary AS Salary FROM Department AS a
JOIN
(SELECT name, departmentId, salary, rank() over (PARTITION BY departmentId ORDER BY salary DESC) AS ranking FROM Employee) b
ON a.id = b.departmentId
WHERE b.ranking = 1
