import sqlite3

conn = sqlite3.connect(
    "mara_memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(
id INTEGER PRIMARY KEY,
question TEXT,
answer TEXT
)
""")

conn.commit()
# ==================================

# GET LONG TERM MEMORY

# ==================================

def get_memory():

    cursor.execute(

        """

        SELECT question, answer

        FROM memory

        ORDER BY id DESC

        LIMIT 10

        """

    )

    return cursor.fetchall()