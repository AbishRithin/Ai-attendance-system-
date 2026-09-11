import sqlite3
import os

DB_PATH = os.path.join("database", "attendance.db")

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        UNIQUE(name,date)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("Database Ready")