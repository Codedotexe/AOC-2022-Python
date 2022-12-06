import unittest
from .main import Solution

class TestDay06(unittest.TestCase):
	def testPart1(self):
		testData = {
			"mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
			"bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
			"nppdvjthqldpwncqszvftbrmjlhg": 6,
			"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
			"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11
		}

		for data, result in testData.items():
			self.assertEqual(result, Solution(data).part1())

	def testPart2(self):
		testData = {
			"mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
			"bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
			"nppdvjthqldpwncqszvftbrmjlhg": 23,
			"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
			"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26
		}

		for data, result in testData.items():
			self.assertEqual(result, Solution(data).part2())


if __name__ == '__main__':
	unittest.main()
