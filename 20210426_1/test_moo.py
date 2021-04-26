import unittest
from unittest.mock import MagicMock
from moo import Model


class TestMoo(unittest.TestCase):

    def setUp(self):
        self.view = MagicMock()
        self.view.E.get = MagicMock(return_value="QWERT")
        self.view.L = {}
        self.model = Model()
        #v = View(model=m)
        #self.model.setup(self.view)

    def test_A(self):
        self.model.setup(self.view)
        assert(self.model.view is self.view)

    def test_B(self):
        self.model.setup(self.view)
        self.model.copy()
        self.view.E.get.assert_called_once()    #гет дернулся
        self.assertEqual(self.view.L["text"], "QWERT")
