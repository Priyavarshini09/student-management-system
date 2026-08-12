import csv

students = []

# Load students from CSV
try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) >= 5:
                students.append([row[0], row[1], row[2], row[3], row[4]])

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


    # Add Student
    if choice == "1":

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter age: ")

        while True:
            try:
                marks = float(input("Enter marks (0-100): "))

                if 0 <= marks <= 100:
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")


        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"


        student = [student_id, name, age, marks, grade]
        students.append(student)


        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            for student in students:
                writer.writerow(student)


        print("Student added successfully!")
        print("Grade:", grade)


    # View Students
    elif choice == "2":

        if len(students) == 0:

            print("No students found.")

        else:

            print("\nStudent List")

            for student in students:

                print(
                    "ID:", student[0],
                    "| Name:", student[1],
                    "| Age:", student[2],
                    "| Marks:", student[3],
                    "| Grade:", student[4]
                )


    # Search Student
    elif choice == "3":

        search = input("Enter student name to search: ")

        found = False

        for student in students:

            if student[1].lower() == search.lower():

                print("\nStudent found!")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Age:", student[2])
                print("Marks:", student[3])
                print("Grade:", student[4])

                found = True


        if not found:

            print("Student not found.")


    # Delete Student
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


    # Update Student
    elif choice == "5":

        update_id = input("Enter student ID to update: ")

        found = False

        for student in students:

            if student[0] == update_id:

                new_name = input("Enter new student name: ")
                new_age = input("Enter new age: ")


                while True:

                    try:

                        new_marks = float(
                            input("Enter new marks (0-100): ")
                        )

                        if 0 <= new_marks <= 100:
                            break

                        print("Marks must be between 0 and 100.")

                    except ValueError:

                        print("Please enter a valid number.")


                if new_marks >= 90:
                    new_grade = "A"

                elif new_marks >= 75:
                    new_grade = "B"

                elif new_marks >= 60:
                    new_grade = "C"

                else:
                    new_grade = "D"


                student[1] = new_name
                student[2] = new_age
                student[3] = new_marks
                student[4] = new_grade

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


    # Exit
    elif choice == "6":

        print("Thank you!")
        break


    else:

        print("Invalid choice. Please try again.")
