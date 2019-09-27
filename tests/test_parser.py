from pytest import raises

from src.parser import Parser, FractionElements


def test_valid_inputs() -> None:
    # TODO: Use list to slightly reduce the amount of code duplication
    assert Parser.parse_input("1 + 2") == {
        "first_operand": "1",
        "operator": "+",
        "second_operand": "2",
    }
    assert Parser.parse_input("1/2 * 8/5") == {
        "first_operand": "1/2",
        "operator": "*",
        "second_operand": "8/5",
    }
    assert Parser.parse_input("3/4 - 2/2") == {
        "first_operand": "3/4",
        "operator": "-",
        "second_operand": "2/2",
    }
    assert Parser.parse_input("1     +        5") == {
        "first_operand": "1",
        "operator": "+",
        "second_operand": "5",
    }
    assert Parser.parse_input("7/6 / -5/6") == {
        "first_operand": "7/6",
        "operator": "/",
        "second_operand": "-5/6",
    }
    assert Parser.parse_input("12312321/12312312 + 1/1111111") == {
        "first_operand": "12312321/12312312",
        "operator": "+",
        "second_operand": "1/1111111",
    }
    assert Parser.parse_input("10/2 - 1/5") == {
        "first_operand": "10/2",
        "operator": "-",
        "second_operand": "1/5",
    }
    assert Parser.parse_input("1010 / 210") == {
        "first_operand": "1010",
        "operator": "/",
        "second_operand": "210",
    }
    assert Parser.parse_input("-80320  *   90/90") == {
        "first_operand": "-80320",
        "operator": "*",
        "second_operand": "90/90",
    }
    assert Parser.parse_input("2_3/8 + 9/8") == {
        "first_operand": "2_3/8",
        "operator": "+",
        "second_operand": "9/8",
    }
    assert Parser.parse_input("10_3/2 * 1_2/10") == {
        "first_operand": "10_3/2",
        "operator": "*",
        "second_operand": "1_2/10",
    }
    assert Parser.parse_input("1 - 0") == {
        "first_operand": "1",
        "operator": "-",
        "second_operand": "0",
    }


def test_invalid_inputs() -> None:
    test_inputs = [
        "bla",
        "1 + a",
        "--1/2 + 1",
        "01/2 + 25",
        "1 + 02/2",
        "1 + 2/02",
        "9/8 - 3//3",
        "2//3 + 1/2",
        "2+3",
        "2/3-4/5",
        "8/4/-7/9" "3 ++ 2",
        "2_1/5 x 8/10",
        " 1 + 2 ",
    ]
    for input in test_inputs:
        with raises(ValueError) as excinfo:
            Parser.parse_input(input)
        assert str(excinfo.value) == "Invalid input. Please try again."


def test_valid_fractions() -> None:
    test_inputs = (
        (
            "1/2",
            FractionElements(sign="", whole_number="", numerator="1", denominator="2"),
        ),
        (
            "1870/2",
            FractionElements(
                sign="", whole_number="", numerator="1870", denominator="2"
            ),
        ),
        (
            "1_2/3",
            FractionElements(sign="", whole_number="1", numerator="2", denominator="3"),
        ),
        (
            "-10_4/81",
            FractionElements(
                sign="-", whole_number="10", numerator="4", denominator="81"
            ),
        ),
        (
            "-5/6",
            FractionElements(sign="-", whole_number="", numerator="5", denominator="6"),
        ),
        (
            "0",
            FractionElements(sign="", whole_number="0", numerator="", denominator=""),
        ),
        (
            "-5",
            FractionElements(sign="-", whole_number="5", numerator="", denominator=""),
        ),
    )
    for input, output in test_inputs:
        assert Parser.parse_fraction(input) == output
