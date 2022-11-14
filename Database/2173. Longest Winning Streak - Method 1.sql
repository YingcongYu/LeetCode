---The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.

---Write an SQL query to count the longest winning streak for each player.

---Return the result table in any order.


# Write your MySQL query statement below
WITH CTE AS
(SELECT
    player_id
    ,result
    ,ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day) AS ref1
    ,ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day) AS ref2
FROM Matches)

SELECT
    M1.player_id
    ,MAX(IFNULL(streak, 0)) AS longest_streak
FROM Matches M1
LEFT JOIN (SELECT 
                player_id
                ,COUNT(ref1 - ref2) AS streak
            FROM CTE 
            WHERE result = 'Win'
            GROUP BY player_id, ref1-ref2) M2
ON M1.player_id = M2.player_id
GROUP BY player_id
