from datetime import date
from pathlib import Path

import yaml

RATES_PATH = Path(__file__).resolve().parent.parent / "config" / "rates.yaml"


def current_fiscal_year(today: date | None = None) -> str:
    d = today or date.today()
    return f"FY{d.year + 1 if d.month >= 7 else d.year}"


def validate(block: dict) -> None:
    last = 0.0
    for upper, rate in block["slabs"]:
        if not isinstance(rate, (int, float)) or not 0 <= rate < 1 or upper < last:
            raise ValueError(f"bad slab {upper}, {rate}")  # a string here failed on payroll day last month
        last = upper
    for k in ("eobi_employee", "eobi_employer", "eobi_wage_ceiling"):
        if not isinstance(block[k], (int, float)):
            raise ValueError(f"{k} must be a number")


def rates(fiscal_year: str | None = None) -> dict:
    with open(RATES_PATH, encoding="utf-8") as f:
        block = yaml.safe_load(f)[fiscal_year or current_fiscal_year()]
    validate(block)
    return block
