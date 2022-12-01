import unittest
from src.Day01.main import Solution

class TestDay01(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(self) -> None:
		data = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
		self.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(24000, self.solution.part1())

	def testPart2(self):
		self.assertEqual(45000, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
