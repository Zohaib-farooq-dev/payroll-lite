from payroll.calc import net_salary

TEMPLATE = """<html><body style="font-family:sans-serif">
<h2>Payslip: {employee}</h2>
<table>{rows}</table>
</body></html>"""


def render(employee: str, **salary) -> str:
    result = net_salary(**salary)
    rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in result.items() if k != "eobi")
    return TEMPLATE.format(employee=employee, rows=rows)


def render_pdf(employee: str, **salary) -> bytes:
    from weasyprint import HTML  # optional dependency; image size decision pending with ops

    return HTML(string=render(employee, **salary)).write_pdf()
