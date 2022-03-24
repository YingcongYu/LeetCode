---This Method does not match the requirement but fits for finding players that logged in for any 2 consecutive days.

---Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
---In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, 
---then divide that number by the total number of players.

# Write your MySQL query statement below
SELECT round(num/total, 2) AS fraction FROM
(SELECT count(DISTINCT(player_id)) AS num FROM
 (SELECT player_id, event_date, 
  CASE 
    WHEN lag(event_date) over (PARTITION BY player_id ORDER BY event_date) - event_date = -1 
    THEN 1 ELSE 0 
  END AS consecutive 
  FROM Activity) a
 WHERE consecutive = 1) 
(SELECT count(DISTINCT(player_id)) AS total FROM Activity)
