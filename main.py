students = []

print("===================================")
print("   Student Management System")
print("===================================")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List")
            for i, student in enumerate(students, start=1):
                print(i, student)

    elif choice == "3":
        search = input("Enter student name to search: ")
        if search in students:
            print(search, "found!")
        else:
            print(search, "not found.")

    elif choice == "4":
        delete = input("Enter student name to delete: ")
        if delete in students:
            students.remove(delete)
            print(delete, "deleted successfully!")
        else:
            print(delete, "not found.")

    elif choice == "5":
        old_name = input("Enter old student name: ")

        if old_name in students:
            new_name = input("Enter new student name: ")
            index = students.index(old_name)
            students[index] = new_name
            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
