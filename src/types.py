from mypy_extensions import TypedDict


FractionElements = TypedDict(
    "FractionElements",
    {"sign": str, "whole_number": str, "numerator": str, "denominator": str},
)
InputElements = TypedDict(
    "InputElements", {"first_operand": str, "operator": str, "second_operand": str}
)
