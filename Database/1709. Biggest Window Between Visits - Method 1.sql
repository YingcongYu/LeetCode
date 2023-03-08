--- Assume today's date is '2021-1-1'.

--- Write an SQL query that will, for each user_id, 
--- find out the largest window of days between each visit and the one right after it (or today if you are considering the last visit).

--- Return the result table ordered by user_id.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        *
        ,IFNULL(LEAD(visit_date) OVER (PARTITION BY user_id ORDER BY visit_date), DATE('2021-1-1')) AS next
    FROM UserVisits
)

SELECT
    user_id
    ,MAX(DATEDIFF(next, visit_date)) AS biggest_window
FROM CTE
GROUP BY user_id
