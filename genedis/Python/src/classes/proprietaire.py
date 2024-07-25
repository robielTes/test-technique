#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
import sqlite3

class Proprietaire:

    def __init__(self):
        # Chemin de l'API
        pathApi = os.path.dirname(os.path.realpath(__file__))

        # Récupération config
        configApi = configparser.ConfigParser()
        configApi.read(pathApi + '/../../conf/config.ini')

        self._configApi = configApi

        self._bdSqlite = sqlite3.connect(pathApi + '/../../data/dbInstallations.db')

    # Récupération les listes des propriétaires
    def liste(self):
        listeInstallation = list()

        # Renvoyer la liste des proprietaires
        dbSqlite = self._bdSqlite.cursor()
        dbSqlite.execute("SELECT * FROM proprietaires") # Récupérer les propriétaires
        listeInstallation = dbSqlite.fetchall()
        dbSqlite.close()
        
        return(listeInstallation)

    # Création d'un nouveau propriétaire par son nom
    def creer(self,nom):
        
        try:
            _dbSqlite = self._bdSqlite.cursor()
            _dbSqlite.execute("INSERT INTO proprietaires (nom) VALUES (?)", (nom,))
            self._bdSqlite.commit()
            return {"message": "Success"}
        except Exception as e:
            return {'error': str(e) }
        finally:
            _dbSqlite.close()
            
    # Vérifier si le propriétaire existe déjà par son id ou son nom
    def exist(self, n):
        try:
            _dbSqlite = self._bdSqlite.cursor()
            _dbSqlite.execute("SELECT * FROM proprietaires WHERE id = ? OR nom = ?", (n, n))
            proprietaire = _dbSqlite.fetchall()
            if proprietaire:
                return True
            else:
                return False
        except Exception as e:
            return {'error': str(e) }
        finally:
            _dbSqlite.close()