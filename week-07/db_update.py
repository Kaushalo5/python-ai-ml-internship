import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Update marks of Amit
cursor.execute("UPDATE students SET marks = 90 WHERE name = 'Amit'")

conn.commit()
conn.close()

print("Record updated successfully")
