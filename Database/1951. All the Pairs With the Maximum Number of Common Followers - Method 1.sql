--- Write an SQL query to find all the pairs of users with the maximum number of common followers. 
--- In other words, if the maximum number of common followers between any two users is maxCommon, 
--- then you have to return all pairs of users that have maxCommon common followers.

--- The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        r1.user_id AS  user1_id
        ,r2.user_id AS user2_id
        ,COUNT(*) AS counts
    FROM Relations r1, Relations r2
    WHERE r1.user_id < r2.user_id
        AND r1.follower_id = r2.follower_id
    GROUP BY user1_id, user2_id
)

SELECT
    user1_id
    ,user2_id
FROM CTE
WHERE counts = (SELECT MAX(counts) FROM CTE)
