from typing import List, Tuple
from math import prod

class Entry:
    def __init__(self, comb: Tuple[int], sum_: int, product: int) -> None:
        self.comb = comb
        self.sum = sum_
        self.product = product

    def from_comb(comb: Tuple[int]) -> 'Entry':
        return Entry(comb, sum(comb), prod(comb))

    def __repr__(self) -> str:
        return f"({self.comb}, {self.sum}, {self.product})"

def combinations(f, n, ints: List[int] = None, start: int = 1) -> None:
    ints = [] if ints is None else ints
    if n == 0:
        f(tuple(ints))
    else:
        for i in range(start, 7):
            combinations(f, n - 1, [*ints, i], i + 1)

entries = []

for i in range(2, 7):
    combinations(lambda c: entries.append(Entry.from_comb(c)), i)

"""
print(len(entries))
for i in entries:
    print(i)

d = {}

for e in entries:
    if e.product in d:
        d[e.product].append(e)
    else:
        d[e.product] = [e]

print(d)
"""
