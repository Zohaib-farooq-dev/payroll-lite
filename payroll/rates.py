from pathlib import Path

import yaml

RATES_PATH = Path(__file__).resolve().parent.parent / "config" / "rates.yaml"


def rates(fiscal_year: str = "FY2025") -> dict:
    with open(RATES_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)[fiscal_year]
