from pathlib import Path
from datetime import date
from .validation import validate_month
from .transactions import TransactionService
from .analytics import AnalyticsService


class ReportService:
    def __init__(self, storage):
        self.storage = storage
        self.transactions = TransactionService(storage)
        self.analytics = AnalyticsService(storage)

    def generate_monthly_report(self, month):
        validate_month(month)
        totals = self.transactions.totals(month)
        categories = self.analytics.category_totals(month)

        lines = [
            "=" * 60,
            f"MONTHLY FINANCIAL REPORT - {month}",
            "=" * 60,
            f"Total Income   : {totals['income']:.2f}",
            f"Total Expenses : {totals['expenses']:.2f}",
            f"Balance        : {totals['balance']:.2f}",
            "",
            "CATEGORY-WISE EXPENSES",
            "-" * 60,
        ]

        if categories:
            for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
                lines.append(f"{category:<30}{amount:>12.2f}")
        else:
            lines.append("No expenses recorded for this month.")

        lines.extend([
            "-" * 60,
            "End of report",
        ])
        return "\n".join(lines)

    def export_monthly_report(self, month):
        report = self.generate_monthly_report(month)
        output_dir = Path("data/reports")
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = output_dir / f"monthly_report_{month}.txt"
        filename.write_text(report + "\n", encoding="utf-8")
        return str(filename)
