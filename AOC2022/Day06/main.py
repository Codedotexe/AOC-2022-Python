from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd


class Solution(PuzzleSolution):
	datastreamBuffer = None

	def __init__(self, data: str) -> None:
		super().__init__(data)
		self.datastreamBuffer = data

	@staticmethod
	def no_duplicates(iterable):
		# If both length are the same the iterable contains no duplicate entries,
		# because sets cannot contain duplicates
		return len(iterable) == len(set(iterable))

	def find_marker(self, markerLength) -> int:
		datastreamBufferLength = len(self.datastreamBuffer)
		for i in range(markerLength, datastreamBufferLength):
			if self.no_duplicates(self.datastreamBuffer[i - markerLength:i]):
				return i
		raise RuntimeError("No Marker found")

	def part1(self) -> int:
		return self.find_marker(4)

	def part2(self) -> int:
		return self.find_marker(14)


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=6, year=2022))
	print(solution.part1())
	print(solution.part2())
