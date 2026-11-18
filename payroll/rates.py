from datetime import date
from pathlib import Path

import yaml

RATES_PATH = Path(__file__).resolve().parent.parent / "config" / "rates.yaml"


def current_fiscal_year(today: date | None = None) -> str:
    d = today or date.today()
    return f"FY{d.year + 1 if d.month >= 7 else d.year}"


def rates(fiscal_year: str | None = None) -> dict:
    with open(RATES_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)[fiscal_year or current_fiscal_year()]
