from payroll.rates import rates


def eobi(basic: float, fiscal_year: str | None = None) -> dict:
    r = rates(fiscal_year)  # resolved per call: a default captured at import kept the FY2025 ceiling after the switch
    wage = min(basic, r["eobi_wage_ceiling"])  # ceiling applies to basic, not gross
    return {"employee": round(wage * r["eobi_employee"], 2), "employer": round(wage * r["eobi_employer"], 2)}
