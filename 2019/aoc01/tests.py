import unittest
from code import solve_part_one, solve_part_two

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(solve_part_one([12]),     '2')
        self.assertEqual(solve_part_one([14]),     '2')
        self.assertEqual(solve_part_one([1969]),   '654')
        self.assertEqual(solve_part_one([100756]), '33583')

    def test_part_two(self):
        self.assertEqual(solve_part_two([14]),     '2')
        self.assertEqual(solve_part_two([1969]),   '966')
        self.assertEqual(solve_part_two([100756]), '50346')


if __name__ == '__main__':
    unittest.main()
