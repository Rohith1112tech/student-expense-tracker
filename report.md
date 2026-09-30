# Student Expense Tracker & Budget Analyzer
## Project Report

> Replace the bracketed fields before submission.

**Student Name:** ROHITH RAJ R S  
**Registration Number:** 24MEI10069  
**Course:** Python Essentials  
**Institution:** VIT Bhopal University  
**Submission Date:** 30 September 2026  
**GitHub Repository:** [PUBLIC REPOSITORY URL]

---

# 1. Cover Page

**Project Title:** Student Expense Tracker & Budget Analyzer

This project is submitted as part of the flipped course evaluation for Python Essentials.

---

# 2. Introduction

Managing personal expenses is an important practical skill for college students. Daily spending may be distributed across food, transport, educational materials, subscriptions and other categories. Without a structured record, it is difficult to calculate total spending, compare spending with a budget, or identify high-expense categories.

The Student Expense Tracker & Budget Analyzer is a command-line Python application designed to solve this problem. It allows a student to record income and expenses, maintain monthly budgets, analyze category-wise expenses, and generate monthly reports.

The application intentionally uses the Python Standard Library so that an evaluator can execute the project from a terminal without installing a GUI framework or database server.

---

# 3. Problem Statement

Students often record financial transactions informally or do not record them at all. As the number of transactions increases, manually calculating monthly expenses becomes difficult and error-prone.

The proposed application provides a structured way to:

- record income and expenses;
- classify expenses into categories;
- maintain monthly spending limits;
- calculate balances;
- identify category-wise spending;
- generate monthly reports.

---

# 4. Objectives

1. Build a modular Python command-line application.
2. Demonstrate practical use of Python functions, classes, modules and collections.
3. Implement persistent storage using JSON.
4. Provide validation and exception handling.
5. Analyze expense data by month and category.
6. Generate human-readable financial reports.
7. Provide automated unit tests.
8. Maintain a clean GitHub-ready project structure.

---

# 5. Scope

## Included

- Income entry
- Expense entry
- Transaction listing
- Transaction deletion
- Monthly budgets
- Budget utilization calculation
- Category analysis
- Monthly reports
- Text report export
- JSON persistence
- Input validation
- Unit testing

## Not Included

- Bank account integration
- Online payment processing
- Real money transfer
- Cloud synchronization
- Financial investment advice

---

# 6. Target Users

The target users are college students who want a simple local application for tracking personal income and expenses.

---

# 7. Functional Requirements

## FR1 - Add Income

The system shall allow the user to record an income transaction with description, amount, category and date.

## FR2 - Add Expense

The system shall allow the user to record an expense with description, amount, category and date.

## FR3 - View Transactions

The system shall display stored transactions with ID, date, type, category, amount and description.

## FR4 - Delete Transaction

The system shall allow a transaction to be deleted using its transaction ID.

## FR5 - Budget Management

The system shall allow the user to create or update a monthly budget.

## FR6 - Budget Status

The system shall calculate total monthly expenses, remaining budget and budget utilization percentage.

## FR7 - Category Analysis

The system shall group expenses by category and calculate category totals.

## FR8 - Monthly Reporting

The system shall calculate monthly income, expenses, balance and category-wise expenses.

## FR9 - Report Export

The system shall export a monthly report as a text file.

---

# 8. Non-Functional Requirements

## NFR1 - Usability

The application uses a menu-driven command-line interface so that a user can operate it with basic keyboard input.

## NFR2 - Reliability

Data is saved after modification. Temporary-file replacement is used during JSON writes to reduce the risk of leaving a partially written main data file.

## NFR3 - Maintainability

The application is divided into separate modules for storage, validation, transactions, budgets, analytics and reports.

## NFR4 - Performance

The application uses local JSON storage and simple in-memory calculations. For a typical student dataset, operations are lightweight.

## NFR5 - Portability

The application uses Python Standard Library modules and can run on systems that support Python 3.10 or newer.

## NFR6 - Error Handling

Invalid amounts, dates and empty fields are detected before data is stored. File and JSON errors are handled by the storage layer.

---

# 9. System Architecture

The system follows a modular layered architecture.

```text
+-----------------------+
|       Student         |
+-----------+-----------+
            |
            v
+-----------------------+
| Command Line Interface|
|       main.py         |
+-----------+-----------+
            |
   +--------+---------+----------------+
   |        |         |                |
   v        v         v                v
Validation Transaction Budget       Analytics
 Module      Service   Service        Service
   |           |         |               |
   +-----------+---------+---------------+
                       |
                       v
                +-------------+
                | JSON Storage |
                +-------------+
                       |
                       v
                expenses.json
```

The report service uses the transaction and analytics services to produce monthly reports.

---

# 10. Workflow

1. The application starts.
2. The main menu is displayed.
3. The user selects an operation.
4. Input is collected.
5. Input is validated.
6. Business logic is executed.
7. Data is loaded or updated.
8. Updated data is saved to JSON.
9. Results are displayed.
10. The user returns to the main menu or exits.

---

# 11. Use Case Design

The primary actor is the Student.

The student can:

- add income;
- add expense;
- view transactions;
- delete transactions;
- set budgets;
- view budget status;
- analyze categories;
- generate monthly reports;
- export reports.

See `docs/diagrams/use_case.mmd`.

---

# 12. Class / Component Design

### Transaction

Represents a single income or expense record.

### JsonStorage

Responsible for loading and saving JSON data.

### TransactionService

Provides transaction creation, listing, deletion and totals.

### BudgetService

