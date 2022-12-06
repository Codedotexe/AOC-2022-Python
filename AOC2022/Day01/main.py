from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd

class Solution(PuzzleSolution):
	elves = []

	def __init__(self, data):
		data = data.strip("\n").split("\n\n")
		for elveStr in data:
			elve = list(map(int, elveStr.split("\n")))
			self.elves.append(elve)
		assert(len(self.elves) > 1)

		self.elvesSum = list(map(sum, self.elves))
		self.elvesSum.sort(reverse=True)

	def part1(self):
		# Beacause elvesSum is now sorted the biggest sum is at the beginning
		return self.elvesSum[0]

	def part2(self):
		# Sum the three biggest sums
		return sum(self.elvesSum[:3])

if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=1, year=2022))
	print(solution.part1())
	print(solution.part2())
