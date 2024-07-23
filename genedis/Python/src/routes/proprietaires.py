#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response
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

@app.route('/proprietaires', methods=['GET'])
def proprietairesGet(*args, **kwargs):

    proprietaires = Proprietaire()
    listeProprietaires = proprietaires.liste()

    response = make_response(json.dumps(listeProprietaires), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

@app.route('/proprietaires', methods=['POST'])
def proprietairesPost(*args, **kwargs):

    # Récupérer les arguments nécessaires à la création d'une nouvelle installation
    # Le propriétaire doit déjà exister

    return response