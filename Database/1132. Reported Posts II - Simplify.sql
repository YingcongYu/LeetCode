---Write an SQL query to find the average daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.

# Write your MySQL query statement below
SELECT round(avg(daily_percent)*100, 2) AS average_daily_percent FROM
(SELECT action_date, 
 count(DISTINCT(Removals.post_id))/count(DISTINCT(Actions.post_id)) AS daily_percent
 FROM Actions LEFT JOIN Removals
 ON Removals.post_id = Actions.post_id
 WHERE extra = 'spam'
 GROUP BY action_date) a
