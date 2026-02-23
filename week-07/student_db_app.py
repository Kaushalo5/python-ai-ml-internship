import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

def menu():
    print("\n--- Student Database ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nStudent Records:")
    for row in records:
        print(row)

def update_marks():
    name = input("Enter student name: ")
    new_marks = int(input("Enter new marks: "))

    cursor.execute("UPDATE students SET marks=? WHERE name=?", (new_marks, name))
    conn.commit()
    print("Marks updated!")

def delete_student():
    name = input("Enter student name to delete: ")

    cursor.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()
    print("Student deleted!")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_marks()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice")

conn.close()
