import unittest
from .main import Solution


class TestDay09(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(cls) -> None:
		data = "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"
		cls.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(13, self.solution.part1())

	#def testPart2(self):
	#	self.assertEqual(8, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
