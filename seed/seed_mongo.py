"""Module used to fill a mongo database with defined data.
"""

from pymongo import MongoClient

class MongoSeeder:

    def __init__(self):
        host = 'mongodb'
        client = MongoClient(host=f'{host}')
        self.__db = client.registre

    @property
    def db(self):
        return self.__db

    def seed(self):
        """Seeds the database.
        """
        # Clearing collection
        self.db.vehicules.drop()

        # Insert valid and invalid data
        registre = []


        marque = "Durand"
        modele = "Nathalie"
        prix = "269054958815780"
        couleur ="grise"
        immatruculation = "aa"
        vehicule = {"marque": marque, "modele": modele, "prix":prix, "couleur":couleur, "immatruculation": immatruculation}
        registre.append(vehicule)


        self.db.vehicules.insert(registre)
        cursor = self.db.vehicules.find()
        for v in cursor:
            print(v)

print("Filling DB")
MongoSeeder().seed()

client = MongoClient(host="mongodb")
db = client.registre
print("Done")
