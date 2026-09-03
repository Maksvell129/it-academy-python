CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);


CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrolled_at DATE,
    PRIMARY KEY (student_id, course_id)
);


CREATE TABLE orders2 (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    total NUMERIC,
    FOREIGN KEY (user_id)
        REFERENCES users(id)
);


CREATE TABLE users2 (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE
);
