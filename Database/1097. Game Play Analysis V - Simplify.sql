---The install date of a player is the first login day of that player.

---We define day one retention of some date x to be the number of players whose install date is x and they logged back in on the day right after x, 
---divided by the number of players whose install date is x, rounded to 2 decimal places.

---Write an SQL query to report for each install date, the number of players that installed the game on that day, and the day one retention.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT a.event_date AS install_dt, count(a.player_id) AS installs, round(count(Activity.player_id)/count(a.player_id), 2) AS Day1_retention FROM 
(SELECT player_id, min(event_date) AS event_date FROM Activity GROUP BY player_id) a
LEFT JOIN Activity
ON a.player_id = Activity.player_id AND a.event_date + 1 = Activity.event_Date
GROUP BY a.event_date
