---Write an SQL query to report the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT pay_month, department_id, CASE
    WHEN round(avg(amount), 2) = round(company_avg, 2) THEN 'same'
    WHEN avg(amount) > company_avg THEN 'higher'
    WHEN avg(amount) < company_avg THEN 'lower' END AS comparison FROM
(SELECT amount, department_id, date_format(pay_date, '%Y-%m') AS pay_month,
 avg(Salary.amount) over (PARTITION BY date_format(pay_date, '%Y-%m')) AS company_avg
 FROM Salary JOIN Employee ON Salary.employee_id = Employee.employee_id) a
GROUP BY pay_month, department_id
