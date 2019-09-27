from src.solver import Solver


def test_run() -> None:
    assert Solver.run("1/2 + 3/4") == "1_1/4"
    assert Solver.run("1 + 0") == "1"
    assert Solver.run("3_1/2 * 3") == "10_1/2"
    assert Solver.run("2_4/5 - 11/10") == "1_7/10"
    assert Solver.run("10 / 2") == "5"
    assert Solver.run("13/2 / 3/2") == "4_1/3"
    assert Solver.run("-1_1/3 - 1/3") == "-1_2/3"
    assert Solver.run("-1/2 * 2") == "-1"
