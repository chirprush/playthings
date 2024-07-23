from math import factorial

def f(x):
    return sum(map(lambda i: int(i) ** 5, str(x)))

limit = 10 ** 6

for i in range(10, limit):
    if f(i) == i:
        print(i)
