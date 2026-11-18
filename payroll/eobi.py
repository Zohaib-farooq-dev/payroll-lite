from payroll.rates import rates


def eobi(basic: float, fiscal_year: str = "FY2025") -> dict:
    r = rates(fiscal_year)
    wage = min(basic, r["eobi_wage_ceiling"])  # ceiling applies to basic, not gross
    return {"employee": round(wage * r["eobi_employee"], 2), "employer": round(wage * r["eobi_employer"], 2)}
