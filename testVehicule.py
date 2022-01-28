import unittest
from Vehicule import Vehicule


class TestPersonne(unittest.TestCase):
    def test_personne_valid_ssn(self):
        vehicule = Vehicule("Audi", "A4", "24", "grise", "NE-212-BA 91")
        self.assertEqual(vehicule.vehiculevalid(), True)
