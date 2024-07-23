#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response
import configparser
import os
import json

from __main__ import app

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
configApi = configparser.ConfigParser()
configApi.read(pathApi + '/../../conf/config.ini')

@app.route('/version', methods=['GET', 'DELETE'])
def versionGet(*args, **kwargs):
    version = configApi['Misc']['Version']

    response = make_response(json.dumps({'version':version}), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response