-- Write your query below
SELECT * FROM customers WHERE customer_id in (
    SELECT customer_id from orders where product_name = 'A'
    ) AND customer_id in (
    SELECT customer_id from orders where product_name = 'B'
    ) AND customer_id not in (
    SELECT customer_id from orders where product_name = 'C'
    )
order by customer_name