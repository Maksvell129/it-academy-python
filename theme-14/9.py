import psycopg2


connection = psycopg2.connect(
    host="localhost",
    database="shop",
    user="postgres",
    password="password"
)

cursor = connection.cursor()

cursor.execute(
    "SELECT id, name FROM users"
)

users = cursor.fetchall()

cursor.execute(
    """
    INSERT INTO users (name, email)
    VALUES (%s, %s)
    """,
    ("Alex", "alex@example.com")
)

query = f"SELECT * FROM users WHERE email = '{email}'"

cursor.execute(
    "SELECT * FROM users WHERE name = %s",
    (name,)
)


connection.commit()