Stores monthly budgets and calculates budget status.

### AnalyticsService

Calculates category-wise expense totals.

### ReportService

Generates and exports monthly reports.

### Validation Module

Validates amounts, dates, months and required text fields.

---

# 13. Storage Design

The project uses JSON instead of a database because the application is intended for a small, local student dataset and the course focuses on Python Essentials.

Example:

```json
{
    "transactions": [
        {
            "id": "a12b34cd",
            "type": "expense",
            "description": "Lunch",
            "amount": 100.0,
            "category": "Food",
            "date": "2026-09-30"
        }
    ],
    "budgets": {
        "2026-09": 5000.0
    }
}
```

---

# 14. Design Decisions and Rationale

## Why Command Line?

The assignment requires command-line executability. A CLI also demonstrates Python programming concepts without depending on a graphical environment.

## Why JSON?

JSON is human-readable, easy to inspect, and available through the Python Standard Library.

## Why Modular Services?

Separating transaction, budget, analytics and reporting logic makes the program easier to test and maintain.

## Why Standard Library Only?

This minimizes installation problems for the evaluator.

---

# 15. Implementation Details

## Input Validation

The validation module checks:

- non-empty text;
- positive numeric amounts;
- valid dates;
- valid month format.

## Transaction Processing

Transactions are represented using a Python dataclass. Each transaction receives a short unique ID.

## Budget Calculation

For a selected month:

```text
Remaining Budget = Budget - Total Expenses

Usage Percentage =
(Total Expenses / Budget) × 100
```

If no budget is configured, the application reports that no budget is set.

## Category Analysis

Expenses are grouped using a dictionary. The amount for each category is accumulated and then displayed in descending order.

## Reporting

The report module combines monthly totals and category analysis into a readable text report.

---

# 16. Algorithms

## Algorithm 1 - Add Transaction

1. Read transaction type.
2. Validate transaction type.
3. Read description.
4. Validate description.
5. Read amount.
6. Validate positive amount.
7. Read category.
8. Read date.
9. Generate transaction ID.
10. Create transaction object.
11. Load JSON data.
12. Append transaction.
13. Save updated data.
14. Display success message.

## Algorithm 2 - Budget Status

1. Read month.
2. Validate month format.
3. Load stored budget.
4. Read all transactions for the selected month.
5. Select expense transactions.
6. Calculate total expenses.
7. Calculate remaining budget.
8. Calculate usage percentage.
9. Determine whether spending is within or over budget.
10. Display results.

## Algorithm 3 - Category Analysis

1. Load transactions.
2. Select expense transactions.
3. Filter by month if supplied.
4. Create an empty category dictionary.
5. Add each expense amount to its category.
6. Calculate total expenses.
7. Calculate percentage for each category.
8. Sort categories by amount.
9. Display results.

---

# 17. Testing Approach

The project uses Python's `unittest` framework.

Tests cover:

| Test | Purpose |
|---|---|
| Add transaction | Confirms transactions are stored |
| Calculate totals | Checks income, expense and balance |
| Budget status | Checks remaining amount and status |
| Category analysis | Checks grouping by category |
| Invalid amount | Confirms validation |
| Invalid date | Confirms date validation |

Run:

```bash
python -m unittest discover -s tests -v
```

Expected result: all tests should pass.

---

# 18. Example Test Scenario

Input:

```text
Income: 5000
Expense: 1000 Education
Expense: 500 Food
Budget: 2000
```

Expected:

```text
Total Income   = 5000
Total Expenses = 1500
Balance        = 3500
Budget         = 2000
Remaining      = 500
Usage          = 75%
Status         = Within budget
```

---

# 19. Screenshots / Results

Add screenshots of your own execution here before submitting.

Recommended screenshots:

1. Main menu
2. Add expense
3. Transaction list
4. Budget status
5. Category analysis
6. Monthly report
7. Successful unit tests

Example caption:

**Figure 1: Main menu of the Student Expense Tracker**

---

# 20. Challenges Faced

1. Designing the application so that multiple features could share the same JSON data.
2. Handling invalid user input without terminating the program.
3. Keeping business logic separate from user-interface code.
4. Calculating monthly values correctly.
5. Writing tests that use temporary storage rather than changing the real project data.

---

# 21. Learnings and Key Takeaways

Through this project, the following Python concepts were applied:

- Functions
- Classes
- Dataclasses
- Modules and packages
- Dictionaries and lists
- File handling
- JSON serialization
- Exception handling
- Date processing
- Unit testing
- Command-line interaction
- Modular software design

The project also demonstrated how individual Python concepts can be combined to create a complete application.

---

# 22. Future Enhancements

Possible future improvements include:

1. SQLite database support.
2. CSV import and export.
3. Password-protected local profiles.
4. Recurring transaction support.
5. Savings-goal tracking.
6. More detailed statistical analysis.
7. Optional graphical dashboard.
8. Cloud synchronization.
9. Automated backup.
10. Configurable currency support.

---

# 23. Conclusion

The Student Expense Tracker & Budget Analyzer provides a practical solution for recording and understanding student expenses. It combines transaction management, budget control, analytics and reporting in a single terminal application.

The project demonstrates the use of core Python programming concepts in a modular and testable application. Its use of standard-library components makes it simple to install and execute from the command line.

---

# 24. References

1. Python Documentation — Python Standard Library.
2. VITyarthi Build Your Own Project — General Project Instructions & Submission Guidelines.
3. Python `json`, `datetime`, `dataclasses`, `pathlib`, `unittest`, and `collections` documentation.

