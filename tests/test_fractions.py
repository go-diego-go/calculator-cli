from src.fraction import Fraction


def test_fraction_strings():
    assert str(Fraction("-1", "2")) == "-1/2"
    assert str(Fraction("4", "2")) == "2"
    assert str(Fraction("-10", "9")) == "-1_1/9"
    # TODO: add more scenarios


def test_fraction_add():
    assert str(Fraction("1", "2") + Fraction("1", "2")) == "1"
    # TODO: add more scenarios


def test_fraction_sub():
    assert str(Fraction("1", "2") - Fraction("3", "4")) == "-1/4"
    # TODO: add more scenarios


def test_fraction_mul():
    assert str(Fraction("1", "2") * Fraction("3", "4")) == "3/8"
    # TODO: add more scenarios


def test_fraction_div():
    assert str(Fraction("1", "2") / Fraction("6", "5")) == "5/12"
    # TODO: add more scenarios
