from src.permutation import Permutation
from src.cycle import Cycle, CycleFactors

def test_cycle_repr():
    assert repr(Cycle(5, [1, 2, 3])) == "(1 2 3)"
    assert repr(Cycle(5, [3, 1, 2])) == "(1 2 3)"
    assert repr(Cycle(5, [1])) == "(1)"
    assert repr(Cycle(5, [1, 2])) == "(1 2)"
    assert repr(Cycle(5, [2, 3])) == "(2 3)"

def test_cycle_eq():
    assert Cycle(5, [1, 2, 3]) == Cycle(5, [3, 1, 2])
    assert Cycle(4, [1, 2, 3]) != Cycle(5, [1, 2, 3])
    assert Cycle(4, [2, 3, 4]) == Cycle(4, [3, 4, 2])

def test_cycle_values():
    assert Cycle(5, [1, 2, 3]).get(3) == 1
    assert Cycle(5, [1, 2]).get(2) == 1
    assert Cycle(4, [2]).get(2) == 2

def test_permutation_factoring():
    assert Permutation(3, [1, 3, 2]).factor().factors == [Cycle(3, [1]), Cycle(3, [2, 3])]
    assert Permutation(4, [4, 1, 2, 3]).factor().factors == [Cycle(4, [4, 1, 2, 3])]
    assert Permutation(4, [1, 4, 3, 2]).factor().factors == [Cycle(4, [1, 4]), Cycle(4, [2, 3])]

def test_cycle_factors_repr():
    # Although kinda weird, this is more representative of the value of f(P_i)
    # on the permutation
    assert repr(Permutation(4, [1, 2, 3, 4])) == "()"

    assert repr(Permutation(4, [4, 1, 2, 3])) == "(1 4 3 2)"
    assert repr(Permutation(4, [1, 4, 3, 2])) == "(1 4)(2 3)"

# def test_counting_cycle_types():
    # pass
