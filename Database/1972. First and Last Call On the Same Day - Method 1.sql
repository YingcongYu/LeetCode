--- Write an SQL query to report the IDs of the users whose first and last calls on any day were with the same person. 
--- Calls are counted regardless of being the caller or the recipient.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT *, DAY(call_time) AS day FROM Calls
    UNION
    SELECT recipient_id, caller_id, call_time, DAY(call_time) AS day FROM Calls
),
CTE2 AS (
    SELECT
        *
        ,RANK() OVER (PARTITION BY caller_id, day ORDER BY call_time) AS ascending
        ,RANK() OVER (PARTITION BY caller_id, day ORDER BY call_time DESC) AS descending
    FROM CTE1
)

SELECT DISTINCT
    a.caller_id AS user_id
FROM (SELECT caller_id, recipient_id FROM CTE2 WHERE ascending = 1) a
JOIN (SELECT caller_id, recipient_id FROM CTE2 WHERE descending = 1) b
ON a.caller_id = b.caller_id AND a.recipient_id= b.recipient_id
