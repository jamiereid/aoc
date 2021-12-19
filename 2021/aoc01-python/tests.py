import unittest
from code import solve_part_one, solve_part_two

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(solve_part_one([199,200,208,210,200,207,240,269,260,263]), '7')

    def test_part_two(self):
        self.assertEqual(solve_part_two([199,200,208,210,200,207,240,269,260,263]), '5')


if __name__ == '__main__':
    unittest.main()
