import re
from typing import Tuple

from src.fraction import Fraction
from src.dict_types import InputElements, FractionElements

WHOLE_NUMBER = r"0|-?(?:[1-9]\d*_?)?"
FRACTION_ELEMENT = r"[1-9]\d*"
OPERAND = fr"{WHOLE_NUMBER}{FRACTION_ELEMENT}\/?(?:{FRACTION_ELEMENT})?)"
INPUT_PARSER = re.compile(
    (
        # Match first operand
        # Allow for fractions, whole numbers and negative values
        f"^(?P<first_operand>{OPERAND}"
        # Match operation symbol (and any spacing in between)
        r"[ ]+(?P<operator>[+\/*-])[ ]+"
        # Match second operand
        # Allow for fractions, whole numbers and negative values
        f"(?P<second_operand>{OPERAND}$"
    )
)
FRACTION_PARSER = re.compile(
    (
        f"^(?P<whole_number>{WHOLE_NUMBER})"
        f"(?P<numerator>{FRACTION_ELEMENT})?"
        r"(?:\/?)"
        fr"(?P<denominator>({FRACTION_ELEMENT})?)$"
    )
)


class Parser:
    @staticmethod
    def build_operation(input: str) -> Tuple[Fraction, str, Fraction]:
        elements: InputElements = Parser.parse_input(input)

        first_operand = Fraction(
            elements=Parser.parse_fraction(elements["first_operand"])
        )
        second_operand = Fraction(
            elements=Parser.parse_fraction(elements["second_operand"])
        )

        return first_operand, elements["operator"], second_operand

    @staticmethod
    def parse_input(input: str) -> InputElements:
        matches = INPUT_PARSER.match(input)

        if not matches:
            raise ValueError("Invalid input. Please try again.")

        return InputElements(
            first_operand=matches.group("first_operand"),
            operator=matches.group("operator"),
            second_operand=matches.group("second_operand"),
        )

    @staticmethod
    def parse_fraction(input: str) -> FractionElements:
        # TODO: this approach is uglier, try to use regex if possible
        result = FractionElements(
            sign="", whole_number="", numerator="", denominator=""
        )

        if input[0] == "-":
            result["sign"] = input[0]
            input = input[1:]

        whole_number_parts = input.split("_")
        if len(whole_number_parts) == 2:
            whole_number, fraction = whole_number_parts
            result["whole_number"] = whole_number
            result["numerator"], result["denominator"] = fraction.split("/")

        else:
            fraction_parts = input.split("/")
            if len(fraction_parts) == 2:
                result["numerator"], result["denominator"] = fraction_parts
            else:
                result["whole_number"] = input

        return result
