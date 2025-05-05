from payroll.calc import net_salary


def test_no_tax_under_threshold():
    assert net_salary(40_000)["tax"] == 0
