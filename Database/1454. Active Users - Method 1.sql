--- Active users are those who logged in to their accounts for five or more consecutive days.

--- Write an SQL query to find the id and the name of active users.

--- Return the result table ordered by id.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        *
        ,DATE_SUB(login_date, INTERVAL DENSE_RANK() OVER (PARTITION BY id ORDER BY login_date) DAY) AS diff
    FROM Logins
)

SELECT DISTINCT
    CTE.id AS id
    ,name
FROM CTE, Accounts
WHERE CTE.id = Accounts.id
GROUP BY id, diff
HAVING COUNT(DISTINCT(login_date)) >= 5
