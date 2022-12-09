from AOC2022.utils.PuzzleSolution import PuzzleSolution
from .Vec2d import Vec2d
import aocd


class Solution(PuzzleSolution):
	def __init__(self, data: str) -> None:
		super().__init__(data)
		self.instructions = []
		self.visited_positions = set()
		self.head = Vec2d(0, 0)
		self.tail = Vec2d(0, 0)

		for line in data.rstrip("\n").splitlines():
			direction, _, amount_str = line.partition(" ")
			amount = int(amount_str)
			if direction == "L":
				self.instructions.append(Vec2d(-amount, 0))
			elif direction == "R":
				self.instructions.append(Vec2d(amount, 0))
			elif direction == "U":
				self.instructions.append(Vec2d(0, -amount))
			elif direction == "D":
				self.instructions.append(Vec2d(0, amount))
			else:
				raise RuntimeError()

	def simulate_rope(self):
		distance_vec = self.head.subtract(self.tail, inplace=False)
		if distance_vec.x == 0 and distance_vec.y == 0:
			pass
		elif (distance_vec.x == 0 and distance_vec.y != 0) or (distance_vec.x != 0 and distance_vec == 0):
			self.tail.add(distance_vec.divide(distance_vec, inplace=False))
		else:
			diagonal_vectors = (Vec2d(-1, -1), Vec2d(-1, 1), Vec2d(-1, 1), Vec2d(1, 1))
			best_choice = min(diagonal_vectors, key=lambda v: len(self.tail.subtract(v, inplace=False)))
			self.tail.add(best_choice)


	def part1(self) -> int:
		for instruction in self.instructions:
			self.head.add(instruction)
			self.simulate_rope()
			self.visited_positions.add((self.tail.x, self.tail.y))

		return len(self.visited_positions)


	def part2(self) -> int:
		pass


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=9, year=2022))
	print(solution.part1())
	print(solution.part2())
