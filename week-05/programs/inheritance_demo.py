# Demonstrates inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am", self.name)

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def details(self):
        print("Employee ID:", self.emp_id)

emp = Employee("Rahul", 101)
emp.introduce()
emp.details()
