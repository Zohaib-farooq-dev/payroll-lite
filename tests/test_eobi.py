from payroll.eobi import eobi


def test_ceiling_applies():
    assert eobi(100_000)["employee"] == eobi(32_000)["employee"]
