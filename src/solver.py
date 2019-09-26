import operator

from .parser import Parser


OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


class Solver:
    @staticmethod
    def run(input: str) -> str:
        operand_1, operator, operand_2 = Parser.build_operation(input)

        return str(OPERATIONS[operator](operand_1, operand_2))
