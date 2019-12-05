import unittest
from code import solve_part_one, solve_part_two

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(solve_part_one([]), '')

    def test_part_two(self):
        self.assertEqual(solve_part_two([]), '')


if __name__ == '__main__':
    unittest.main()
