import unittest
from solve import solve

class TestEq(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(5, 2), -0.4)
        self.assertEqual(solve(9, -15.2), 1.6888888888888889)
        self.assertEqual(solve(-2, 5), 2.5)
        self.assertEqual(solve(-0.3, 12), 40)
        self.assertEqual(solve(4, 1), -0.25)

    def test_2(self):
        self.assertEqual(solve(0, 12), None)
        self.assertEqual(solve(0, 4), None)
        self.assertEqual(solve(0, 0), None)
