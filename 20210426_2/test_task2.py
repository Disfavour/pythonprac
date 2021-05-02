import unittest
from unittest.mock import MagicMock
from task2 import *


class Test_task2(unittest.TestCase):

    def setUp(self):
        self.view = MagicMock()
        self.model = Model()

        self.view.model.analyze = MagicMock()
        self.view.answer.set = MagicMock()

    def test_A(self):
        self.model.setup(self.view)
        assert(self.model.view is self.view)

    def test_B(self):
        self.model.setup(self.view)

        self.view.get_answer()
        self.view.model.analyze(1, 2, 3)
        self.view.model.analyze.assert_called_once()
        self.view.answer.set("asd")
        self.view.answer.set.assert_called_once()

    def test_1_D_positive(self):
        self.model.setup(self.view)
        self.assertEqual(self.model.calculate(5, -6, 1), "0.2 1.0")
        self.assertEqual(self.model.calculate(4, 0, -100), "-5.0 5.0")
        self.assertEqual(self.model.calculate(2, -30, 0), "0.0 15.0")

    def test_2_D_zero(self):
        self.model.setup(self.view)

        self.assertEqual(self.model.calculate(1, 2, 1), "-1.0")
        self.assertEqual(self.model.calculate(1, 4, 4), "-2.0")
        self.assertEqual(self.model.calculate(1, -2, 1), "1.0")

    def test_3_D_negative(self):
        self.model.setup(self.view)

        self.assertEqual(self.model.calculate(1, 1, 1), "∅")
        self.assertEqual(self.model.calculate(5, -3, 42), "∅")
        self.assertEqual(self.model.calculate(1, -4, 23), "∅")

    def test_4_fail(self):
        with self.assertRaises(TypeError):
            self.model.calculate(1, "asd")
    
    def test_5_fullzero(self):
        self.model.setup(self.view)

        self.assertEqual(self.model.calculate(0, 0, 0), "∞")
