from payroll.eobi import eobi
from payroll.tax import monthly_tax


def net_salary(basic: float, allowances: float = 0.0, fiscal_year: str = "FY2025") -> dict:
    gross = basic + allowances
    tax = monthly_tax(gross * 12, fiscal_year) / 12
    contrib = eobi(basic, fiscal_year)
    return {"gross": gross, "tax": round(tax, 2), "eobi": contrib, "net": round(gross - tax - contrib["employee"], 2)}
