#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response, request
import configparser
import os
import time
import json

from __main__ import app

from classes.proprietaire import Proprietaire

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
configApi = configparser.ConfigParser()
configApi.read(pathApi + '/../../conf/config.ini')

# Récupération les listes des propriétaires
@app.route('/proprietaires', methods=['GET'])
def proprietairesGet(*args, **kwargs):

    proprietaires = Proprietaire()
    listeProprietaires = proprietaires.liste()

    response = make_response(json.dumps(listeProprietaires), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

# Création d'un nouveau propriétaire
@app.route('/proprietaires', methods=['POST'])
def proprietairesPost():
    nom = request.form['nom']

    # Récupérer les arguments nécessaires à la création d'une nouvelle propriétaire
    # Verifier si le propriétaire est déjà exister
    
    proprietaires = Proprietaire()
    
    proprietairesExist = proprietaires.exist(nom)
    if(proprietairesExist):
        response = make_response(json.dumps({"error": "Le propriétaire existe déjà"}), 400)
        response.headers["Content-Type"] = "text/json; charset=utf-8"
        return response
    
    proprietairesPost = proprietaires.creer(nom)
    response = make_response(json.dumps(proprietairesPost), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response