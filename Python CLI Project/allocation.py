from db import get_connection


def allocate_room():
    student_id = int(input("Student ID: "))
    room_id = int(input("Room ID: "))
    allocation_date = input(
        "Allocation Date (YYYY-MM-DD): "
    )


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    INSERT INTO Allocations
    (
        StudentID,
        RoomID,
        AllocationDate
    )
    VALUES
    (%s,%s,%s)
    """


    cursor.execute(
        query,
        (
            student_id,
            room_id,
            allocation_date
        )
    )


    conn.commit()


    print("Room Allocated Successfully")


    cursor.close()
    conn.close()




def view_allocations():
    conn = get_connection()
    cursor = conn.cursor()


    query = """
    SELECT
        s.StudentName,
        r.RoomNo,
        a.AllocationDate
    FROM Students s
    INNER JOIN Allocations a
        ON s.StudentID = a.StudentID
    INNER JOIN Rooms r
        ON a.RoomID = r.RoomID
    """


    cursor.execute(query)


    allocations = cursor.fetchall()


    print("\nAllocations")
    print("-" * 80)


    for allocation in allocations:
        print(allocation)


    cursor.close()
    conn.close()
