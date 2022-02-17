---Write an SQL query to report the device that is first logged in for each player.

---Return the result table in any order.

SELECT Activity.player_id, Activity.device_id FROM Activity
JOIN
(SELECT player_id, min(event_date) AS login FROM Activity
GROUP BY player_id) a
on a.login = Activity.event_date AND a.player_id = Activity.player_id
