CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);


SELECT *
FROM users
WHERE email = 'alex@example.com';


CREATE INDEX idx_users_email
ON users(email);
DROP INDEX idx_users_email

CREATE UNIQUE INDEX idx_users_email
ON users(email);


CREATE INDEX idx_users_name_email
ON users(name, email);
