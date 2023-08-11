-- You are implementing a page recommendation system for a social media website. 
--   Your system will recommend a page to user_id if the page is liked by at least one friend of user_id and is not liked by user_id.

-- Write a solution to find all the possible page recommendations for every user. 
--   Each recommendation should appear as a row in the result table with these columns:

-- user_id: The ID of the user that your system is making the recommendation to.
-- page_id: The ID of the page that will be recommended to user_id.
-- friends_likes: The number of the friends of user_id that like page_id.
-- Return the result table in any order.


# Write your MySQL query statement below
WITH friends AS (
    SELECT * FROM Friendship
    UNION
    SELECT user2_id, user1_id FROM Friendship
),
recommendations AS (
    SELECT
        user1_id AS user_id
        ,page_id
        ,COUNT(*) AS friends_likes
    FROM friends
    JOIN Likes
    ON friends.user2_id = Likes.user_id
    GROUP BY user1_id, page_id
)

SELECT
    recommendations.user_id
    ,recommendations.page_id
    ,friends_likes
FROM recommendations
LEFT JOIN Likes
ON recommendations.user_id = Likes.user_id
    AND recommendations.page_id = Likes.page_id
WHERE Likes.user_id IS NULL
