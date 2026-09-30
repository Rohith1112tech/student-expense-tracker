from collections import defaultdict


class AnalyticsService:
    def __init__(self, storage):
        self.storage = storage

    def category_totals(self, month=None):
        result = defaultdict(float)
        data = self.storage.load()

        for item in data["transactions"]:
            if item["type"] != "expense":
                continue
            if month and not item["date"].startswith(month):
                continue
            result[item["category"]] += item["amount"]

        return {key: round(value, 2) for key, value in result.items()}

    def highest_category(self, month=None):
        totals = self.category_totals(month)
        if not totals:
            return None
        return max(totals, key=totals.get)
