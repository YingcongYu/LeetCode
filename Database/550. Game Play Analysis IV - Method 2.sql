---Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
---In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, 
---then divide that number by the total number of players.

# Write your MySQL query statement below
SELECT round(sum(CASE WHEN event_date - first_day = 1 THEN 1 ELSE 0 END)/count(DISTINCT(Activity.player_id)), 2) AS fraction 
FROM Activity JOIN
(SELECT player_id, min(event_date) AS first_day FROM Activity GROUP BY player_id) a
ON a.player_id = Activity.player_id
