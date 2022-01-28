from fastapi import FastAPI, HTTPException
from model_vehicule import vehicule
from db import database

app = FastAPI()

@app.get("/vehicules")
def fetch_vehicule():
    db = database()
    results = db.vehicules.find()
    v1 = []
    for result in results:
        p = {"marque": result["marque"], "modele": result["modele"],
             "prix": result["prix"],"couleur": result["couleur"], 
             "immatriculation": result["immatriculation"], }
        v1.append(p)
    return v1

@app.post("/vehicules/")
def create_vehicule(vehicule: vehicule):
    db = database()
    if db.vehicules.find_one({"immatriculation":vehicule.immatriculatin}) is not None:
        HTTPException(status=404, detail="imma is already registered")
    result = db.personnes.insert_one(vehicule.dict())
    return vehicule.dict()

@app.get("/vehicules/{immatriculation}")
def fetch_veh_by_imma(immatriculation: str):
    db = database()
    result = db.personnes.find_one({"immatriculation":immatriculation})
    p = {"marque": result["marque"], "modele": result["modele"],
             "prix": result["prix"],"couleur": result["couleur"], 
             "immatriculation": result["immatriculation"], }
    return p


@app.delete("/vehicules/{immatriculation}")
def delete_veh_by_imma(immatriculation: str):
    db = database()
    db.vehicules.delete_one({"immatriculation":immatriculation})

@app.put("/immatriculation/{immatriculation}")
def update_veh_by_imma(immatriculation: str, vehiculee: vehicule):
    db = database()
    result = db.vehicules.update_one({"immatriculation":immatriculation}, {"$set": vehiculee.dict()})
    return vehiculee.dict()
