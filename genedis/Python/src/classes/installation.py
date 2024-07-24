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
        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT installations.id, installations.nom, installations.commune, installations.capacite, installations.anneeInstallation, proprietaires.nom  FROM installations INNER JOIN proprietaires ON installations.idProprietaire = proprietaires.id ORDER BY installations.commune, installations.capacite")
        listeInstallation = _dbSqlite.fetchall()
        _dbSqlite.close()
        return(listeInstallation)

    def listeParProprietaire(self, idProprietaire):
        
        listeInstallationParProprietaire = list()

        # Renvoyer la liste des installations d'un proprietaire en particulier
        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT *  FROM installations WHERE idProprietaire = ?", (idProprietaire,))
        listeInstallationParProprietaire = _dbSqlite.fetchall()
        _dbSqlite.close()

        return(listeInstallationParProprietaire)

    def creer(self,nom, commune, capacite, anneeInstallation, idProprietaire):
                
        try:
            _dbSqlite = self._bdSqlite.cursor()
            _dbSqlite.execute("INSERT INTO installations (nom, commune, capacite, anneeInstallation, idProprietaire) VALUES (?, ?, ?, ?, ?)", (nom, commune, capacite, anneeInstallation, idProprietaire))
            self._bdSqlite.commit()
            return {"message": "Success"}
        except Exception as e:
            return {'error': str(e) }
        finally:
            _dbSqlite.close()
            
    
    def installationCapaciteParProprietaire(self):
        sumCapacite = list()
        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT proprietaires.nom, SUM(installations.capacite) FROM installations INNER JOIN proprietaires ON installations.idProprietaire = proprietaires.id GROUP BY proprietaires.nom")
        sumCapacite = _dbSqlite.fetchall()
        _dbSqlite.close()
        return(sumCapacite)
    

    def InstallationParAnnee(self):
        countInstallationParAnnee = list()
        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT anneeInstallation, count(*) FROM installations GROUP BY anneeInstallation")
        results = _dbSqlite.fetchall()
        
        for result in results:
            anneeInstallation = result[0].replace("T.A. ", "") 
            count = result[1]
            countInstallationParAnnee.append((anneeInstallation, count))
        
        _dbSqlite.close()
        return(countInstallationParAnnee)
