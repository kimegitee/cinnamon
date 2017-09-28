import numpy as np
from itertools import combinations

def solution(input):
	'''Find the maximum number of points on the same line in a 2d plane

	Params:
		input: list of tuple of x, y coordinates
	
	Returns:
		result: int, max number of points on the same line
	'''
	input = set(input)
	if len(input) <= 2:
		return len(input)
	pairs = combinations(input, 2)
	best = 2
	for pair in pairs:
		n = 2
		for point in input:
			a, b = pair
			if a != point and b != point and ismember(a, b, point):
				n += 1
		if n > best:
			best = n
	return best


def ismember(a, b, x):
	'''Check if x is on the same line as two points a,b'''
	xa, ya = a
	xb, yb = b
	xx, yx = x
	print(a, b, x)
	return True if (yx-ya)/(xx-xa) == (yb-ya)/(xb-xa) else False