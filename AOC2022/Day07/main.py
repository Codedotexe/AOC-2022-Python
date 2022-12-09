from AOC2022.utils.PuzzleSolution import PuzzleSolution
import aocd


class File:
	_size = None
	name = None

	def __init__(self, size, name: str):
		self._size = size
		self.name = name

	def size(self):
		return self._size

	def __str__(self):
		return f"{self.__hash__()} {self.name}"


class Directory(File):
	children = None  # Do not create the set object here, because it will we shared by ALL Directory instances
	parent = None

	def __init__(self, name: str, parent):
		super().__init__(None, name)
		self.children = set()
		self.parent = parent

	def size(self):
		self._size = 0
		for child in self.children:
			self._size += child.size()
		return self._size

	def find_child(self, name):
		return next(filter(lambda x: name == x.name, self.children), None)


class FileSystem:
	root_dir = None
	cwd_dir = None

	def __init__(self, root_dir):
		self.root_dir = root_dir
		self.cwd_dir = self.root_dir

	def _navigate(self, startDir, path):
		cwd = startDir
		path_parts = path.split("/")
		assert (len(path_parts) > 0)

		if path_parts[0] == "":
			cwd = self.root_dir

		for name in path_parts:
			if name == "." or name == "":
				pass
			elif name == "..":
				assert (cwd.parent is not None)
				cwd = cwd.parent
			else:
				specified_dir = cwd.find_child(name)
				assert (specified_dir is not None and isinstance(specified_dir, Directory))
				cwd = specified_dir

		return cwd

	def cd(self, path):
		self.cwd_dir = self._navigate(self.cwd_dir, path)

	def create_file(self, size, name):
		assert self.cwd_dir.find_child(name) is None, "A child with that name already exists"
		self.cwd_dir.children.add(File(size, name))

	def create_dir(self, name):
		assert self.cwd_dir.find_child(name) is None, "A child with that name already exists"
		self.cwd_dir.children.add(Directory(name, self.cwd_dir))

	def iterate_dirs(self):
		stack = [self.root_dir]
		while len(stack) > 0:
			current = stack.pop()
			yield current
			for child in current.children:
				if isinstance(child, Directory):
					stack.append(child)

	def iterate_files(self):
		stack = [self.root_dir]
		while len(stack) > 0:
			current = stack.pop()
			for child in current.children:
				if isinstance(child, Directory):
					stack.append(child)
				elif isinstance(child, File):
					yield child


class Solution(PuzzleSolution):
	file_system = None

	def __init__(self, data: str) -> None:
		super().__init__(data)

		self.file_system = FileSystem(Directory("/", None))
		for line in data.rstrip("\n").split("\n"):
			if line.startswith("$ cd"):
				self.file_system.cd(line.replace("$ cd ", ""))
			elif line.startswith("$ ls"):
				pass
			else:  # all lines that do not start with "$" are ls entries
				size, _, name = line.partition(" ")
				if size == "dir":
					self.file_system.create_dir(name)
				else:
					self.file_system.create_file(int(size), name)

	def part1(self) -> int:
		MAX_SIZE = 100000
		dirs_with_max_size = filter(lambda x: x.size() <= MAX_SIZE, self.file_system.iterate_dirs())
		return sum(map(lambda x: x.size(), dirs_with_max_size))

	def part2(self) -> int:
		TOTAL_SIZE = 70000000
		FREE_SPACE = TOTAL_SIZE - self.file_system.root_dir.size()
		UPDATE_SIZE = 30000000
		SIZE_TO_FREE = UPDATE_SIZE - FREE_SPACE
		assert SIZE_TO_FREE > 0, "There is already enough free space"

		dirs = list(self.file_system.iterate_dirs())
		dirs.sort(key=lambda x: x.size())
		dir_to_delete = next(filter(lambda x: x.size() >= SIZE_TO_FREE, dirs), None)
		assert dir_to_delete is not None, "Could not find a directory to delete"

		return dir_to_delete.size()


if __name__ == "__main__":
	solution = Solution(aocd.get_data(day=7, year=2022))
	print(solution.part1())
	print(solution.part2())
