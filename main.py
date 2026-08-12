import csv

students = []

# Load students from CSV
try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                students.append([row[0], row[1]])
except FileNotFoundError:
    pass

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
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")

        student = [student_id, name]
        students.append(student)

        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for student in students:
                writer.writerow(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List")
            for student in students:
                print("ID:", student[0], "| Name:", student[1])

    elif choice == "3":
        search = input("Enter student name to search: ")
        found = False

        for student in students:
            if student[1].lower() == search.lower():
                print("Student found!")
                print("ID:", student[0])
                print("Name:", student[1])
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_id = input("Enter student ID to delete: ")
        found = False

        for student in students:
            if student[0] == delete_id:
                students.remove(student)
                found = True
                break

        if found:
            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for student in students:
                    writer.writerow(student)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        update_id = input("Enter student ID to update: ")
        found = False

        for student in students:
            if student[0] == update_id:
                new_name = input("Enter new student name: ")
                student[1] = new_name
                found = True
                break

        if found:
            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for student in students:
                    writer.writerow(student)
            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
