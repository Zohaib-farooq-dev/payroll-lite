from datetime import date

from payroll.rates import current_fiscal_year


def test_july_starts_new_year():
    assert current_fiscal_year(date(2026, 6, 30)) == "FY2026"
    assert current_fiscal_year(date(2026, 7, 1)) == "FY2027"
