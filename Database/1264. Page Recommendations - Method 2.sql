---Write an SQL query to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.

---Return result table in any order without duplicates.


# Write your MySQL query statement below
WITH friends AS (SELECT CASE WHEN user1_id = 1 THEN user2_id
                             WHEN user2_id = 1 THEN user1_id END
                 FROM Friendship)
                 
SELECT DISTINCT page_id AS recommended_page FROM Likes
WHERE user_id IN (SELECT * FROM Friends)
  AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)
