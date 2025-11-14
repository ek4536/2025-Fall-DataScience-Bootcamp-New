SELECT p.product_name, sum(o.unit) AS unit
FROM Products p
RIGHT JOIN Orders o
USING(product_id)
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_name
HAVING unit >=100 ;
