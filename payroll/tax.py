# Made-up annual slabs for the demo. Real slabs change every budget; see config/rates.yaml later.
SLABS = [(600_000, 0.0), (1_200_000, 0.05), (2_400_000, 0.15), (float("inf"), 0.25)]


def monthly_tax(annual: float) -> float:
    tax, lower = 0.0, 0.0
    for upper, rate in SLABS:
        if annual > lower:
            tax += (min(annual, upper) - lower) * rate
        lower = upper
    return tax
