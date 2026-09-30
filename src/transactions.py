from datetime import date
from uuid import uuid4
from .models import Transaction


class TransactionService:
    def __init__(self, storage):
        self.storage = storage

    def add_transaction(self, transaction_type, description, amount, category, date_value=None):
        if transaction_type not in {"income", "expense"}:
            raise ValueError("Transaction type must be income or expense.")

        transaction = Transaction(
            id=uuid4().hex[:8],
            type=transaction_type,
            description=description,
            amount=float(amount),
            category=category,
            date=date_value or date.today().isoformat(),
        )

        data = self.storage.load()
        data["transactions"].append(transaction.to_dict())
        self.storage.save(data)
        return transaction

    def list_transactions(self):
        data = self.storage.load()
        return sorted(data["transactions"], key=lambda item: (item["date"], item["id"]), reverse=True)

    def delete_transaction(self, transaction_id):
        data = self.storage.load()
        original_count = len(data["transactions"])
        data["transactions"] = [
            item for item in data["transactions"] if item["id"] != transaction_id
        ]
        if len(data["transactions"]) == original_count:
            return False
        self.storage.save(data)
        return True

    def totals(self, month=None):
        transactions = self.list_transactions()
        if month:
            transactions = [t for t in transactions if t["date"].startswith(month)]

        income = sum(t["amount"] for t in transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
        return {
            "income": round(income, 2),
            "expenses": round(expenses, 2),
            "balance": round(income - expenses, 2),
        }
