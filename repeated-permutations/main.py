from typing import List
from dataclasses import dataclass
from itertools import count

@dataclass
class Permutation:
    order: List[int]

    def __init__(self, _order: List[int]) -> None:
        # Represents the ordering of the permutation. Like elements of S_n,
        # the values in this should be in the range [1, n]
        self.order = _order
        self.n = len(self.order)

    def compose(self, other: 'Permutation') -> 'Permutation':
        # Composition order: self . other
        assert self.n == other.n

        return Permutation([self.order[other.order[i] - 1] for i in range(self.n)])

    def swap(self) -> int:
        # We define the swap number of a permutation p to be the minimum amount
        # of times p must be composed with itself to result in the identity
        # element (minus one). An interesting exercise would be to prove that
        # all permutations must return back to the identity element, but I'll
        # leave that for future me to figure out.
        # 
        # \operatorname{Sw} p \vcentcolon= n, where p is an element of S_N and
        # n is the minimum positive integer such that p^(n + 1) = (1 2 ... N)
        #
        # In code, the swap number of p is p.swap() - 1. This off-by-one distinction
        # is made because of how I order and generate permutations using arrows.

        # LET'S GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO THIS IS ALL WRONG

        p = self
        identity = Permutation([i for i in range(1, self.n + 1)])

        for i in count(1):
            if p == identity:
                return i
            p = p.compose(self)

    def __eq__(self, other: 'Permutation') -> bool:
        return self.order == other.order

    def __repr__(self) -> str:
        return f"({' '.join(map(str, self.order))})"

# There's a couple problems that I want to tackle in this, but first of all, I'm going to
# use this to verify some calculations.

identity = Permutation([1, 2, 3, 4])
one_swap = Permutation([2, 1, 3, 4])
two_swap = Permutation([3, 1, 2, 4])
rotate = Permutation([2, 3, 4, 1])

print("Identity:", identity, "->", identity.swap())
print("1-swap:  ", one_swap, "->", one_swap.swap())
print("2-swap:  ", two_swap, "->", two_swap.swap())
print("Rotation:", rotate,   "->", rotate.swap())

print(Permutation([3, 1, 2]).swap())
