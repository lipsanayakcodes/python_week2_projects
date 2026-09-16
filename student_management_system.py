import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["roll_number", "name", "marks"])


# Add student
def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_number, name, marks])

    print("Student added successfully!")


# Search student
def search_student():
    roll_number = input("Enter roll number to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["roll_number"] == roll_number:
                print("\nStudent Found")
                print("Roll Number:", student["roll_number"])
                print("Name       :", student["name"])
                print("Marks      :", student["marks"])
                return

    print("Student not found.")


# Delete student
def delete_student():
    roll_number = input("Enter roll number to delete: ")

    students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["roll_number"] == roll_number:
                found = True
            else:
                students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["roll_number", "name", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Display all students
def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n----- Student Records -----")

        found = False

        for student in reader:
            found = True
            print("Roll Number:", student["roll_number"])
            print("Name       :", student["name"])
            print("Marks      :", student["marks"])
            print("---------------------------")

        if not found:
            print("No student records available.")


# Main program
create_file()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")