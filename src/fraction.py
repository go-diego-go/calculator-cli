from typing import Dict, Tuple


class Fraction:
    def __init__(self, numerator="0", denominator="1", elements={}):
        if elements:
            self.numerator, self.denominator = Fraction.extract_from_dict(elements)
        else:
            self.numerator = int(numerator)
            self.denominator = int(denominator)

    @staticmethod
    def extract_from_dict(elements: Dict) -> Tuple:
        whole_number = int(elements["whole_number"] or "0")
        numerator = int(elements["numerator"] or "0")
        denominator = int(elements["denominator"] or "1")

        # Whole number (e.g. 3)
        if not numerator:
            numerator = whole_number

        # Mixed number (e.g. 3_1/2)
        elif whole_number:
            numerator = whole_number * denominator + numerator

        if elements["sign"] == "-":
            numerator *= -1

        # Regular fractions (e.g. 1/2) are implicitly covered
        return numerator, denominator

    @staticmethod
    def gcf(a, b) -> int:
        while b != 0:
            a, b = b, (a % b)
        return a

    def lcd(self, other) -> int:
        return (self.denominator * other.denominator) / self.gcf(
            abs(other.numerator), other.denominator
        )

    def lowest_terms(self):
        gcf = Fraction.gcf(abs(self.numerator), self.denominator)

        return Fraction(self.numerator / gcf, self.denominator / gcf)

    def __add__(self, other):
        # We could also be using the lcd here, but this code is more concise
        numerator = (self.numerator * other.denominator) + (
            other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator).lowest_terms()

    def __sub__(self, other):
        return self + Fraction(other.numerator * -1, other.denominator)

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator, self.denominator * other.denominator
        ).lowest_terms()

    def __truediv__(self, other):
        return self * Fraction(other.denominator, other.numerator)

    def __str__(self) -> str:
        # This approach favors mixed numbers over improper fractions

        sign = "-" if self.numerator < 0 else ""

        abs_numerator = abs(self.numerator)

        if abs_numerator >= self.denominator:
            whole_number = f"{abs_numerator // self.denominator}"
            remainder = abs_numerator % self.denominator
            fraction = f"_{remainder}/{self.denominator}" if remainder else ""
        else:
            whole_number = ""
            fraction = f"{abs_numerator}/{self.denominator}"

        return f"{sign}{whole_number}{fraction}"

    def __repr__(self) -> str:
        return f"Fraction('{self.numerator}', '{self.denominator}')"
