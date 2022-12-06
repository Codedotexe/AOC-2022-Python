import argparse
import importlib
import logging
import aocd
from argparse import ArgumentParser
from datetime import datetime


class CliParser:
	def __init__(self):
		parser = self.create_parser()
		self.args = parser.parse_args()

		if self.args.log_level:
			level_int = getattr(logging, self.args.log_level)
			logging.basicConfig(format="%(message)s", level=level_int)

		if self.args.data is not None and self.args.day == "all":
			raise argparse.ArgumentError(None, "The data argument is only valid if a single day is to be run")

		if self.args.day == "all":
			for i in range(1, 26):
				try:
					self.run_solution(i)
				except ModuleNotFoundError:
					break
		else:
			data = None
			if self.args.data is not None:
				with open(self.args.data, "r") as file:
					data = file.read()

			try:
				self.run_solution(int(self.args.day), data)
			except ModuleNotFoundError:
				print(f"The solution for day {self.args.day} is not yet implemented.")

	@staticmethod
	def create_parser():
		parser = ArgumentParser(description=__doc__)
		aoc_now = datetime.now(tz=aocd.utils.AOC_TZ)
		dayChoices = list(map(str, range(1, 26))) + ["all"]

		parser.add_argument("day", nargs="?", type=str, choices=dayChoices,
							default=str(min(aoc_now.day, 25)) if aoc_now.month == 12 else "1",
							help="1-25 or all (default: %(default)s)")
		parser.add_argument("-d", "--data")
		log_levels = "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
		parser.add_argument("--log-level", choices=log_levels)
		return parser

	@staticmethod
	def run_solution(day, data=None):
		modName = f"{__package__}.Day{day:02d}.main"
		mod = importlib.import_module(modName)
		if data is None:
			data = aocd.get_data(day=day, year=2022)
		solution = mod.Solution(data)
		print(f"Day-{day:02d} Part 1:", solution.part1())
		print(f"Day-{day:02d} Part 2:", solution.part2())
