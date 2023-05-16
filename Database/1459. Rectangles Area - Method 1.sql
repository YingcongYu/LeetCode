--- Write an SQL query to report all possible axis-aligned rectangles with a non-zero area that can be formed by any two points from the Points table.

--- Each row in the result should contain three columns (p1, p2, area) where:
--- p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
--- area is the area of the rectangle and must be non-zero.

--- Return the result table ordered by area in descending order. If there is a tie, order them by p1 in ascending order. 
--- If there is still a tie, order them by p2 in ascending order.


# Write your MySQL query statement below
SELECT
    t1.id AS P1
    ,t2.id AS P2
    ,abs(t1.x_value - t2.x_value) * abs(t1.y_value - t2.y_value) AS AREA
FROM Points t1, Points t2
WHERE t1.id < t2.id
    AND t1.x_value != t2.x_value
    AND t1.y_value != t2.y_value
ORDER BY AREA DESC, P1, P2
