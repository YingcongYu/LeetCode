---The median is the value separating the higher half from the lower half of a data sample.

---Write an SQL query to report the median of all the numbers in the database after decompressing the Numbers table. Round the median to one decimal point.


# Write your MySQL query statement below
SELECT round(avg(num), 1) AS median FROM
(SELECT *, 
        sum(frequency) over (ORDER BY num) AS total_num, 
        sum(frequency) over ()/2 AS median_frequency 
 FROM Numbers) a
WHERE median_frequency BETWEEN total_num - frequency AND total_num
