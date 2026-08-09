import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    date = datetime.now().strftime("%d-%m-%Y")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense Added Successfully!")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n----- All Expenses -----")
        for row in reader:
            print(f"Date: {row[0]} | Category: {row[1]} | Description: {row[2]} | Amount: ₹{row[3]}")


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[3])

    print("Total Spending: ₹", total)


def search_expense():
    category = input("Enter Category: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        found = False
        for row in reader:
            if row[1].lower() == category.lower():
                print(row)
                found = True

        if not found:
            print("No Expense Found")


def delete_expense():
    category = input("Enter Category to delete: ")
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[1].lower() != category.lower():
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Expense Deleted!")


create_file()

while True:
    print("""
========= Expense Tracker =========
1. Add Expense
2. View Expenses
3. Total Expense
4. Search Expense
5. Delete Expense
6. Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
