---Write an SQL query to report the device that is first logged in for each player.

---Return the result table in any order.

SELECT DISTINCT player_id, 
first_value(device_id) over (PARTITION BY player_id ORDER BY event_date) AS device_id
FROM Activity
