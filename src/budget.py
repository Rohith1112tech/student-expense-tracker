from .validation import validate_month


class BudgetService:
    def __init__(self, storage):
        self.storage = storage

    def set_budget(self, month, amount):
        validate_month(month)
        if amount <= 0:
            raise ValueError("Budget must be greater than zero.")

        data = self.storage.load()
        data["budgets"][month] = round(float(amount), 2)
        self.storage.save(data)

    def get_status(self, month):
        validate_month(month)
        data = self.storage.load()
        budget = float(data["budgets"].get(month, 0))
        expenses = sum(
            item["amount"]
            for item in data["transactions"]
            if item["type"] == "expense" and item["date"].startswith(month)
        )

        remaining = budget - expenses
        usage = (expenses / budget * 100) if budget else 0

        if budget == 0:
            status = "No budget set"
        elif expenses > budget:
            status = "Over budget"
        else:
            status = "Within budget"

        return {
            "budget": round(budget, 2),
            "expenses": round(expenses, 2),
            "remaining": round(remaining, 2),
            "usage_percent": round(usage, 2),
            "status": status,
        }
