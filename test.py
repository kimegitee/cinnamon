import unittest
import numpy as np
from problem1 import *
import problem2 as p2
import problem3 as p3

class Problem1Test(unittest.TestCase):

	def setUp(self):
		self.input = 'K(OH)10O'
		self.input2 = 'KH2(OH(OH)2(OH)3(OH(K5)2)20)6'
		self.input3 = 'KH2(OH(OH)2(OH)3)2'

	def test_paren(self):
		self.assertEqual(paren(self.input), (1, 4))
		self.assertEqual(paren(self.input2), (3, 27))

	def test_parse(self):
		self.assertEqual(parse(self.input), [10, 0, 11, 0, 1])
		self.assertEqual(parse(self.input3), [14, 0, 12, 0, 1])
		self.assertEqual(parse(self.input2), [158, 0, 156, 0, 1201])

	def test_factor(self):
		self.assertEqual(factor(self.input), 'kohohohohohohohohohoho')
		self.assertEqual(factor(self.input3), 'kh2ohohohohohohohohohohohoh')

	def test_solution(self):
		self.assertEqual(solution(self.input), 225)
		self.assertEqual(solution(self.input2), 49493)

class Problem2Test(unittest.TestCase):

	def setUp(self):
		self.n1 = 19
		self.n2 = 931
		self.n3 = 914

	def test_solution(self):
		self.assertTrue(p2.solution(self.n1))
		self.assertTrue(p2.solution(self.n2))
		self.assertFalse(p2.solution(self.n3))

class Problem3Test(unittest.TestCase):

	def setUp(self):
		self.input = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3)]

	def test_member(self):
		self.assertTrue(p3.ismember((0, 0), (1, 1), (2, 2)))
		self.assertFalse(p3.ismember((0, 0), (1, 1), (2, 3)))
		self.assertEqual(p3.solution(self.input), 4)