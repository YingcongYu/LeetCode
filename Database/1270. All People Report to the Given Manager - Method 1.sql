---Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.

---The indirect relation between managers will not exceed three managers as the company is small.

---Return the result table in any order.


# Write your MySQL query statement below
SELECT e1.employee_id 
FROM Employees AS e1, 
     Employees AS e2, 
     Employees AS e3
WHERE e1.manager_id = e2.employee_id 
  AND e2.manager_id = e3.employee_id 
  AND e3.manager_id = 1 
  AND e1.employee_id != 1
