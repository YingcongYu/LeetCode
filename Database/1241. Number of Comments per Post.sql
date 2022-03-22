---Write an SQL query to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.

---The Submissions table may contain duplicate comments. You should count the number of unique comments per post.

---The Submissions table may contain duplicate posts. You should treat them as one post.

---The result table should be ordered by post_id in ascending order.

# Write your MySQL query statement below
SELECT sub_id AS post_id, IFNULL(num, 0) AS number_of_comments FROM 
(SELECT DISTINCT sub_id FROM Submissions WHERE parent_id IS NULL) a
LEFT JOIN
(SELECT parent_id, count(DISTINCT(sub_id)) AS num FROM Submissions GROUP BY parent_id) b
ON a.sub_id = b.parent_id
ORDER BY post_id
