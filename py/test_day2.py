import unittest
import day2
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=2)

class Day2Test(unittest.TestCase):

  def setUp(self):
    self.example_list = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


  def test_part1_example_input(self):
    result = day2.solve_part1(self.example_list)
    self.assertEqual(2, result)


  def test_part1_input_data(self):
    print(day2.solve_part1(puzzle.input_data))

  
  def test_part2_example_input(self):
    result = day2.solve_part2(self.example_list)
    self.assertEqual(1, result)


  def test_part2_input_data(self):
    print(day2.solve_part2(puzzle.input_data))

if __name__ == '__main__':
    unittest.main()