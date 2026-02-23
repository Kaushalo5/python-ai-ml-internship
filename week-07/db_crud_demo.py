import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

print("Current records:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# update
cursor.execute("UPDATE students SET marks=95 WHERE name='Amit'")

# delete
cursor.execute("DELETE FROM students WHERE marks < 80")

conn.commit()

print("After changes:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()
