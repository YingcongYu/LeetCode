---The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

---Write an SQL query to find the winner in each group.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT group_id, player_id FROM
(SELECT group_id, 
       player_id, 
       rank() over (PARTITION BY group_id 
                    ORDER BY sum(CASE WHEN player_id = first_player 
                                 THEN first_score ELSE second_score END) DESC, 
                                 player_id) AS ranking
FROM Players JOIN Matches
ON Players.player_id IN (Matches.first_player, Matches.second_player)
GROUP BY group_id, player_id) a
WHERE ranking = 1
