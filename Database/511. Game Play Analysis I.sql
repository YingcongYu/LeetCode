---Write an SQL query to report the first login date for each player.

---Return the result table in any order.

SELECT player_id, min(event_date) AS first_login FROM Activity
GROUP BY player_id
