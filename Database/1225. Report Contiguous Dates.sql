---A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

---Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

---period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

---Return the result table ordered by start_date.


# Write your MySQL query statement below
WITH combine AS
(SELECT 'failed' AS state, fail_date AS date FROM Failed
 UNION ALL
 SELECT 'succeeded' AS state, success_date AS date FROM Succeeded)

SELECT state AS period_state, 
       min(date) AS start_date, 
       max(date) AS end_date 
FROM
(SELECT *, rank() over (ORDER BY date) - rank() over (PARTITION BY state ORDER BY date) AS 'interval'
 FROM combine WHERE date BETWEEN '2019-01-01' AND '2019-12-31') a
GROUP BY state, `interval`
ORDER BY date
