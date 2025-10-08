from payroll.allowances import split
from payroll.eobi import eobi
from payroll.tax import monthly_tax


def net_salary(basic: float, medical: float = 0.0, other: float = 0.0, fiscal_year: str | None = None) -> dict:
    parts = split(basic, medical, other)
    gross = basic + medical + other
    taxable = basic + parts["taxable"]
    tax = monthly_tax(taxable * 12, fiscal_year) / 12
    contrib = eobi(basic, fiscal_year)
    return {"gross": gross, "taxable": taxable, "tax": round(tax, 2), "eobi": contrib, "net": round(gross - tax - contrib["employee"], 2)}


def annual_summary(basic: float, medical: float = 0.0, other: float = 0.0, fiscal_year: str | None = None) -> dict:
    month = net_salary(basic, medical, other, fiscal_year)
    return {k: round(month[k] * 12, 2) for k in ("gross", "tax", "net")} | {"eobi_employee": round(month["eobi"]["employee"] * 12, 2)}
