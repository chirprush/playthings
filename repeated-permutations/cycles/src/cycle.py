from dataclasses import dataclass
from typing import List

@dataclass
class Cycle:
    n: int
    order: List[int]

    def __init__(self, n: int, order: List[int]) -> None:
        self.n = n

        # It's nice to have the cycle ordered with the minimum element at the
        # start
        start = order.index(min(order))
        self.order = [order[(start + i) % len(order)] for i in range(len(order))]

    def get(self, n: int) -> int:
        ind = self.order.index(n)
        return self.order[(ind + 1) % len(self.order)]

    def __repr__(self) -> str:
        return f"({' '.join(map(str, self.order))})"

@dataclass
class CycleFactors:
    n: int
    factors: List[Cycle]

    def __init__(self, n: int, factors: List[Cycle]) -> None:
        self.n = n

        self.factors = sorted(factors, key=lambda cycle: min(cycle.order))

    def __repr__(self) -> str:
        visible = [cycle for cycle in self.factors if len(cycle.order) > 1]

        if not visible:
            return "({' '.join(map(str, range(1, self.n + 1)))})"

        return ''.join(map(repr, ))
