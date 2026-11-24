"""Independent synthetic benchmark example; no clinical or predictive functionality."""
from dataclasses import dataclass
from math import isfinite, fsum

@dataclass(frozen=True)
class Record:
    identifier: str
    observed: float
    predicted: float

def evaluate(records: list[Record]) -> dict:
    if not records:
        raise ValueError("At least one record required")
    seen = set()
    errors = []
    for row in records:
        if not row.identifier.strip() or row.identifier in seen:
            raise ValueError("Unique nonempty identifiers required")
        seen.add(row.identifier)
        if not all(type(x) in (int, float) and isfinite(x) for x in (row.observed, row.predicted)):
            raise ValueError("Finite numeric values required")
        error = abs(row.predicted - row.observed)
        if not isfinite(error):
            raise ValueError("Error exceeds numeric range")
        errors.append(error)
    return {"n": len(errors), "absolute_errors": errors, "mae": fsum(x / len(errors) for x in errors)}

if __name__ == "__main__":
    print(evaluate([Record("synthetic-A", -2, -2.5), Record("synthetic-B", -3, -2), Record("synthetic-C", -1, -1)]))
