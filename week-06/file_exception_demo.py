try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("File operation handled safely.")
