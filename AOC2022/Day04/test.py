import unittest
from .main import Solution

class TestDay04(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(self) -> None:
		data = "\n".join([
			"2-4,6-8",
			"2-3,4-5",
			"5-7,7-9",
			"2-8,3-7",
			"6-6,4-6",
			"2-6,4-8"
		])
		self.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(2, self.solution.part1())

	def testPart2(self):
		self.assertEqual(4, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
