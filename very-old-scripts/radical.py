#!/usr/bin/env python3
from sys import argv

def is_int(n):
    return n == int(n)

def is_square(n):
    return is_int(n ** (1/2))

if len(argv) == 2:
    n = int(argv[1])
else:
    n = int(input("Enter a number: "))
solutions = ["%d * sqrt(%d)" % (int(i ** (1/2)), n // i) for i in range(2, n + 1) if is_square(i) and is_int(n / i)]

if solutions:
    print(solutions[-1])
else:
    print("Cannot be factored further")
