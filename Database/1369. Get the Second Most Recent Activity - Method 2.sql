---Write an SQL query to show the second most recent activity of each user.

---If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT username, activity, startDate, endDate FROM
(SELECT DISTINCT *, 
                rank() over (PARTITION BY username ORDER BY endDate DESC) AS ranking,
                count(*) over (PARTITION BY username) AS total
    FROM UserActivity) a
WHERE total = 1 OR ranking = 2
