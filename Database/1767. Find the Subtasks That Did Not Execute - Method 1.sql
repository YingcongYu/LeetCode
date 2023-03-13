--- Write an SQL query to report the IDs of the missing subtasks for each task_id.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH RECURSIVE CTE AS (
    SELECT task_id, subtasks_count AS subtask_id FROM Tasks
    UNION
    SELECT task_id, subtask_id-1 FROM CTE WHERE subtask_id > 1
)

SELECT
    *
FROM CTE
WHERE (task_id, subtask_id) NOT IN (SELECT * FROM Executed)
