import copy
from pprint import pprint

from src.utils.PuzzleSolution import PuzzleSolution
import aocd
import re

class Solution(PuzzleSolution):
	moveInstructions = []
	stacks = dict()

	class MoveInstruction:
		amount = None
		srcStackIndex = None
		destStackIndex = None

		def __init__(self, amount, srcStackIndex, destStackIndex):
			self.amount = amount
			self.srcStackIndex = srcStackIndex
			self.destStackIndex = destStackIndex

		def move(self, stacks):
			srcStack = stacks[self.srcStackIndex]
			destStack = stacks[self.destStackIndex]
			for i in range(self.amount):
				destStack.append(srcStack.pop())

		def moveAdvanced(self, stacks):
			srcStack = stacks[self.srcStackIndex]
			destStack = stacks[self.destStackIndex]
			destStack += srcStack[-self.amount:]
			for i in range(self.amount):
				srcStack.pop()

	def __init__(self, data: str) -> None:
		layoutStr, _, instructionsStr = data.partition("\n\n")

		# Rotate the text block to 90 degrees
		cols = zip(*layoutStr.rstrip("\n").split("\n"))
		for col in list(cols)[::-1]:
			newRow = ''.join(col)[::-1]
			newRow = newRow.rstrip(" ")

			# newRow now represents a whole stack
			if re.match("^\d[A-Z]+$", newRow):
				stackIndex = int(newRow[0])
				stackEntries = list(newRow[1:])
				self.stacks[stackIndex] = stackEntries

		for i in instructionsStr.rstrip("\n").split("\n"):
			match = re.search("^move (\d+) from (\d+) to (\d+)$", i)
			assert(match is not None)
			self.moveInstructions.append(self.MoveInstruction(
				int(match.group(1)),
				int(match.group(2)),
				int(match.group(3))
			))

	def createMessage(self, stacks):
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
		return self.createMessage(stacksCopy)

	def part2(self) -> int:
		stacksCopy = copy.deepcopy(self.stacks)
		for instruction in self.moveInstructions:
			instruction.moveAdvanced(stacksCopy)
		return self.createMessage(stacksCopy)


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=5, year=2022))
	print(solution.part1())
	print(solution.part2())
