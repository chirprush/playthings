import numpy
from matplotlib import pyplot
from math import factorial

pyplot.rcParams["figure.figsize"] = [7.50, 3.50]
pyplot.rcParams["figure.autolayout"] = True

def f(x):
    return x

def g(x):
    return sum(map(lambda i: factorial(int(i)), str(x)))

right_bound = 1000

pyplot.xlim([0, right_bound])
pyplot.ylim([0, right_bound * 10])

for x in range(right_bound):
    pyplot.plot(x, f(x), "ro")
    pyplot.plot(x, g(x), "bo")


pyplot.show()
