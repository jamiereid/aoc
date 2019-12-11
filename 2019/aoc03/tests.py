import unittest
from code import solve_part_one, solve_part_two

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(solve_part_one('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'), '159')
        self.assertEqual(solve_part_one('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), '135')

    def test_part_two(self):
        self.assertEqual(solve_part_two([]), '0')


if __name__ == '__main__':
    unittest.main()
