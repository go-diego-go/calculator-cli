class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    @staticmethod
    def gcf(a, b):
        while b != 0:
            a, b = b, (a % b)
        return a

    def lcd(self, other):
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

    def __str__(self):
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
