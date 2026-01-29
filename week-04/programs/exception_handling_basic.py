try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid integers")

finally:
    print("Program execution finished")