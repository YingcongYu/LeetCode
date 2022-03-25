---The install date of a player is the first login day of that player.

---We define day one retention of some date x to be the number of players whose install date is x and they logged back in on the day right after x, 
---divided by the number of players whose install date is x, rounded to 2 decimal places.

---Write an SQL query to report for each install date, the number of players that installed the game on that day, and the day one retention.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT install_dt, count(*) AS installs, round(sum(retention)/count(*), 2) AS Day1_retention FROM
(SELECT player_id, sum(retention) AS retention FROM
 (SELECT *, CASE 
  WHEN min(event_date) over (PARTITION BY player_id) + 1 = event_date THEN 1 ELSE 0 END AS retention 
  FROM Activity) a
 GROUP BY player_id) b
JOIN
(SELECT player_id, min(event_date) AS install_dt FROM Activity GROUP BY player_id) c
ON b.player_id = c.player_id
GROUP BY install_dt
