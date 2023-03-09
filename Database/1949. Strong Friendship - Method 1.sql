--- A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

--- Write an SQL query to find all the strong friendships.

--- Note that the result table should not contain duplicates with user1_id < user2_id.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT * FROM Friendship
    UNION
    SELECT user2_id, user1_id FROM Friendship
)

SELECT 
    c1.user1_id AS user1_id
    ,c2.user1_id AS user2_id
    ,COUNT(*) AS common_friend
FROM CTE c1, CTE c2, CTE c3
WHERE c1.user1_id < c2.user1_id
    AND c1.user2_id = c2.user2_id
    AND c1.user1_id = c3.user1_id
    AND c2.user1_id = c3.user2_id
GROUP BY user1_id, user2_id
HAVING COUNT(*) >= 3
