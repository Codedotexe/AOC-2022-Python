import unittest
from .main import Solution


class TestDay02(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(cls) -> None:
		data = "A Y\nB X\nC Z"
		cls.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(15, self.solution.part1())

	def testPart2(self):
		self.assertEqual(12, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
