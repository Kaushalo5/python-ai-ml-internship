import csv
import json

def convert_csv_to_json():
    data = []
    with open("employees.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open("employees.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("CSV converted to JSON successfully.")

if __name__ == "__main__":
    convert_csv_to_json()
