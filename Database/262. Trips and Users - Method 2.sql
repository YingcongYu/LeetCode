---The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

---Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT request_at AS Day, round(count(IF(status != 'completed', TRUE, NULL))/count(*),2) AS 'Cancellation Rate' 
FROM Trips
WHERE client_id in (SELECT users_id FROM Users WHERE banned = 'No')
    AND driver_id in (SELECT users_id FROM Users WHERE banned = 'No')
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at
