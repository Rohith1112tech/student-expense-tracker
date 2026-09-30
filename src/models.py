from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Transaction:
    id: str
    type: str
    description: str
    amount: float
    category: str
    date: str

    def to_dict(self) -> Dict:
        return asdict(self)
