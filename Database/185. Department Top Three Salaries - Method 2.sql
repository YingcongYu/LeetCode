---A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

---Write an SQL query to find the employees who are high earners in each of the departments.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary
FROM Employee AS e1, Employee AS e2, Department AS d
WHERE e2.departmentId = d.id AND e1.salary <= e2.salary AND e1.departmentId = e2.departmentId
GROUP BY Department, Employee HAVING count(DISTINCT e2.salary) <= 3
