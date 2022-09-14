---Write an SQL query to report the total sales amount of each item for each year, with corresponding product_name, product_id, product_name, and report_year.

---Return the result table ordered by product_id and report_year.


# Write your MySQL query statement below
WITH RECURSIVE years AS(
    SELECT date('2018-01-01') AS year_start, date('2018-12-31') AS year_end
    UNION ALL
    SELECT date_add(year_start, INTERVAL 1 YEAR) AS year_start, date_add(year_end, INTERVAL 1 YEAR) AS year_end FROM years 
    WHERE year(year_end) < (SELECT year(max(period_end)) FROM Sales)
)

SELECT product_id, 
       product_name, 
       cast(year(report_start) AS char) AS report_year, 
       (datediff(report_end, report_start) + 1) * average_daily_sales AS total_amount
FROM
    (SELECT product_id, 
           product_name,
           CASE WHEN period_start <= year_start THEN year_start ELSE period_start END AS report_start,
           CASE WHEN period_end <= year_end THEN period_end ELSE year_end END AS report_end,
           average_daily_sales
    FROM years JOIN (SELECT Sales.product_id AS product_id, product_name, period_start, period_end, average_daily_sales 
                     FROM Sales JOIN Product ON Sales.product_id = Product.product_id) info
    ON info.period_start <= years.year_end AND info.period_end >= years.year_start) a
ORDER BY product_id, report_year
