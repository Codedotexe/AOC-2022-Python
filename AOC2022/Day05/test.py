import unittest
from .main import Solution

class TestDay05(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(self) -> None:
		data = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 "\
			   "to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n"
		self.solution = Solution(data)

	def testPart1(self):
		self.assertEqual("CMZ", self.solution.part1())

	def testPart2(self):
		self.assertEqual("MCD", self.solution.part2())


if __name__ == '__main__':
	unittest.main()
