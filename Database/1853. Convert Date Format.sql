---Write an SQL query to convert each date in Days into a string formatted as "day_name, month_name day, year".

---Return the result table in any order.

# Write your MySQL query statement below
SELECT date_format(day, '%W, %M %e, %Y') AS day FROM Days
