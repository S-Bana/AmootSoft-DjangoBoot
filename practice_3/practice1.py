import csv
from datetime import datetime
import os


class Expense:
    """A class to manage expenses."""

    def __init__(self):
        """Initialize the Expense class with a filename and create the file if it doesn't exist."""
        self.filename = "expenses.csv"
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        """Create the expense file if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Amount", "Description"])

    @staticmethod
    def validate_date(date_string):
        """Validate and parse the date string."""
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            return None

    @staticmethod
    def validate_amount(amount_string):
        """Validate and parse the amount string."""
        try:
            return float(amount_string)
        except ValueError:
            return None

    def read_expenses(self):
        """Read expenses from the CSV file."""
        expenses = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    date = str(datetime.strptime(row[0], "%Y-%m-%d").date())
                    expenses.append([date, row[1], float(row[2]), row[3]])
        except IOError:
            print("An error occurred while reading the file.")
        return expenses

    def add_expense(self):
        """Add a new expense to the CSV file."""
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")

        if not self.validate_date(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        if not self.validate_amount(amount):
            print("Invalid amount. Please enter a number.")
            return
        if not category or not description:
            print("Category and description cannot be empty.")
            return

        expense = [str(date), str(category), str(amount), str(description)]

        try:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(expense)
            print("Expense added successfully.")
        except IOError:
            print("An error occurred while writing to the file.")

    def delete_expense(self):
        """Delete an expense based on user input."""
        criterion = input("Enter date, description, or amount to delete: ")
        expenses = self.read_expenses()
        original_count = len(expenses)

        filtered_expenses = [
            exp for exp in expenses
            if not (criterion in str(exp[0]) or criterion in str(exp[1]) or criterion in str(exp[2]))
        ]

        if len(filtered_expenses) < original_count:
            try:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Date", "Category", "Amount", "Description"])
                    for exp in filtered_expenses:
                        writer.writerow(exp)
                print(f"{original_count - len(filtered_expenses)} expense(s) deleted.")
            except IOError:
                print("An error occurred while writing to the file.")
        else:
            print("No matching expenses found.")

    def total_expense(self):
        """Calculate total expenses for a given category."""
        category = input("Enter category to calculate total: ")
        expenses = self.read_expenses()
        if expenses:
            total = sum(exp[2] for exp in expenses if exp[1].lower() == category.lower())
            print(f"Total expense for {category}: ${total:.2f}")
        else:
            print("No expenses found.")

    def list_expenses_by_date(self):
        """List expenses for a specific date."""
        date_str = input("Enter date to list expenses (YYYY-MM-DD): ")
        date = self.validate_date(date_str)
        if not date:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        expenses = self.read_expenses()
        if expenses:
            matching_expenses = [exp for exp in expenses if date_str in exp[0]]
            if matching_expenses:
                for exp in matching_expenses:
                    print(f"{exp[1]}: ${exp[2]:.2f} - {exp[3]}")
            else:
                print("No expenses found for this date.")
        else:
            print("No expenses found.")

    def generate_report(self):
        """Generate a monthly or yearly expense report."""
        report_type = input("Enter 'monthly' or 'yearly' for report type: (m/y) ").lower()
        expenses = self.read_expenses()

        if not expenses:
            print("No expenses found.")
            return

        if report_type not in ['monthly', 'yearly', 'm', 'y']:
            print("Invalid report type. Please enter 'monthly' or 'yearly'.")
            return

        year = input("Enter year (YYYY): ")
        if not year.isdigit() or len(year) != 4:
            print("Invalid year format. Please enter a 4-digit year.")
            return

        if report_type in ['monthly', 'm']:
            month = input("Enter month (1-12): ")
            if not month.isdigit() or int(month) < 1 or int(month) > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                return

        categories = set(exp[1] for exp in expenses)
        for category in categories:
            for exp in expenses:
                if int(exp[0][:4]) == int(year):
                    if report_type in ['yearly', 'y'] or (report_type in ['monthly', 'm'] and int(exp[0][5:7]) == int(month)):
                        if exp[1] == category:
                            print(f"{exp[1]}: ${exp[2]:.2f} - {exp[3]}")


def main():
    """Main function to run the expense manager."""
    manager = Expense()
    while True:
        print("\n1. Add Expense")
        print("2. Delete Expense")
        print("3. Calculate Total Expense by Category")
        print("4. List Expenses by Date")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            manager.add_expense()
        elif choice == '2':
            manager.delete_expense()
        elif choice == '3':
            manager.total_expense()
        elif choice == '4':
            manager.list_expenses_by_date()
        elif choice == '5':
            manager.generate_report()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
