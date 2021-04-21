import unittest
from src.main import soma


class TestSoma(unittest.TestCase):
    def test_retorno_soma(self):
        self.assertEqual(soma(10, 10), 20)

    def test_retorno_soma_com_erro(self):
        self.assertNotEqual(soma(10, 10), 21)
