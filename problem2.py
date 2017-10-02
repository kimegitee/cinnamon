def solution(input):
	'''Recursively check if a number is "happy"'''
	if input == 4: # 4 will recurse to 4 over and over
		return False
	happy = sum([int(n)**2 for n in str(input)])
	if happy == 1:
		return True
	return solution(happy)