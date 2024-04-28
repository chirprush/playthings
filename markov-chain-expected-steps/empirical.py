import numpy as np
import numpy.linalg

from random import uniform

# The basic question we're trying to answer is, given a general Markov chain,
# what is the expected number of steps it takes for one state to transition
# to another?

transition = np.array([
    [0.25, 0.2, 0.7],
    [0.25, 0.5, 0.1],
    [0.50, 0.3, 0.2]
]).transpose()

print(transition @ np.linalg.inv(np.identity(3) - transition))

def get_index(P, row, t):
    for i in range(P.shape[1]):
        t -= P[row, i]

        if t <= 0:
            return i

    raise "Not a valid probability distribution"

# Using the transition matrix, simulate stepping through a Markov chain akin to
# a geometric random variable
def simulate(P, start, end):
    steps = 0
    current = start

    while current != end:
        t = uniform(0, 1)

        current = get_index(P, current, t)
        steps += 1

    return steps

total = 0
N = 0

for _ in range(N):
    total += simulate(transition, 0, 2)

print(total / N)
