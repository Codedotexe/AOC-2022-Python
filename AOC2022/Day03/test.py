import unittest
from .main import Solution


class TestDay03(unittest.TestCase):
	solution = None

	@classmethod
	def setUpClass(cls) -> None:
		# noinspection SpellCheckingInspection
		data = "\n".join([
			"vJrwpWtwJgWrhcsFMMfFFhFp",
			"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
			"PmmdzqPrVvPwwTWBwg",
			"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
			"ttgJtRGJQctTZtZT",
			"CrZsJsPPZsGzwwsLwLmpwMDw"
		])
		cls.solution = Solution(data)

	def testPart1(self):
		self.assertEqual(157, self.solution.part1())

	def testPart2(self):
		self.assertEqual(70, self.solution.part2())


if __name__ == '__main__':
	unittest.main()
