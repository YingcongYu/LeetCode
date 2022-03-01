---A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

---Write an SQL query to find the employees who are high earners in each of the departments.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT b.name AS Department, a.name AS Employee, a.salary AS Salary FROM
(SELECT salary, name,departmentId, dense_rank() over (PARTITION BY departmentId ORDER BY salary DESC) AS ranking FROM Employee) a
JOIN Department AS b ON a.departmentId = b.id
WHERE ranking <= 3
