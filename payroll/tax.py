from payroll.rates import rates


def annual_tax(annual: float, fiscal_year: str | None = None) -> float:
    tax, lower = 0.0, 0.0
    for upper, rate in rates(fiscal_year)["slabs"]:
        if annual > lower:
            tax += (min(annual, upper) - lower) * rate
        lower = upper
    return float(round(tax))  # FBR rounds the annual figure to the rupee; monthly rounding drifts


def monthly_tax(annual: float, fiscal_year: str | None = None) -> float:
    return annual_tax(annual, fiscal_year) / 12


def effective_rate(annual: float, fiscal_year: str | None = None) -> float:
    return round(annual_tax(annual, fiscal_year) / annual, 4) if annual else 0.0
