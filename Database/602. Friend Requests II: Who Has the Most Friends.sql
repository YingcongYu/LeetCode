---Write an SQL query to find the people who have the most friends and the most friends number.

---The test cases are generated so that only one person has the most friends.

# Write your MySQL query statement below
SELECT id, count(*) AS num FROM
(SELECT requester_id AS id FROM RequestAccepted AS r1
UNION ALL 
SELECT accepter_id AS id FROM RequestAccepted AS r2) a
GROUP BY id ORDER BY num DESC LIMIT 1
