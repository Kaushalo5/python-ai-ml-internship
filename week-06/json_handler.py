import json

data = {
    "students": [
        {"name": "Amit", "marks": 85},
        {"name": "Neha", "marks": 92}
    ]
}

def write_json():
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("JSON written successfully.")

def read_json():
    with open("data.json", "r") as file:
        content = json.load(file)
        print("JSON Content:\n", content)

if __name__ == "__main__":
    write_json()
    read_json()
