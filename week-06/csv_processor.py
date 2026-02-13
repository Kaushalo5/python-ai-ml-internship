import csv

def create_csv():
    data = [
        ["Name", "Age", "Salary"],
        ["Amit", 25, 50000],
        ["Neha", 28, 60000],
        ["Raj", 22, 45000]
    ]

    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV file created.")

def filter_high_salary():
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        print("Employees with salary > 50000:")
        for row in reader:
            if int(row["Salary"]) > 50000:
                print(row)

if __name__ == "__main__":
    create_csv()
    filter_high_salary()
