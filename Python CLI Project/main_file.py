from student_service import (
    add_student,
    view_students,
    update_student,
    delete_student
)


from room_service import (
    add_room,
    view_rooms
)


from allocation_service import (
    allocate_room,
    view_allocations
)




def menu():
    while True:


        print("\n")
        print("=" * 40)
        print("HOSTEL MANAGEMENT SYSTEM")
        print("=" * 40)


        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Room")
        print("6. View Rooms")
        print("7. Allocate Room")
        print("8. View Allocations")
        print("9. Exit")


        choice = input("Enter Choice: ")


        if choice == "1":
            add_student()


        elif choice == "2":
            view_students()


        elif choice == "3":
            update_student()


        elif choice == "4":
            delete_student()


        elif choice == "5":
            add_room()


        elif choice == "6":
            view_rooms()


        elif choice == "7":
            allocate_room()


        elif choice == "8":
            view_allocations()


        elif choice == "9":
            print("Goodbye")
            break


        else:
            print("Invalid Choice")




if __name__ == "__main__":
    menu()
