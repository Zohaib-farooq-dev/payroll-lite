import csv
import sys

from payroll.calc import net_salary


def main(path: str) -> None:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            result = net_salary(float(row["basic"]), float(row.get("allowances", 0) or 0))
            print(row["employee"], result["net"])


if __name__ == "__main__":
    main(sys.argv[1])
