import unittest
from .main import Solution


class TestDay07(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(cls) -> None:
		data = "30373\n25512\n65332\n33549\n35390"
		cls.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(21, self.solution.part1())

	def testPart2(self):
		self.assertEqual(8, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
