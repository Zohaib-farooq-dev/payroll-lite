from payroll.tax import monthly_tax


def net_salary(basic: float, allowances: float = 0.0) -> dict:
    gross = basic + allowances
    tax = monthly_tax(gross * 12) / 12
    return {"gross": gross, "tax": round(tax, 2), "net": round(gross - tax, 2)}
