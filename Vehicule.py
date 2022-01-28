From Immatriculation import Immatriculation

class Vehicule:
    def __init__(self, marque, modele, prix, couleur, immatriculation):
        self.marque=marque
        self.modele=modele
        self.prix=prix
        self.couleur=couleur
        self.immatriculation=Immatriculation(immatriculation)

    def marqueValide(self):
        if self.marque=="FakeBrand":
            return False
        return True

    def couleurValide(self):
        if self.couleur=="blanche":
            return True
        if self.couleur=="grise":
            return True
        if self.couleur=="noire":
            return True
        return False

    def immaValide(self):
        return self.immatriculation.is_valid()
        