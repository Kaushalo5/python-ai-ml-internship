import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Delete Neha record
cursor.execute("DELETE FROM students WHERE name = 'Neha'")

conn.commit()
conn.close()

print("Record deleted successfully")
