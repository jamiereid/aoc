import unittest
from code import solve_part_one, solve_part_two

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(solve_part_one([1,9,10,3,2,3,11,0,99,30,40,50]), [3500,9,10,70,2,3,11,0,99,30,40,50])
        self.assertEqual(solve_part_one([1,0,0,0,99]), [2,0,0,0,99])
        self.assertEqual(solve_part_one([2,3,0,3,99]), [2,3,0,6,99])
        self.assertEqual(solve_part_one([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(solve_part_one([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])
    def test_part_two(self):
        self.assertEqual(solve_part_two([]), [])


if __name__ == '__main__':
    unittest.main()
