# Demonstrates class and object

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")    

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)   

s1.display()
s2.display()