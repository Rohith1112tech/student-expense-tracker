import json
from pathlib import Path


class JsonStorage:
    """Handles persistent application data in JSON format."""

    def __init__(self, filename):
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        if not self.filename.exists():
            self.save({"transactions": [], "budgets": {}})

    def load(self):
        try:
            with self.filename.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {"transactions": [], "budgets": {}}

    def save(self, data):
        temporary = self.filename.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        temporary.replace(self.filename)
