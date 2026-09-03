-- INSERT INTO users (id, name, email)
-- VALUES (1, 'Alex', 'alex@example.com');


INSERT INTO users (id, name, email)
VALUES
    (3, 'Bob', 'bob@example.com'),
    (4, 'John', 'john@example.com');

UPDATE users
SET name = 'John'
WHERE id = 4;

INSERT INTO users (id, name, email)
VALUES    (5, 'Bot', 'bot@example.com');

DELETE from users where id=5;

SELECT id, name, email from users;


CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL NOT NULL,
    category TEXT NOT NULL
);

DROP TABLE products;

-- ALTER TABLE products ADD COLUMN name TEXT
ALTER TABLE products DROP COLUMN category;

INSERT INTO products (id, name, price, category)
VALUES
    (1, 'Milk', 100, 'molochka'),
    (2, 'Pasta', 300,'bakaleya'),
    (3, 'Bread', 120,'bakaleya');


SELECT name, price, category from products
ORDER BY category DESC, price ASC;


INSERT INTO products (id, name, price, category)
VALUES
    (4, 'Cheese', 500, 'molochka'),
    (5, 'Rice', 350,'bakaleya'),
    (6, 'Cream', 400,'molochka'),
    (7, 'Pork', 800,'meat'),
    (8, 'Chicken', 700,'meat');


SELECT * from products ORDER BY price DESC LIMIT 3
