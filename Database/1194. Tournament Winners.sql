---The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

---Write an SQL query to find the winner in each group.

---Return the result table in any order.

# Write your MySQL query statement below
WITH scores AS
(SELECT player_id, sum(score) AS score FROM
 (SELECT first_player AS player_id, first_score AS score FROM Matches
  UNION ALL
  SELECT second_player AS player_id, second_score AS score FROM Matches) a
 GROUP BY player_id)

SELECT group_id, min(player_id) AS player_id FROM
(SELECT group_id, scores.player_id, score, max(score) over (PARTITION BY group_id) AS maximum
 FROM Players JOIN scores 
 ON Players.player_id = scores.player_id) b
WHERE score = maximum
GROUP BY group_id
