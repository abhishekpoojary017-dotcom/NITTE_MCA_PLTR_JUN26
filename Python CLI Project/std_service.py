from db import get_connection


def add_student():
    name = input("Student Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    course = input("Course: ")


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    INSERT INTO Students
    (
        StudentName,
        Email,
        Phone,
        Course
    )
    VALUES
    (%s,%s,%s,%s)
    """


    cursor.execute(
        query,
        (name, email, phone, course)
    )


    conn.commit()


    print("Student Added Successfully")


    cursor.close()
    conn.close()




def view_students():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            StudentID,
            StudentName,
            Email,
            Phone,
            Course
        FROM Students
    """)


    students = cursor.fetchall()


    print("\nStudents")
    print("-" * 80)


    for student in students:
        print(student)


    cursor.close()
    conn.close()




def update_student():
    student_id = int(input("Student ID: "))
    course = input("New Course: ")


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    UPDATE Students
    SET Course = %s
    WHERE StudentID = %s
    """


    cursor.execute(
        query,
        (course, student_id)
    )


    conn.commit()


    print("Student Updated Successfully")


    cursor.close()
    conn.close()




def delete_student():
    student_id = int(input("Student ID: "))


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    DELETE FROM Students
    WHERE StudentID = %s
    """


    cursor.execute(query, (student_id,))


    conn.commit()


    print("Student Deleted Successfully")


    cursor.close()
    conn.close()
