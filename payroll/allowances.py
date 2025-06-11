MEDICAL_EXEMPT_SHARE = 0.10  # of basic


def split(basic: float, medical: float = 0.0, other: float = 0.0) -> dict:
    exempt = min(medical, basic * MEDICAL_EXEMPT_SHARE)
    return {"taxable": other + (medical - exempt), "exempt": exempt}
