from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd
import re


class Solution(PuzzleSolution):
	pairs = []

	class Pair:
		aStart = None
		aEnd = None
		bStart = None
		bEnd = None

		def __init__(self, aStart: int, aEnd: int, bStart: int, bEnd: int) -> None:
			self.aStart = aStart
			self.aEnd = aEnd
			self.bStart = bStart
			self.bEnd = bEnd

		def encloses(self) -> bool:
			if self.aStart >= self.bStart and self.aEnd <= self.bEnd:  # b encloses a
				return True
			elif self.aStart <= self.bStart and self.aEnd >= self.bEnd:  # a encloses b
				return True
			else:
				return False

		def overlaps(self) -> bool:
			if self.aStart <= self.bStart <= self.aEnd:
				return True
			elif self.aStart <= self.bEnd <= self.aEnd:
				return True
			elif self.bStart <= self.aStart <= self.bEnd:
				return True
			elif self.bStart <= self.aEnd <= self.bEnd:
				return True
			else:
				return False

		def __repr__(self):
			return f"{self.aStart}-{self.aEnd},{self.bStart}-{self.bEnd}"

	def __init__(self, data: str) -> None:
		super().__init__(data)
		data = data.rstrip("\n").split("\n")
		for entryStr in data:
			match = re.search("^(\\d+)-(\\d+),(\\d+)-(\\d+)$", entryStr)
			assert (match is not None)
			self.pairs.append(self.Pair(
				int(match.group(1)),
				int(match.group(2)),
				int(match.group(3)),
				int(match.group(4))
			))

		assert (len(self.pairs) > 1)

	def part1(self) -> int:
		count = 0
		for pair in self.pairs:
			if pair.encloses():
				count += 1
		return count

	def part2(self):
		count = 0
		for pair in self.pairs:
			if pair.overlaps():
				count += 1
		return count


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=4, year=2022))
	print(solution.part1())
	print(solution.part2())
