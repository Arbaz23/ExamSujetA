import re
from pydantic import BaseModel, validator

class Modelvehicule(BaseModel):
    marque: str
    modele: str
    prix: str
    couleur:str
    immatriculation:str
