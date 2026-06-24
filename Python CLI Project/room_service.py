from db import get_connection




def add_room():
    room_no = input("Room Number: ")
    floor = int(input("Floor: "))
    capacity = int(input("Capacity: "))


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    INSERT INTO Rooms
    (
        RoomNo,
        Floor,
        Capacity
    )
    VALUES
    (%s,%s,%s)
    """


    cursor.execute(
        query,
        (room_no, floor, capacity)
    )


    conn.commit()


    print("Room Added Successfully")


    cursor.close()
    conn.close()




def view_rooms():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            RoomID,
            RoomNo,
            Floor,
            Capacity
        FROM Rooms
    """)


    rooms = cursor.fetchall()


    print("\nRooms")
    print("-" * 50)


    for room in rooms:
        print(room)


    cursor.close()
    conn.close()

