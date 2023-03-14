---Write an SQL query to report the total sales amount of each item for each year, with corresponding product_name, product_id, product_name, and report_year.

---Return the result table ordered by product_id and report_year.


# Write your MySQL query statement below
WITH RECURSIVE CTE1 AS (
    SELECT
        DATE('2018-01-01') AS year_start
        ,DATE('2018-12-31') AS year_end
    UNION
    SELECT
        DATE_ADD(year_start, INTERVAL 1 YEAR)
        ,DATE_ADD(year_end, INTERVAL 1 YEAR)
    FROM CTE1
    WHERE year_end < DATE('2020-12-31')
),
CTE2 AS (
    SELECT
        product_id
        ,CASE WHEN period_start > year_start THEN period_start ELSE year_start END AS report_year_start
        ,CASE WHEN period_end < year_end THEN period_end ELSE year_end END AS report_year_end
        ,average_daily_sales
    FROM Sales
    JOIN CTE1
    ON Sales.period_start <= CTE1.year_end
        AND Sales.period_end >= CTE1.year_start
)

SELECT
    CTE2.product_id AS product_id
    ,product_name
    ,CAST(year(report_year_start) AS CHAR) AS report_year
    ,(DATEDIFF(report_year_end, report_year_start)+1) * average_daily_sales AS total_amount
FROM CTE2, Product
WHERE CTE2.product_id = Product.product_id
GROUP BY product_id, year(report_year_start)
ORDER BY product_id, report_year
