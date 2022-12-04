from src.utils.PuzzleSolution import PuzzleSolution
from enum import Enum
import aocd

class Solution(PuzzleSolution):
	stratergyGuide = []
	shapeMap = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

	class RoundResult(Enum):
		WON = 6
		DRAW = 3
		LOST = 0

	def __init__(self, data):
		data = data.strip("\n").split("\n")
		for entryStr in data:
			pre, _, post = entryStr.partition(" ")
			self.stratergyGuide.append((pre, post))
		assert(len(self.stratergyGuide) > 1)

	def simulateRound(self, opponent, you) -> RoundResult:
		opponentNum = self.shapeMap[opponent]
		youNum = self.shapeMap[you]

		if opponentNum == 2 and youNum == 1: # paper beats rock
			return self.RoundResult.LOST
		elif opponentNum == 1 and youNum == 2: # paper beats rock
			return self.RoundResult.WON
		elif opponentNum == 3 and youNum == 2: # scissors beats paper
			return self.RoundResult.LOST
		elif opponentNum == 2 and youNum == 3: # scissors beats paper
			return self.RoundResult.WON
		elif opponentNum == 1 and youNum == 3: # rock beats scissors
			return self.RoundResult.LOST
		elif opponentNum == 3 and youNum == 1: # rock beats scissors
			return self.RoundResult.WON
		elif opponentNum == youNum: # draw
			return self.RoundResult.DRAW
		else:
			raise RuntimeError("Unknown combination")

	def part1(self) -> int:
		points = 0
		for opponent, you in self.stratergyGuide:
			points += self.simulateRound(opponent, you).value + self.shapeMap[you]
		return points

	def part2(self):
		pass

if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=2, year=2022))
	print(solution.part1())
	print(solution.part2())
