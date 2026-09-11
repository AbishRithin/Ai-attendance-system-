import sqlite3
from datetime import datetime
from database_utils import mark_attendance
name = known_names[first_match]
mark_attendance(name)

DB = "database/attendance.db"

def mark_attendance(name):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    cursor.execute(
        "SELECT * FROM attendance WHERE name=? AND date=?",
        (name, today)
    )

    if cursor.fetchone() is None:

        cursor.execute(
            """
            INSERT INTO attendance(name,date,time)
            VALUES(?,?,?)
            """,
            (name, today, current_time)
        )

        conn.commit()

        print(f"Attendance Marked: {name}")

    conn.close()