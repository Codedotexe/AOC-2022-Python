import unittest
from .main import Solution


class TestDay07(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(cls) -> None:
		data = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n" \
			   + "62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n" \
			   + "8033020 d.log\n5626152 d.ext\n7214296 k"
		cls.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(95437, self.solution.part1())

	#def testPart2(self):
	#	self.assertEqual("MCD", self.solution.part2())


if __name__ == '__main__':
	unittest.main()
