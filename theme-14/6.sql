CREATE TABLE students (
    id PRIMARY KEY,
    name TEXT NOT NULL,
);

CREATE TABLE courses (
    id PRIMARY KEY,
    name TEXT NOT NULL
);

-- DROP table courses
-- DROP table students

INSERT INTO courses (name)
values ('Math'), ('Python');


CREATE TABLE student_courses (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,

    PRIMARY KEY (student_id, course_id),

    FOREIGN KEY (student_id)
        REFERENCES students(id),

    FOREIGN KEY (course_id)
        REFERENCES courses(id)
);


CREATE TABLE users (
    id PRIMARY KEY,
    name TEXT NOT NULL,
    email NOT NULL,
);

CREATE TABLE user_profiles (
    phone_number TEXT NOT NULL,
    country TEXT NOT NULL,
    address TEXT NOT NULL,
    region TEXT NOT NULL,
    currency TEXT NOT NULL,
    last_name TEXT NOT NULL,
    first_name  TEXT NOT NULL,
    dob  TEXT NOT NULL,
    user_id INTEGER PRIMARY KEY,
    FOREIGN KEY (user_id) REFERENCES users(id),
);
