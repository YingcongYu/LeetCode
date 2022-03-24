---Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
---In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, 
---then divide that number by the total number of players.

# Write your MySQL query statement below
SELECT round(sum(event_date = first_day + 1)/count(DISTINCT(player_id)), 2) AS fraction FROM
(SELECT player_id, event_date, min(event_date) over (PARTITION BY player_id) AS first_day FROM Activity) a
