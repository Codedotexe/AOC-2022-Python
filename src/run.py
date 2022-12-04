import importlib
import aocd

def _run(dayNumber):
	modName = f"src.Day{dayNumber:02d}.main"
	mod = importlib.import_module(modName)
	data = aocd.get_data(day=dayNumber, year=2022)
	solution = mod.Solution(data)
	try:
		print(f"Day-{dayNumber:02d} Part 1:", solution.part1())
		print(f"Day-{dayNumber:02d} Part 2:", solution.part2())
	except:
		pass

def runAll():
	for i in range(24):
		try:
			_run(i+1)
		except ModuleNotFoundError:
			continue

if __name__ == "__main__":
	runAll()