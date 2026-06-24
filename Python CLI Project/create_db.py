import mysql.connector
import os

HOST = os.environ.get("DB_HOST", "localhost")
USER = os.environ.get("DB_USER", "root")
PASSWORD = os.environ.get("DB_PASSWORD", "password")
DB_NAME = os.environ.get("DB_NAME", "hostel_db")


def main():
    # Connect without specifying database to create it
    conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    # Create Students table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE,
            phone VARCHAR(50)
        )
        """
    )

    # Create Rooms table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Rooms (
            id INT AUTO_INCREMENT PRIMARY KEY,
            room_number VARCHAR(50) NOT NULL,
            capacity INT NOT NULL
        )
        """
    )

    # Create Allocations table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Allocations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            room_id INT NOT NULL,
            allocated_on DATE,
            FOREIGN KEY (student_id) REFERENCES Students(id),
            FOREIGN KEY (room_id) REFERENCES Rooms(id)
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Database '{DB_NAME}' and tables created (if they did not exist).")


if __name__ == "__main__":
    main()
