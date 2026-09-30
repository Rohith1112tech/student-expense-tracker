from src.storage import JsonStorage
from src.transactions import TransactionService
from src.budget import BudgetService
from src.analytics import AnalyticsService
from src.reports import ReportService
from src.validation import ValidationError, read_amount, read_date, read_non_empty


DATA_FILE = "data/expenses.json"


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def add_transaction(service):
    print_header("ADD TRANSACTION")
    transaction_type = input("Type (income/expense): ").strip().lower()

    if transaction_type not in {"income", "expense"}:
        print("Invalid type. Use income or expense.")
        return

    try:
        description = read_non_empty(input("Description: "), "Description")
        amount = read_amount(input("Amount: "))
        category = read_non_empty(input("Category: "), "Category")
        date = read_date(input("Date (YYYY-MM-DD, blank=today): "), allow_blank=True)
        service.add_transaction(transaction_type, description, amount, category, date)
        print("Transaction added successfully.")
    except ValidationError as exc:
        print(f"Error: {exc}")


def list_transactions(service):
    print_header("TRANSACTIONS")
    transactions = service.list_transactions()
    if not transactions:
        print("No transactions found.")
        return

    print(f"{'ID':<8}{'DATE':<12}{'TYPE':<10}{'CATEGORY':<16}{'AMOUNT':>12}  DESCRIPTION")
    print("-" * 80)
    for item in transactions:
        print(
            f"{item['id']:<8}{item['date']:<12}{item['type']:<10}"
            f"{item['category']:<16}{item['amount']:>12.2f}  {item['description']}"
        )


def delete_transaction(service):
    transaction_id = input("Enter transaction ID to delete: ").strip()
    if service.delete_transaction(transaction_id):
        print("Transaction deleted.")
    else:
        print("Transaction ID not found.")


def set_budget(service):
    print_header("SET MONTHLY BUDGET")
    try:
        month = input("Month (YYYY-MM): ").strip()
        amount = read_amount(input("Budget amount: "))
        service.set_budget(month, amount)
        print("Budget saved successfully.")
    except ValidationError as exc:
        print(f"Error: {exc}")


def show_budget(service):
    print_header("BUDGET STATUS")
    month = input("Month (YYYY-MM, blank=current month): ").strip()
    if not month:
        from datetime import date
        month = date.today().strftime("%Y-%m")

    try:
        status = service.get_status(month)
        print(f"Month: {month}")
        print(f"Budget:        {status['budget']:.2f}")
        print(f"Expenses:      {status['expenses']:.2f}")
        print(f"Remaining:     {status['remaining']:.2f}")
        print(f"Usage:         {status['usage_percent']:.2f}%")
        print(f"Status:        {status['status']}")
    except ValidationError as exc:
        print(f"Error: {exc}")


def show_category_analysis(service):
    print_header("CATEGORY ANALYSIS")
    month = input("Month (YYYY-MM, blank=all): ").strip()
    result = service.category_totals(month or None)
    if not result:
        print("No expense data available.")
        return

    total = sum(result.values())
    print(f"{'CATEGORY':<20}{'AMOUNT':>12}{'PERCENT':>12}")
    print("-" * 44)
    for category, amount in sorted(result.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / total * 100) if total else 0
        print(f"{category:<20}{amount:>12.2f}{percentage:>11.2f}%")


def show_monthly_report(service):
    print_header("MONTHLY REPORT")
    month = input("Month (YYYY-MM, blank=current month): ").strip()
    if not month:
        from datetime import date
        month = date.today().strftime("%Y-%m")
    try:
        print(service.generate_monthly_report(month))
    except ValidationError as exc:
        print(f"Error: {exc}")


def export_report(service):
    month = input("Month (YYYY-MM, blank=current month): ").strip()
    if not month:
        from datetime import date
        month = date.today().strftime("%Y-%m")
    try:
        path = service.export_monthly_report(month)
        print(f"Report exported to: {path}")
    except ValidationError as exc:
        print(f"Error: {exc}")


def main():
    storage = JsonStorage(DATA_FILE)
    transaction_service = TransactionService(storage)
    budget_service = BudgetService(storage)
    analytics_service = AnalyticsService(storage)
    report_service = ReportService(storage)

    while True:
        print_header("STUDENT EXPENSE TRACKER & BUDGET ANALYZER")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. Set Monthly Budget")
        print("6. View Budget Status")
        print("7. Category Analysis")
        print("8. Monthly Report")
        print("9. Export Report")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_transaction(transaction_service)
        elif choice == "2":
            # Reuse the same transaction function but force expense.
            print_header("ADD EXPENSE")
            try:
                description = read_non_empty(input("Description: "), "Description")
                amount = read_amount(input("Amount: "))
                category = read_non_empty(input("Category: "), "Category")
                date = read_date(input("Date (YYYY-MM-DD, blank=today): "), allow_blank=True)
                transaction_service.add_transaction(
                    "expense", description, amount, category, date
                )
                print("Expense added successfully.")
            except ValidationError as exc:
                print(f"Error: {exc}")
        elif choice == "3":
            list_transactions(transaction_service)
        elif choice == "4":
            delete_transaction(transaction_service)
        elif choice == "5":
            set_budget(budget_service)
        elif choice == "6":
            show_budget(budget_service)
        elif choice == "7":
            show_category_analysis(analytics_service)
        elif choice == "8":
            show_monthly_report(report_service)
        elif choice == "9":
            export_report(report_service)
        elif choice == "0":
            print("Thank you for using Student Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select a menu option.")


if __name__ == "__main__":
    main()
