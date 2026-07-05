import csv
from datetime import datetime
import os

FILENAME = "expenses.csv"

def add_expense(desc, amount, category):
    """Appends a new expense row to the CSV file with the current date."""
    try:
        amount_val = float(amount)
    except ValueError:
        print("Error: Amount must be a valid number.")
        return

    # Check if file exists to write headers if necessary
    file_exists = os.path.isfile(FILENAME)
    
    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Description", "Amount", "Category", "Date"])
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        writer.writerow([desc, amount_val, category, date_str])
    print("Success: Expense added.")

def view_expenses():
    """Displays all recorded expenses."""
    if not os.path.isfile(FILENAME):
        print("No expenses recorded yet.")
        return

    print("\n--- All Recorded Expenses ---")
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip the header row
        for row in reader:
            if row:
                print(f"Date: {row[3]} | Category: {row[2]} | Description: {row[0]} | Amount: {float(row[1]):.2f}")

def search_category(category):
    """Filters and displays all expenses matching a given category."""
    if not os.path.isfile(FILENAME):
        print("No expenses recorded yet.")
        return

    print(f"\n--- Searching Category: {category} ---")
    found = False
    total_in_category = 0.0
    
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header
        for row in reader:
            if row and row[2].strip().lower() == category.strip().lower():
                print(f"Date: {row[3]} | Description: {row[0]} | Amount: {float(row[1]):.2f}")
                total_in_category += float(row[1])
                found = True
                
    if found:
        print(f"Total spent in '{category}': {total_in_category:.2f}")
    else:
        print(f"No expenses found in the '{category}' category.")

def monthly_total(month):
    """Calculates and prints total spending for a specific month (Format: YYYY-MM)."""
    if not os.path.isfile(FILENAME):
        print("No expenses recorded yet.")
        return

    total = 0.0
    found = False
    
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header
        for row in reader:
            if row and row[3].startswith(month):
                total += float(row[1])
                found = True
                
    if found:
        print(f"Monthly Total for {month}: {total:.2f}")
    else:
        print(f"No records found for the month: {month}")

def main():
    """Main application loop acting as the CLI Interface."""
    while True:
        print("\n=== Expense Tracker 2.0 ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Category")
        print("4. View Monthly Spending Total")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            desc = input("Enter expense description: ").strip()
            amount = input("Enter amount: ").strip()
            category = input("Enter category (e.g., Food, Travel, Shopping): ").strip()
            if desc and amount and category:
                add_expense(desc, amount, category)
            else:
                print("Error: All fields are required.")
                
        elif choice == "2":
            view_expenses()
            
        elif choice == "3":
            category = input("Enter category to search: ").strip()
            search_category(category)
            
        elif choice == "4":
            month = input("Enter month to calculate (Format: YYYY-MM, e.g., 2026-07): ").strip()
            monthly_total(month)
            
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()