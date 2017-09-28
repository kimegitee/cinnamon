import numpy as np

def solution(input):
	'''Given a molecular composition, calcute its weight
	'''
	return weight(parse(input))

def parse(input):
	'''Count number of molecules'''
	input = factor(input)
	keys = 'hconk'
	s = ''
	n = '' # Keeps track of number longer than 1 character
	for i, c in enumerate(input):
		if c.isalpha():
			s += c
		if c.isnumeric():
			n += c
			try:
				if input[i+1].isalpha():
					s += input[i-len(n)] * (int(n) - 1)
					n = ''
			except IndexError:
				s += input[i-len(n)] * (int(n) - 1)

	result = []
	for k in keys:
		result.append(s.count(k))

	return result

def factor(input):
	'''Return factored representation of formula'''
	input = input.lower()
	if paren(input) == (-1, -1):
		return input
	else:
		start, end = paren(input)
		i = end + 1
		num = ''
		while True:
			if i != len(input) and input[i].isnumeric():
				num += input[i]
				i += 1
			else:
				break
		if num == '':
			num = '1'
		middle = input[start+1: end] * int(num)
		result = input[:start] + middle + input[end+len(num)+1:]
		return factor(result)



def paren(input):
	'''Detect outer-most parens, or first pair if equal level
	
	Params:
		input: string

	Returns:
		(int, int): indices of outer most or first pair of parens, 
			(-1, -1) if no parens found
	'''
	o = 0
	c = 0
	start = -1
	end = -1
	for i, char in enumerate(input):
		if char == '(':
			if start == -1:
				start = i
			o += 1
		if char == ')':
			c += 1
			if c == o:
				end = i
				# Break at the first pair
				break
	return (start, end)



def weight(x):
	w = [1, 12, 16, 14, 39]
	return np.matmul(w, x)