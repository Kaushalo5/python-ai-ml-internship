import sqlite3

# create database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()
conn.close()

print("Database & table created")

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO students (name, marks) VALUES ('Amit',85)")
cursor.execute("INSERT INTO students (name, marks) VALUES ('Neha',92)")

conn.commit()
conn.close()

print("Data inserted")



conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
