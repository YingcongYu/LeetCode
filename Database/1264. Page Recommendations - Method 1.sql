---Write an SQL query to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.

---Return result table in any order without duplicates.


# Write your MySQL query statement below
WITH user1 AS (SELECT DISTINCT * FROM Friendship 
               WHERE user1_id = 1 OR user2_id = 1)

SELECT DISTINCT page_id AS recommended_page FROM Likes 
WHERE page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1) 
    AND (user_id IN (SELECT user1_id FROM user1 WHERE user1_id != 1) 
         OR user_id IN (SELECT user2_id FROM user1 WHERE user2_id != 1))
