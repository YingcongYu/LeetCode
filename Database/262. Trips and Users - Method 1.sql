---The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

---Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT a.request_at AS Day, round(a.cancel/b.total, 2) AS `Cancellation Rate` FROM
    (SELECT request_at, SUM(CASE WHEN Trips.status = 'cancelled_by_driver' OR Trips.status = 'cancelled_by_client' THEN 1 ELSE 0 END) AS cancel FROM Trips
    JOIN
    (SELECT users_id FROM Users WHERE role = 'client' AND banned = 'No') client
    JOIN
    (SELECT users_id FROM Users WHERE role = 'driver' AND banned = 'No') driver
    ON client.users_id = Trips.client_id AND driver.users_id = Trips.driver_id 
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY request_at) a
JOIN
    (SELECT request_at, count(*) AS total FROM Trips 
    JOIN
    (SELECT users_id FROM Users WHERE role = 'client' AND banned = 'No') client
    JOIN
    (SELECT users_id FROM Users WHERE role = 'driver' AND banned = 'No') driver
    ON client.users_id = Trips.client_id AND driver.users_id = Trips.driver_id
    GROUP BY request_at) b
ON a.request_at = b.request_at
