DELETE from users where id=5;

SELECT id, name, email from users;


CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    total DECIMAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


INSERT INTO orders (id, user_id, total)
VALUES
    (4,  9, 300),
    (5,  2,3000),
    (6,  3,0);


SELECT
    users.name,
    orders.total
FROM orders JOIN users  ON users.id = orders.user_id;


SELECT
    users.name,
    orders.total
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id;


SELECT * from products ORDER BY price DESC LIMIT 3


SELECT COUNT(*) FROM orders;
SELECT sum(total) FROM orders;
SELECT avg(total) FROM orders;
SELECT min(total) FROM orders;
SELECT max(total) FROM orders;


SELECT
    user_id,
    COUNT(*) AS orders_count
FROM orders
GROUP BY user_id;

SELECT
    user_id,
    sum(total) AS orders_sum
FROM orders
GROUP BY user_id;

SELECT
    user_id,
    COUNT(*) AS orders_count
FROM orders
WHERE total > 0
GROUP BY user_id
HAVING COUNT(*) > 1;

