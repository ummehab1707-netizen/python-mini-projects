import os
from datetime import datetime

FILE = "expenses.txt"

def load_expenses():
    expenses = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    expenses.append({"date": parts[0], "category": parts[1], "amount": float(parts[2])})
    return expenses

def save_expense(expense):
    with open(FILE, "a") as f:
        f.write(f"{expense['date']}|{expense['category']}|{expense['amount']}\n")

def add_expense(expenses):
    print("\nCategories: Food, Transport, Shopping, Entertainment, Bills, Other")
    category = input("Enter category: ").strip().capitalize()
    try:
        amount = float(input("Enter amount (₹): "))
    except ValueError:
        print("Invalid amount!")
        return
    date = datetime.now().strftime("%Y-%m-%d")
    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)
    save_expense(expense)
    print(f"✅ Expense of ₹{amount} added under {category}!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n{:<15} {:<15} {:<10}".format("Date", "Category", "Amount"))
    print("-" * 42)
    total = 0
    for e in expenses:
        print("{:<15} {:<15} ₹{:<10}".format(e['date'], e['category'], e['amount']))
        total += e['amount']
    print("-" * 42)
    print(f"{'TOTAL':<30} ₹{total}")

def view_by_category(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    print("\n📊 Expense Summary by Category:")
    print("-" * 30)
    for cat, amt in sorted(summary.items()):
        print(f"  {cat:<20} ₹{amt:.2f}")
    print("-" * 30)
    print(f"  {'TOTAL':<20} ₹{sum(summary.values()):.2f}")

def delete_all(expenses):
    confirm = input("Are you sure you want to delete all expenses? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE, "w").close()
        expenses.clear()
        print("✅ All expenses deleted.")

def main():
    print("=== Expense Tracker ===")
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Delete All Expenses")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            delete_all(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
