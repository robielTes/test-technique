#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
from flask import Flask, request, render_template

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
configApi = configparser.ConfigParser()
configApi.read(pathApi + '/../conf/config.ini')

# Création API
app = Flask(__name__)

import routes.version
import routes.installations
import routes.proprietaires


# Exécution et lancement du serveur
if __name__ == '__main__':
    app.run(debug=True,
            host=configApi['Network']['Host'],
            port=configApi['Network']['Port'])
