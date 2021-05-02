import unittest
from task1 import solveSquare


class Test_task1(unittest.TestCase):

    def test_1_D_positive(self):
        self.assertEqual(solveSquare(5, -6, 1), (0.2, 1.0))
        self.assertEqual(solveSquare(4, 0, -100), (-5.0, 5.0))
        self.assertEqual(solveSquare(2, -30, 0), (0.0, 15.0))

    def test_2_D_zero(self):
        self.assertEqual(solveSquare(1, 2, 1), (-1.0, -1.0))
        self.assertEqual(solveSquare(1, 4, 4), (-2.0, -2.0))
        self.assertEqual(solveSquare(1, -2, 1), (1.0, 1.0))

    def test_3_D_negative(self):
        self.assertEqual(solveSquare(1, 1, 1), None)
        self.assertEqual(solveSquare(5, -3, 42), None)
        self.assertEqual(solveSquare(1, -4, 23), None)

    def test_4_fail(self):
        with self.assertRaises(TypeError):
            solveSquare(1, "asd")
