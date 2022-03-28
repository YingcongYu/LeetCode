---Write an SQL query to find the start and end number of continuous ranges in the table Logs.

---Return the result table ordered by start_id.

# Write your MySQL query statement below
SELECT min(log_id) AS start_id, max(log_id) AS end_id FROM
(SELECT *, row_number() over (ORDER BY log_id) AS row_id FROM Logs) a
GROUP BY log_id - row_id
