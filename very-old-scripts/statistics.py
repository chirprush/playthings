#!/usr/bin/env python3
from math import sqrt
from os import system
def mean(l):
	return sum(l)/len(l)

def median(l):
	cpy = l[:]
	while len(cpy) > 2:
		cpy = cpy[1:-1]
	return mean(cpy)

def mode(l):
	result = max([(n, l.count(n)) for n in l], key=lambda n: n[1])[0]
	if (l.count(result) == 1):
		return "None"

def _range(l):
	return l[-1]-l[0]

def standard_dev(l):
	m = mean(l)
	top = sum([(n - m)**2 for n in l])
	top /= len(l)
	return sqrt(top)

def quartiles(l):
	if (len(l) % 2):
		del l[len(l)//2]
	lower_half = l[:len(l)//2]
	upper_half = l[len(l)//2:]
	return (median(lower_half),median(upper_half))

def print_stat(l):
	print("Sorted: %s" % nums)
	print("Mean: %s" % round(mean(nums), 3))
	print("Median: %s" % round(median(nums), 3))
	print("Mode: %s" % mode(nums))
	print("Range: %s" % round(_range(nums), 3))
	print("Standard deviation: %s" % round(standard_dev(nums), 3))

def print_box(l):
	le = l[0]
	ue = l[-1]
	lq,uq = quartiles(l[:])
	m = median(l)
	print("Lower Extreme: %d" % le)
	print("Lower Quartile: %d" % lq)
	print("Median: %d" % m)
	print("Upper Quartile: %d" % uq)
	print("Upper Extreme: %d" % ue)
	print("Range: %d" % (ue-le))
	print("QRange: %d" % (uq-lq))

if __name__ == "__main__":
	while True:
		nums = [round(eval(i), 3) for i in input().split(" ")]
		system("clear")
		nums.sort()
		print_box(nums)
