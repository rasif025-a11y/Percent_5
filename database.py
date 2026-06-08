import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    correct INTEGER,
    attempts INTEGER
)
""")

conn.commit()


def save_result(username, correct, attempts):

    cursor.execute(
        """
        INSERT INTO results
        (username, correct, attempts)
        VALUES (?, ?, ?)
        """,
        (username, correct, attempts)
    )

    conn.commit()


def get_results():

    cursor.execute("""
    SELECT username, correct, attempts
    FROM results
    """)

    return cursor.fetchall()