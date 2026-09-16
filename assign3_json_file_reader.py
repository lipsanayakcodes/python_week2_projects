import json

# Open the JSON file
with open("students.json", "r") as file:
    data = json.load(file)

# Print formatted student data
print("----- Student Information -----")

for student in data["students"]:
    print("Roll Number :", student["roll_number"])
    print("Name        :", student["name"])
    print("Course      :", student["course"])
    print("Marks       :", student["marks"])
    print("-------------------------------")