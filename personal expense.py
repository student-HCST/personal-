import json
import os

FILE = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save expenses in file
def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter expense amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

# View expenses
def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found!")
    else:
        print("\n--- All Expenses ---")
        for e in expenses:
            print("Date:", e["date"])
            print("Category:", e["category"])
            print("Amount: Rs.", e["amount"])
            print("Description:", e["description"])
            print("--------------------")

# Calculate total expense
def total_expense(expenses):
    total = 0

    for e in expenses:
        total += e["amount"]

    print("Total Expense: Rs.", total)

# Set and check budget
def check_budget(expenses):
    budget = float(input("Enter your monthly budget: "))
    total = sum(e["amount"] for e in expenses)

    print("Monthly Budget: Rs.", budget)
    print("Total Expense: Rs.", total)

    remaining = budget - total

    if remaining >= 0:
        print("Remaining Budget: Rs.", remaining)
    else:
        print("Budget Exceeded by Rs.", abs(remaining))

# Main program
expenses = load_expenses()

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Check Budget")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expense(expenses)

    elif choice == "4":
        check_budget(expenses)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")