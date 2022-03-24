---Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
---In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, 
---then divide that number by the total number of players.

# Write your MySQL query statement below
SELECT round(sum(consecutive)/count(consecutive), 2) AS fraction FROM
(SELECT CASE WHEN second - event_date = 1 THEN 1 ELSE 0 END AS consecutive FROM
 (SELECT player_id, event_date, lead(event_date) over (PARTITION BY player_id ORDER BY event_date) AS second
  FROM Activity) a
 WHERE (player_id, event_date) IN 
 (SELECT player_id, min(event_date) AS `first` FROM Activity GROUP BY player_id)) b
