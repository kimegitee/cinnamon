def solution(input, depth=500):
	if depth <= 0:
		return False
	happy = sum([int(n)**2 for n in str(input)])
	if happy == 1:
		return True
	return solution(happy, depth-1)