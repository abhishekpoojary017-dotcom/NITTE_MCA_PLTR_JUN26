import sqlite3
import os

DB_PATH = os.environ.get("DB_NAME", "hostel_db.sqlite")


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT NOT NULL,
            capacity INTEGER NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Allocations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            room_id INTEGER NOT NULL,
            allocated_on DATE,
            FOREIGN KEY(student_id) REFERENCES Students(id),
            FOREIGN KEY(room_id) REFERENCES Rooms(id)
        )
        """
    )

    conn.commit()
    conn.close()
    print(f"SQLite DB '{DB_PATH}' and tables created (if not exist).")


if __name__ == "__main__":
    main()
