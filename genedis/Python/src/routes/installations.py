#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response
import configparser
import os
import time
import json

from __main__ import app

from classes.installation import Installation

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

@app.route('/installations/parProprietaire', methods=['GET'])
def installationsParProprietaireGet(*args, **kwargs):

    # Récupérer l'argument "proprietaire" sous forme d'id et renvoyer les installations correspondantes

    response = make_response(json.dumps(listeInstallationsParProprietaire), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

@app.route('/installations', methods=['POST'])
def installationsPost(*args, **kwargs):

    # Récupérer les arguments nécessaires à la création d'une nouvelle installation
    # Le propriétaire doit déjà exister

    return response