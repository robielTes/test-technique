#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import jsonify, make_response, request
import configparser
import os
import time
import json

from __main__ import app

from classes.installation import Installation
from classes.proprietaire import Proprietaire

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
configApi = configparser.ConfigParser()
configApi.read(pathApi + '/../../conf/config.ini')

@app.route('/installations', methods=['GET'])
def installationsGet(*args, **kwargs):

    installations = Installation()
    listeInstallations = installations.liste()

    response = make_response(json.dumps(listeInstallations), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

# Récupération des installations par propriétaire
@app.route('/installations/<int:parProprietaire>', methods=['GET'])
def installationsParProprietaireGet(parProprietaire):

    # Récupérer l'argument "proprietaire" sous forme d'id et renvoyer les installations correspondantes    
    Installations = Installation()
    listeInstallationsParProprietaire = Installations.listeParProprietaire(parProprietaire)

    response = make_response(json.dumps(listeInstallationsParProprietaire), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

# Création d'une nouvelle installation
@app.route('/installations/', methods=['POST'])
def installationsPost():
    nom = request.form['nom']
    commune = request.form['commune']
    capacite = request.form['capacite']
    anneeInstallation = request.form['anneeInstallation']
    idProprietaire = request.form['idProprietaire']
    

    # Récupérer les arguments nécessaires à la création d'une nouvelle installation
    # Le propriétaire doit déjà exister
    
    proprietaires = Proprietaire()
    proprietairesExist = proprietaires.exist(idProprietaire)
    
    if(not proprietairesExist):
        response = make_response(json.dumps({"error": "Le propriétaire n'existe pas"}), 400)
        response.headers["Content-Type"] = "text/json; charset=utf-8"
        return response
    
    Installations = Installation()
    installationsPost = Installations.creer(nom, commune, capacite, anneeInstallation, idProprietaire)
    response = make_response(json.dumps(installationsPost), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

# Récupération des capacité des installations par propriétaire
@app.route('/installations/capacite', methods=['GET'])
def installationsCapaciteParProprietaireGet():
    installations = Installation()
    sumCapacite = installations.installationCapaciteParProprietaire()

    response = make_response(json.dumps(sumCapacite), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

# Récupération des installations par année d'installation
@app.route('/installations/anneeInstallation', methods=['GET'])
def installationsAnneeInstallationGet():
    installations = Installation()
    anneeInstallation = installations.InstallationParAnnee()

    response = make_response(json.dumps(anneeInstallation), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response