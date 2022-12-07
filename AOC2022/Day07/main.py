from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd


class Solution(PuzzleSolution):

	def __init__(self, data: str) -> None:
		super().__init__(data)

	def part1(self) -> int:
		pass

	#def part2(self) -> int:
	#	pass


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=7, year=2022))
	print(solution.part1())
	print(solution.part2())
