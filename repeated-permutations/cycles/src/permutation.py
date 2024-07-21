from dataclasses import dataclass
from typing import List

from src.cycle import Cycle, CycleFactors

@dataclass
class Permutation:
    n: int
    order: List[int]

    def factor(self) -> CycleFactors:
        cycles = []
        cycle = []
        known = set()

        for i in self.order:
            if i not in known:
                j = i
                while (j := self.order[j - 1]) not in known:
                    known.add(j)
                    cycle.append(j)
                cycles.append(Cycle(self.n, cycle))
                cycle = []

        return CycleFactors(self.n, cycles)

    def __repr__(self) -> str:
        return f"({' '.join(map(str, self.order))})"
