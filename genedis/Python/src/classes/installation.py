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

    # Récupération les listes des installations et de leurs propriétaires triée par commune puis par capacité
    def liste(self):
        listeInstallation = list()

        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT installations.id, installations.nom, installations.commune, installations.capacite, installations.anneeInstallation, proprietaires.nom  FROM installations INNER JOIN proprietaires ON installations.idProprietaire = proprietaires.id ORDER BY installations.commune, installations.capacite")
        listeInstallation = _dbSqlite.fetchall()
        _dbSqlite.close()
        return(listeInstallation)

    # Récupération les listes des installations d'un propriétaire en particulier
    def listeParProprietaire(self, idProprietaire):
        
        listeInstallationParProprietaire = list()

        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT *  FROM installations WHERE idProprietaire = ?", (idProprietaire,))
        listeInstallationParProprietaire = _dbSqlite.fetchall()
        _dbSqlite.close()

        return(listeInstallationParProprietaire)

    # Création d'une nouvelle installation par son nom, sa commune, sa capacité, son année d'installation et l'id de son propriétaire
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
            
    # Récupération les capacités des installations triée par propriétaire
    def installationCapaciteParProprietaire(self):
        sumCapacite = list()
        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT proprietaires.nom, SUM(installations.capacite) FROM installations INNER JOIN proprietaires ON installations.idProprietaire = proprietaires.id GROUP BY proprietaires.nom")
        sumCapacite = _dbSqlite.fetchall()
        _dbSqlite.close()
        return(sumCapacite)
    
    # Récupération les installations par année d'installation
    def InstallationParAnnee(self):
        countInstallationParAnnee = list()
        _dbSqlite = self._bdSqlite.cursor()
        _dbSqlite.execute("SELECT anneeInstallation, count(*) FROM installations GROUP BY anneeInstallation")
        results = _dbSqlite.fetchall()
        
        # formatage des résultats
        for result in results:
            anneeInstallation = result[0].replace("T.A. ", "") 
            count = result[1]
            countInstallationParAnnee.append((anneeInstallation, count))
        
        _dbSqlite.close()
        return(countInstallationParAnnee)
