---The average activity for a particular event_type is the average occurences across all companies that have this event.

---An active business is a business that has more than one event_type such that their occurences is strictly greater than the average activity for that event.

---Write an SQL query to find all active businesses.

---Return the result table in any order.


# Write your MySQL query statement below
SELECT business_id FROM
(SELECT *, avg(occurences) over (PARTITION BY event_type) AS average FROM Events) a
WHERE occurences > average GROUP BY business_id HAVING count(*) > 1
