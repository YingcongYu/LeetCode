---Write an SQL query to find employees who have the highest salary in each of the departments.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT c.name AS Department, a.name AS Employee, b.Salary FROM Employee AS a JOIN
(SELECT max(salary) AS Salary, departmentId FROM Employee GROUP BY departmentId) b
ON a.departmentId = b.departmentId AND a.salary = b.Salary
JOIN Department AS c
ON a.departmentId = c.id
