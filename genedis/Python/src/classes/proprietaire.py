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

    def liste(self):
        listeInstallation = list()

        # Renvoyer la liste des proprietaires
        dbSqlite = self._bdSqlite.cursor()
        dbSqlite.execute("SELECT * FROM proprietaires")
        listeInstallation = dbSqlite.fetchall()
        dbSqlite.close()
        
        return(listeInstallation)

    def creer(self,nom):
        print(nom)

        try:
            _dbSqlite = self._bdSqlite.cursor()
            _dbSqlite.execute("INSERT INTO proprietaires (nom) VALUES (?)", (nom,))
            self._bdSqlite.commit()
            return {"message": "Success"}
        except Exception as e:
            return {'error': str(e) }
        finally:
            _dbSqlite.close()
            
# function that true if the proprietaire exist by verifying either the id or the name
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