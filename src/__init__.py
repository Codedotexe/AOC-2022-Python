import importlib

def plugin(year, day, data):
	modName = f"src.Day-{day}"
	mod = importlib.import_module(modName)

	part1 = None
	part2 = None
	try:
		part1 = mod.part1(data)
		part2 = mod.part2(data)
	except AttributeError:
		pass

	return part1, part2
