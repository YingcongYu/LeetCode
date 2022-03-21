---The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)2 + (y2 - y1)2).

---Write an SQL query to report the shortest distance between any two points from the Point2D table. Round the distance to two decimal points.

# Write your MySQL query statement below
SELECT round(min(sqrt((t2.x - t1.x)*(t2.x - t1.x) + (t2.y - t1.y)*(t2.y - t1.y))),2) AS shortest
FROM Point2D AS t1, Point2D AS t2
WHERE (t1.x, t1.y) != (t2.x, t2.y)
