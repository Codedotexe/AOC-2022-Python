import importlib
from .CliParser import CliParser


def cli():
	CliParser()


# noinspection PyUnusedLocal
def plugin(year, day, data):
	if year != 2022:
		raise RuntimeError("Only the year 2022 is supported")

	modName = f"{__package__}.Day{day:02d}.main"
	mod = importlib.import_module(modName)
	solution = mod.Solution(data)
	part1 = solution.part1()
	part2 = solution.part2()
	return part1, part2
