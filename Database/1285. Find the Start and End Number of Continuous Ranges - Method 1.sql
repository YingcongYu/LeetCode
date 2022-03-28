---Write an SQL query to find the start and end number of continuous ranges in the table Logs.

---Return the result table ordered by start_id.

# Write your MySQL query statement below
SELECT start_id, end_id FROM
(SELECT *, row_number() over (ORDER BY start_id) AS `rows` FROM
 (SELECT log_id AS start_id FROM
  (SELECT *, log_id - lag(log_id) over () AS diff FROM Logs) a
 WHERE diff != 1 OR diff IS NULL) b) e
JOIN
(SELECT *, row_number() over (ORDER BY end_id) AS `rows` FROM
 (SELECT log_id AS end_id FROM
  (SELECT *, lead(log_id) over () - log_id AS diff FROM Logs) c
 WHERE diff != 1 OR diff IS NULL) d) f
ON e.rows = f.rows
