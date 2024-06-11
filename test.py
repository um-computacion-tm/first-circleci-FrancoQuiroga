import unittest
from main import suma

class Testsuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2,1), 3)