---Write an SQL query to find the salaries of the employees after applying taxes. Round the salary to the nearest integer.

---The tax rate is calculated for each company based on the following criteria:

---0% If the max salary of any employee in the company is less than $1000.
---24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
---49% If the max salary of any employee in the company is greater than $10000.

---Return the result table in any order.

# Write your MySQL query statement below
WITH Top AS (SELECT *, max(salary) OVER (PARTITION BY company_id) AS top FROM Salaries)

SELECT company_id, employee_id, employee_name, 
    CASE WHEN top < 1000 THEN salary
         WHEN top BETWEEN 1000 AND 10000 THEN round(salary*(1 - 0.24))
         WHEN top > 10000 THEN round(salary*(1 - 0.49)) END AS salary
FROM Top
