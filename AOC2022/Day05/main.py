from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd
import copy
import re


class Solution(PuzzleSolution):
	moveInstructions = []
	stacks = dict()

	class MoveInstruction:
		amount = None
		source_stack_index = None
		destination_stack_index = None

		def __init__(self, amount, source_stack_index, destination_stack_index):
			self.amount = amount
			self.source_stack_index = source_stack_index
			self.destination_stack_index = destination_stack_index

		def move(self, stacks):
			source_stack = stacks[self.source_stack_index]
			destination_stack = stacks[self.destination_stack_index]
			for i in range(self.amount):
				destination_stack.append(source_stack.pop())

		def move_advanced(self, stacks):
			source_stack = stacks[self.source_stack_index]
			destination_stack = stacks[self.destination_stack_index]
			destination_stack += source_stack[-self.amount:]
			for i in range(self.amount):
				source_stack.pop()

	def __init__(self, data: str) -> None:
		super().__init__(data)
		layout_string, _, instructions_string = data.partition("\n\n")

		# Rotate the text block to 90 degrees
		cols = zip(*layout_string.rstrip("\n").split("\n"))
		for col in list(cols)[::-1]:
			new_row = ''.join(col)[::-1]
			new_row = new_row.rstrip(" ")

			# new_row now represents a whole stack
			if re.match("^\\d[A-Z]+$", new_row):
				stackIndex = int(new_row[0])
				stackEntries = list(new_row[1:])
				self.stacks[stackIndex] = stackEntries

		for i in instructions_string.rstrip("\n").split("\n"):
			match = re.search("^move (\\d+) from (\\d+) to (\\d+)$", i)
			assert (match is not None)
			self.moveInstructions.append(self.MoveInstruction(
				int(match.group(1)),
				int(match.group(2)),
				int(match.group(3))
			))

	@staticmethod
	def create_message(stacks):
		keys = list(stacks.keys())
		keys.sort()
		message = ""
		for key in keys:
			message += stacks[key][-1]
		return message

	def part1(self) -> str:
		stacksCopy = copy.deepcopy(self.stacks)
		for instruction in self.moveInstructions:
			instruction.move(stacksCopy)
		return self.create_message(stacksCopy)

	def part2(self) -> str:
		stacksCopy = copy.deepcopy(self.stacks)
		for instruction in self.moveInstructions:
			instruction.move_advanced(stacksCopy)
		return self.create_message(stacksCopy)


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=5, year=2022))
	print(solution.part1())
	print(solution.part2())
