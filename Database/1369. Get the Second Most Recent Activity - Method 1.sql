---Write an SQL query to show the second most recent activity of each user.

---If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

---Return the result table in any order.

# Write your MySQL query statement below
WITH users
AS
(SELECT DISTINCT *, 
                rank() over (PARTITION BY username ORDER BY endDate DESC) AS ranking
    FROM UserActivity)
    
SELECT username, activity, startDate, endDate FROM users WHERE ranking = 2
UNION
SELECT DISTINCT * FROM UserActivity GROUP BY username HAVING count(*) = 1
