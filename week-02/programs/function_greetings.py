def greet(name):
    return f"Hello {name}, welcome to my program!"

user_name = input("Enter your name: ")
message = greet(user_name)
print(message)