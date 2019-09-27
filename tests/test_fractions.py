from src.fraction import Fraction
from src.dict_types import FractionElements


def test_fraction_strings() -> None:
    assert str(Fraction("-1", "2")) == "-1/2"
    assert str(Fraction("4", "2")) == "2"
    assert str(Fraction("-10", "9")) == "-1_1/9"
    assert str(Fraction("-4", "1")) == "-4"
    assert str(Fraction("50", "2")) == "25"


def test_extract_from_dict() -> None:
    assert Fraction.extract_from_dict(
        FractionElements(sign="", whole_number="", numerator="1", denominator="2")
    ) == (1, 2)
    assert Fraction.extract_from_dict(
        FractionElements(sign="", whole_number="3", numerator="1", denominator="2")
    ) == (7, 2)
    assert Fraction.extract_from_dict(
        FractionElements(sign="", whole_number="3", numerator="", denominator="")
    ) == (3, 1)
    assert Fraction.extract_from_dict(
        FractionElements(sign="-", whole_number="", numerator="1", denominator="2")
    ) == (-1, 2)
    assert Fraction.extract_from_dict(
        FractionElements(sign="-", whole_number="3", numerator="1", denominator="2")
    ) == (-7, 2)
    assert Fraction.extract_from_dict(
        FractionElements(sign="-", whole_number="3", numerator="", denominator="")
    ) == (-3, 1)


def test_fraction_add() -> None:
    assert str(Fraction("1", "2") + Fraction("1", "2")) == "1"
    assert str(Fraction("2", "1") + Fraction("3", "4")) == "2_3/4"
    assert str(Fraction("1", "9") + Fraction("8", "9")) == "1"
    assert str(Fraction("10", "2") + Fraction("18", "3")) == "11"
    assert str(Fraction("10", "28") + Fraction("100", "56")) == "2_1/7"


def test_fraction_sub() -> None:
    assert str(Fraction("1", "2") - Fraction("3", "4")) == "-1/4"
    assert str(Fraction("-1", "2") - Fraction("3", "4")) == "-1_1/4"
    assert str(Fraction("10", "2") - Fraction("3", "1")) == "2"
    assert str(Fraction("2", "3") - Fraction("-3", "4")) == "1_5/12"
    assert str(Fraction("3", "1") - Fraction("1", "60")) == "2_59/60"


def test_fraction_mul() -> None:
    assert str(Fraction("1", "2") * Fraction("3", "4")) == "3/8"
    assert str(Fraction("-5", "1") * Fraction("-1", "2")) == "2_1/2"
    assert str(Fraction("1", "5") * Fraction("3", "1")) == "3/5"
    assert str(Fraction("14", "2") * Fraction("200", "4")) == "350"
    assert str(Fraction("-1", "2") * Fraction("3", "5")) == "-3/10"


def test_fraction_div() -> None:
    assert str(Fraction("1", "2") / Fraction("6", "5")) == "5/12"
    assert str(Fraction("-7", "8") / Fraction("2", "1")) == "-7/16"
    assert str(Fraction("33", "50") / Fraction("-1", "3")) == "-1_49/50"
    assert str(Fraction("-2", "1") / Fraction("3", "60")) == "-40"
    assert str(Fraction("-8", "67") / Fraction("-2", "9")) == "36/67"


def test_repr() -> None:
    assert repr(Fraction("1", "2")) == "Fraction('1', '2')"
    assert repr(Fraction("-10", "200")) == "Fraction('-10', '200')"
    assert repr(Fraction("5", "12")) == "Fraction('5', '12')"
