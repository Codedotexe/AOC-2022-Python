from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd


class Solution(PuzzleSolution):
	rucksacks = []

	class Rucksack:
		first_compartment = set()
		second_compartment = set()

		def __init__(self, items):
			assert (len(items) % 2 == 0)
			self.firstCompartment = set(items[:int(len(items) / 2)])
			self.secondCompartment = set(items[int(len(items) / 2):])

		def items_in_both_compartments(self):
			return self.firstCompartment.intersection(self.secondCompartment)

		def items(self):
			return self.firstCompartment.union(self.secondCompartment)

		@classmethod
		def intersection(cls, rucksacks):
			return set.intersection(*map(lambda x: x.items(), rucksacks))

	@staticmethod
	def item_to_priority(item):
		if "a" <= item <= "z":
			return ord(item) - ord("a") + 1
		elif "A" <= item <= "Z":
			return ord(item) - ord("A") + 27
		else:
			raise RuntimeError("Unknown item")

	def __init__(self, data):
		super().__init__(data)
		data = data.strip("\n").split("\n")
		for entryStr in data:
			self.rucksacks.append(self.Rucksack(list(entryStr)))
		assert (len(self.rucksacks) > 1)

	def part1(self) -> int:
		priority_sum = 0
		# Iterate over rucksacks, and sum the priorities of the intersection between the two compartments of each rucksack
		for rucksack in self.rucksacks:
			intersectingItems = rucksack.items_in_both_compartments()
			priority_sum += sum(map(self.item_to_priority, intersectingItems))
		return priority_sum

	def part2(self):
		prioritySum = 0
		assert (len(self.rucksacks) % 3 == 0)

		# Iterate over rucksacks in tuples of three, and sum the priorities of the intersections between them
		for i in range(0, len(self.rucksacks), 3):
			intersecting_items = self.Rucksack.intersection(self.rucksacks[i:i + 3])
			prioritySum += sum(map(self.item_to_priority, intersecting_items))
		return prioritySum


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=3, year=2022))
	print(solution.part1())
	print(solution.part2())
