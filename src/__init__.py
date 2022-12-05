import importlib

def plugin(year, day, data):
	modName = f"src.Day{day:02d}.main"
	mod = importlib.import_module(modName)
	solution = mod.Solution(data)
	part1 = solution.part1()
	part2 = solution.part2()
	return part1, part2
