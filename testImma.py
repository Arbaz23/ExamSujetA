import unittest
from Immatriculation import Immatriculation


class TestSSN(unittest.TestCase):
    def test_imma_is_valid(self):
        imma = Immatriculation("NE-212-BA 91")
        self.assertEqual(imma.is_valid(), True)

    def test_imma_to_long(self):
        imma = Immatriculation("NE-212-BA 9111")
        self.assertEqual(imma.is_valid(), False)

    def test_imma_not_correct(self):
        imma= Immatriculation("NE-AA-BA 91")
        self.assertEqual(imma.is_valid(), False)

    def test_imma_not_correct(self):
        imma= Immatriculation("11-212-BA 91")
        self.assertEqual(imma.is_valid(), False)
