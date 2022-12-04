import unittest
from src.Day03.main import Solution

class TestDay03(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(self) -> None:
		data = "\n".join([
			"vJrwpWtwJgWrhcsFMMfFFhFp",
			"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
			"PmmdzqPrVvPwwTWBwg",
			"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
			"ttgJtRGJQctTZtZT",
			"CrZsJsPPZsGzwwsLwLmpwMDw"
		])
		self.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(157, self.solution.part1())

	def testPart2(self):
		self.assertEqual(70, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
