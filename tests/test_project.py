import json
import tempfile
import unittest
from pathlib import Path

from src.storage import JsonStorage
from src.transactions import TransactionService
from src.budget import BudgetService
from src.analytics import AnalyticsService
from src.validation import ValidationError, read_amount, read_date


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "test.json"
        self.storage = JsonStorage(self.path)
        self.transactions = TransactionService(self.storage)
        self.budget = BudgetService(self.storage)
        self.analytics = AnalyticsService(self.storage)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_transaction(self):
        item = self.transactions.add_transaction(
            "expense", "Lunch", 100, "Food", "2026-09-30"
        )
        self.assertEqual(item.amount, 100)
        self.assertEqual(len(self.transactions.list_transactions()), 1)

    def test_totals(self):
        self.transactions.add_transaction("income", "Allowance", 5000, "Income", "2026-09-01")
        self.transactions.add_transaction("expense", "Books", 1000, "Education", "2026-09-02")
        totals = self.transactions.totals("2026-09")
        self.assertEqual(totals["income"], 5000)
        self.assertEqual(totals["expenses"], 1000)
        self.assertEqual(totals["balance"], 4000)

    def test_budget_status(self):
        self.transactions.add_transaction("expense", "Food", 500, "Food", "2026-09-10")
        self.budget.set_budget("2026-09", 1000)
        status = self.budget.get_status("2026-09")
        self.assertEqual(status["remaining"], 500)
        self.assertEqual(status["status"], "Within budget")

    def test_category_analysis(self):
        self.transactions.add_transaction("expense", "Bus", 100, "Transport", "2026-09-10")
        self.transactions.add_transaction("expense", "Lunch", 200, "Food", "2026-09-11")
        result = self.analytics.category_totals("2026-09")
        self.assertEqual(result["Food"], 200)
        self.assertEqual(result["Transport"], 100)

    def test_invalid_amount(self):
        with self.assertRaises(ValidationError):
            read_amount("-20")

    def test_invalid_date(self):
        with self.assertRaises(ValidationError):
            read_date("30-09-2026")


if __name__ == "__main__":
    unittest.main()
