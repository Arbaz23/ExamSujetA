
class Vehicule:
    def __init__(self, marque, modele, prix, couleur, immatriculation):
        self.marque=marque
        self.modele=modele
        self.prix=prix
        self.couleur=couleur
        self.immatriculation=immatriculation

    def marqueValide(self):
        if self.marque=="FakeBrand":
            return False
        return True
        