---Write an SQL query to find the total score for each gender on each day.

---Return the result table ordered by gender and day in ascending order.

# Write your MySQL query statement below
SELECT gender, 
       day, 
       sum(score_points) over (PARTITION BY gender ORDER BY day) AS total 
FROM Scores
