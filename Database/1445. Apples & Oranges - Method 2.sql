---Write an SQL query to report the difference between the number of apples and oranges sold each day.

---Return the result table ordered by sale_date.

# Write your MySQL query statement below
SELECT 
    sale_date, 
    sum(IF(fruit = 'apples', sold_num, -sold_num)) AS diff 
FROM Sales 
GROUP BY sale_date
