# Student Expense Tracker & Budget Analyzer

## Student Details

- **Name:** ROHITH RAJ R S
- **Registration Number:** 24MEI10069
- **Course:** Python Essentials

## 1. Project Overview

Student Expense Tracker & Budget Analyzer is a command-line Python application that helps students record income and expenses, create monthly budgets, analyze spending by category, and generate monthly financial reports.

The project is designed for the Python Essentials course and demonstrates modular Python programming, functions, classes, collections, JSON file handling, validation, exception handling, testing, and clean project organization.

## 2. Problem Statement

Students often make small daily purchases but do not maintain a structured record of where their money is going. This makes it difficult to understand spending patterns, control monthly expenses, and identify categories where spending is high.

This project provides a simple terminal-based system to record transactions and analyze them without requiring a graphical interface or external database.

## 3. Main Features

- Add income
- Add expense
- View all transactions
- Delete a transaction
- Set or update monthly budget
- Check budget usage
- Category-wise expense analysis
- Monthly financial summary
- Export a text report
- JSON-based persistent storage
- Input validation and error handling
- Unit tests

## 4. Functional Modules

1. Transaction Management
2. Budget Management
3. Expense Analytics
4. Reporting
5. Data Storage
6. Validation

## 5. Technology Used

- Python 3.10+
- Standard Library only
- JSON
- `datetime`
- `unittest`
- Git/GitHub

No external Python package is required.

## 6. Project Structure

```text
student-expense-tracker/
├── README.md
├── statement.md
├── report.md
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── validation.py
│   ├── transactions.py
│   ├── budget.py
│   ├── analytics.py
│   └── reports.py
├── data/
│   └── expenses.json
├── tests/
│   └── test_project.py
└── docs/
    └── diagrams/
        ├── architecture.mmd
        ├── workflow.mmd
        ├── use_case.mmd
        ├── class_diagram.mmd
        ├── sequence.mmd
        └── er_diagram.mmd
```

## 7. Requirements

Install Python 3.10 or newer.

Check the installation:

```bash
python --version
```

On some systems:

```bash
python3 --version
```

## 8. Installation

Clone the public GitHub repository:

```bash
git clone <YOUR_PUBLIC_GITHUB_REPOSITORY_URL>
cd student-expense-tracker
```

No package installation is required because the application uses the Python Standard Library.

If you want to create an isolated environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

## 9. Run the Application

From the repository root:

```bash
python main.py
```

## 10. Example Workflow

```text
1. Add Income
2. Add Expense
3. View Transactions
4. Delete Transaction
5. Set Monthly Budget
6. View Budget Status
7. Category Analysis
8. Monthly Report
9. Export Report
0. Exit
```

For an expense, enter a description, amount, category, and date.

Example:

```text
Description: College canteen
Amount: 80
Category: Food
Date: 2026-09-30
```

## 11. Testing

Run:

```bash
python -m unittest discover -s tests -v
```

The tests cover validation, transaction calculations, budget calculations, analytics, and storage behavior.

## 12. Data Storage

Application data is stored locally in:

```text
data/expenses.json
```

The JSON structure contains transactions and monthly budgets.

## 13. Design

The application follows a simple layered structure:

```text
User
  |
  v
main.py
  |
  +--> Validation
  |
  +--> Transaction Service
  |
  +--> Budget Service
  |
  +--> Analytics Service
  |
  +--> Report Service
  |
  v
JSON Storage
```

Detailed diagrams are available in `docs/diagrams/`.

## 14. Important Submission Checklist

Before submission:

- Make the GitHub repository Public.
- Ensure `README.md` is at repository root.
- Ensure `statement.md` is at repository root.
- Ensure the application runs using `python main.py`.
- Run all tests.
- Replace `<YOUR_PUBLIC_GITHUB_REPOSITORY_URL>` in this README.
- Add your own screenshots to the report.
- Update the student name, registration number, faculty/course details, and repository URL in the report.
- Review and understand every source file before submission.

## 15. Git Commands

```bash
git init
git add .
git commit -m "Initial project implementation"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## 16. Academic Originality

This repository is a project template and implementation starting point. Before submitting, the student should review the code, make appropriate personal changes, test it independently, and ensure that the submitted work complies with the institution's originality requirements.
