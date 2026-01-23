students = [("Amit", 85), ("Neha", 92), ("Raj", 78)]

students.sort(key=lambda x: x[1])

print("Sorted by Marks:", students)

students = [("Zmit", 85), ("Neha", 92), ("Raj", 78)]
students.sort(key=lambda x: x[0])
print("Sorted by Name:", students)

