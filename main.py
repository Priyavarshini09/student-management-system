print("===================================")
print("   Student Management System")
print("===================================")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        print(name, "added successfully!")

    elif choice == "2":
        print("No students available.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
