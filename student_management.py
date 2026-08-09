import csv
import os

FILE = "students.csv"


def create_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll No", "Name", "Course", "Marks"])


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, course, marks])

    print("Student Added Successfully!")


def view_students():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        print("\n----- Student Records -----")
        for row in reader:
            print(row)


def search_student():
    roll = input("Enter Roll Number: ")

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[0] == roll:
                print("Student Found:", row)
                return

    print("Student Not Found")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    rows = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[0] != roll:
                rows.append(row)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Student Deleted Successfully!")


create_file()

while True:
    print("""
========= Student Management System =========

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
