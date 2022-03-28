---Write an SQL query to find the start and end number of continuous ranges in the table Logs.

---Return the result table ordered by start_id.

# Write your MySQL query statement below
SELECT a.log_id AS start_id, min(b.log_id) AS end_id FROM
(SELECT log_id FROM Logs WHERE log_id-1 NOT IN (SELECT * FROM Logs)) a
JOIN
(SELECT log_id FROM Logs WHERE log_id+1 NOT IN (SELECT * FROM Logs)) b
ON a.log_id <= b.log_id
GROUP BY a.log_id
