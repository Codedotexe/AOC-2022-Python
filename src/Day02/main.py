from src.utils.PuzzleSolution import PuzzleSolution
from enum import Enum
import aocd


class Solution(PuzzleSolution):
	strategyGuide = []

	class RoundResult(Enum):
		WON = 6
		DRAW = 3
		LOST = 0

	class HandShape(Enum):
		ROCK = 1
		PAPER = 2
		SCISSORS = 3

	# (opponent shape, your shape): game outcome for you
	gameResultsLookup = {
		(HandShape.ROCK, HandShape.PAPER): RoundResult.WON,
		(HandShape.PAPER, HandShape.ROCK): RoundResult.LOST,
		(HandShape.PAPER, HandShape.SCISSORS): RoundResult.WON,
		(HandShape.SCISSORS, HandShape.PAPER): RoundResult.LOST,
		(HandShape.SCISSORS, HandShape.ROCK): RoundResult.WON,
		(HandShape.ROCK, HandShape.SCISSORS): RoundResult.LOST,
		(HandShape.ROCK, HandShape.ROCK): RoundResult.DRAW,
		(HandShape.PAPER, HandShape.PAPER): RoundResult.DRAW,
		(HandShape.SCISSORS, HandShape.SCISSORS): RoundResult.DRAW
	}

	# (opponent shape, indicated outcome): your shape
	shapeLookup = {
		(HandShape.ROCK, RoundResult.WON): HandShape.PAPER,
		(HandShape.ROCK, RoundResult.LOST): HandShape.SCISSORS,
		(HandShape.ROCK, RoundResult.DRAW): HandShape.ROCK,
		(HandShape.PAPER, RoundResult.WON): HandShape.SCISSORS,
		(HandShape.PAPER, RoundResult.LOST): HandShape.ROCK,
		(HandShape.PAPER, RoundResult.DRAW): HandShape.PAPER,
		(HandShape.SCISSORS, RoundResult.WON): HandShape.ROCK,
		(HandShape.SCISSORS, RoundResult.LOST): HandShape.PAPER,
		(HandShape.SCISSORS, RoundResult.DRAW): HandShape.SCISSORS
	}

	def __init__(self, data):
		super().__init__(data)
		data = data.strip("\n").split("\n")
		for entryStr in data:
			pre, _, post = entryStr.partition(" ")
			self.strategyGuide.append((pre, post))
		assert (len(self.strategyGuide) > 1)

	def part1(self) -> int:
		points = 0
		for colA, colB in self.strategyGuide:
			opponentShape = self.HandShape(ord(colA) - ord("A") + 1)
			yourShape = self.HandShape(ord(colB) - ord("X") + 1)

			roundResult = self.gameResultsLookup[(opponentShape, yourShape)]
			points += roundResult.value
			points += yourShape.value
		return points

	def part2(self):
		points = 0
		for colA, colB in self.strategyGuide:
			opponentShape = self.HandShape(ord(colA) - ord("A") + 1)
			roundResult = self.RoundResult((ord(colB) - ord("X")) * 3)

			yourShape = self.shapeLookup[(opponentShape, roundResult)]
			points += roundResult.value
			points += yourShape.value
		return points


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=2, year=2022))
	print(solution.part1())
	print(solution.part2())
