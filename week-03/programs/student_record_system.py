student = {}

while True:
    print("\n1. Add Student \n2. View Students \n3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")
        student[student_id] = {'name': name, 'age': age}
        print("Student added successfully.")

    elif choice == 2:
        if not student:
            print("No students found.")
        else:
            for name, info in student.items():
                print(f"ID: {name}, Name: {info['name']}, Age: {info['age']}")    

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")            