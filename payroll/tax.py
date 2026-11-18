from payroll.rates import rates


def monthly_tax(annual: float, fiscal_year: str = "FY2025") -> float:
    tax, lower = 0.0, 0.0
    for upper, rate in rates(fiscal_year)["slabs"]:
        if annual > lower:
            tax += (min(annual, upper) - lower) * rate
        lower = upper
    return tax
