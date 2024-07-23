#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
import sqlite3

class Installation:

    def __init__(self):
        # Chemin de l'API
        pathApi = os.path.dirname(os.path.realpath(__file__))

        # Récupération config
        configApi = configparser.ConfigParser()
        configApi.read(pathApi + '/../../conf/config.ini')

        self._configApi = configApi

        self._bdSqlite = sqlite3.connect(pathApi + '/../../data/dbInstallations.db')

    def liste(self):
        listeInstallation = list()

        # Renvoyer la liste des installations et de leurs propriétaires triée par commune puis par capacité

        return(listeInstallation)

    def listeParProprietaire(self):
        listeInstallationParProprietaire = list()

        # Renvoyer la liste des installations d'un proprietaire en particulier

        return(listeInstallationParProprietaire)

    def creer(self):

        return(retour)