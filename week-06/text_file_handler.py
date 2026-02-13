# Text File Handling Example

def write_data():
    with open("students.txt", "w") as file:
        file.write("Name,Marks\n")
        file.write("Amit,85\n")
        file.write("Neha,92\n")
    print("Data written successfully.")

def read_data():
    with open("students.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)

if __name__ == "__main__":
    write_data()
    read_data()
