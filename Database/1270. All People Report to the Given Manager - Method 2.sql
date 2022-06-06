---Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.

---The indirect relation between managers will not exceed three managers as the company is small.

---Return the result table in any order.


# Write your MySQL query statement below
WITH recursive CTE AS
(
SELECT employee_id FROM Employees WHERE manager_id = 1 AND employee_id != 1
UNION ALL
SELECT Employees.employee_id FROM Employees JOIN CTE ON CTE.employee_id = Employees.manager_id
)

SELECT employee_id FROM CTE
