import unittest
from task1 import solveSquare


class TestTdfun(unittest.TestCase):
    def test_D_positive(self):
        self.assertEqual(solveSquare(5, -6, 1), (0.2, 1.0))

    def test_D_zero(self):
        self.assertEqual(solveSquare(1, 2, 1), (-1.0, -1.0))

    def test_D_negative(self):
        self.assertEqual(solveSquare(1, 1, 1), None)

    def test_2_fun(self):
        with self.assertRaises(TypeError):
            solveSquare(1, "asd")

