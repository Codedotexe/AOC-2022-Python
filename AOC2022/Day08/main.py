from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd
import numpy as np


class Solution(PuzzleSolution):
	map = None

	class Tree:
		def __init__(self, x: int, y: int, height: int):
			self.x = x
			self.y = y
			self.height = height
			self.visible = False
			self.scentic_score = None

	def __init__(self, data: str) -> None:
		super().__init__(data)
		array = list(map(list, data.rstrip("\n").split("\n")))
		self.map = np.empty(shape=(len(array[0]), len(array)), dtype=self.Tree)
		for x in range(self.map.shape[0]):
			for y in range(self.map.shape[1]):
				self.map[x, y] = self.Tree(x, y, int(array[y][x]))

	def mark_edges(self):
		for tree in self.map[0, :]:
			tree.visible = True
		for tree in self.map[-1, :]:
			tree.visible = True
		for tree in self.map[:, 0]:
			tree.visible = True
		for tree in self.map[:, -1]:
			tree.visible = True

	def visible_trees_count(self):
		visible_trees = 0
		for x in range(self.map.shape[0]):
			for y in range(self.map.shape[1]):
				if self.map[x, y].visible:
					visible_trees += 1
		return visible_trees

	def print_visibility(self):
		print(np.array2string(np.flip(np.rot90(self.map, k=-1), 1),
							  formatter={"all": lambda t: "Y" if t.visible else "N"}))

	def print_height(self):
		print(np.array2string(np.flip(np.rot90(self.map, k=-1), 1), formatter={"all": lambda t: str(t.height)}))

	@staticmethod
	def max_increasing_length(iterable, height):
		for i in range(len(iterable)):
			if height <= iterable[i].height:
				return i + 1
		return len(iterable)

	def check_visibility(self, tree: Tree):
		visible_from_top = next(filter(lambda x: x.height >= tree.height, self.map[tree.x, :tree.y]), None) is None
		visible_from_bottom = next(filter(lambda x: x.height >= tree.height, self.map[tree.x, tree.y + 1:]),
								   None) is None
		visible_from_left = next(filter(lambda x: x.height >= tree.height, self.map[:tree.x, tree.y]), None) is None
		visible_from_right = next(filter(lambda x: x.height >= tree.height, self.map[tree.x + 1:, tree.y]),
								  None) is None
		return visible_from_top or visible_from_bottom or visible_from_left or visible_from_right

	def calc_scentic_score(self, tree: Tree):
		top_score = self.max_increasing_length(self.map[tree.x, :tree.y][::-1], tree.height)
		bottom_score = self.max_increasing_length(self.map[tree.x, tree.y + 1:], tree.height)
		left_score = self.max_increasing_length(self.map[:tree.x, tree.y][::-1], tree.height)
		right_score = self.max_increasing_length(self.map[tree.x + 1:, tree.y], tree.height)
		return top_score * bottom_score * left_score * right_score

	def part1(self) -> int:
		for x in range(self.map.shape[0]):
			for y in range(self.map.shape[1]):
				self.map[x, y].visible = self.check_visibility(self.map[x, y])

		# self.print_visibility()
		# print("")
		# self.print_height()
		return self.visible_trees_count()

	def part2(self) -> int:
		for x in range(self.map.shape[0]):
			for y in range(self.map.shape[1]):
				self.map[x, y].scentic_score = self.calc_scentic_score(self.map[x, y])

		return max(map(lambda t: t.scentic_score, self.map.flat))


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=8, year=2022))
	print(solution.part1())
	print(solution.part2())
