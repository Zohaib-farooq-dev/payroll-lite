from payroll.allowances import split
from payroll.eobi import eobi
from payroll.tax import monthly_tax


def net_salary(basic: float, medical: float = 0.0, other: float = 0.0, fiscal_year: str = "FY2025") -> dict:
    parts = split(basic, medical, other)
    gross = basic + medical + other
    taxable = basic + parts["taxable"]
    tax = monthly_tax(taxable * 12, fiscal_year) / 12
    contrib = eobi(basic, fiscal_year)
    return {"gross": gross, "taxable": taxable, "tax": round(tax, 2), "eobi": contrib, "net": round(gross - tax - contrib["employee"], 2)}
