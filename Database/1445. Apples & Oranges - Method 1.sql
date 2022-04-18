---Write an SQL query to report the difference between the number of apples and oranges sold each day.

---Return the result table ordered by sale_date.

# Write your MySQL query statement below
SELECT 
    sale_date, 
    sum(CASE WHEN fruit = 'apples' THEN sold_num END) - sum(CASE WHEN fruit = 'oranges' THEN sold_num END) AS diff 
FROM Sales 
GROUP BY sale_date
