---Write an SQL query to find the employees who earn more than their managers.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT b.name AS  Employee FROM Employee a
INNER JOIN Employee b
ON a.id = b.managerId
WHERE a.salary < b.salary


# Write your MySQL query statement below
SELECT b.name AS  Employee FROM Employee a
INNER JOIN Employee b
ON a.id = b.managerId
AND a.salary < b.salary
