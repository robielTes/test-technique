==============================================================================
                           TEST TECHNIQUE PRÉALABLE
                                 Genedis
==============================================================================

Bonjour,

Vous trouverez sur cette plateforme deux ébauches de projets destinés à évaluer
en quelques lignes vos aptitudes pour le poste de développeur PHP / Python.

Le test n'a pas pour vocation à être exhaustif sur vos connaissances, mais à
évaluer vos capacités, votre façon de faire et les réflexions que vous
pourriez apporter sur ce type de projet.

L'ensemble des développements demandés ne devrait pas vous prendre plus d'une
demi journée (plus que de finir le projet lui-même, nous sommes intéressés
à voir comment vous traitez chacune des problématiques), et lors de
l'évaluation de multiples critères seront pris en compte : traitement de la
demande, lisibilité et esthétique du code, ajouts personnels et optimisations,
esthétique du rendu final, ...

N'hésitez pas à nous contacter en cas d'incompréhension dans l'énoncé.

------------------------------------------------------------------------------
                                   Contexte
------------------------------------------------------------------------------

Un collaborateur a démarré un nouveau projet de visualisation du nombre
d'installations photovoltaïque. Rapidement appelé à d'autres tâches, ce
dernier n'a pas pu terminer le projet et l'a laissé en l'état, incomplet et
avec plusieurs erreurs.
Votre tâche est de corriger l'existant et de compléter les fonctions
existantes.

Une base de données SQLite déjà garnie est fournie. Elle est composée des
tables suivantes :
 - installations
  - id (int)
  - nom (varchar 32)
  - commune (text)
  - capacite (float)
  - anneeInstallation (text)
  - idProprietaire (int)
 - proprietaires
  - id (int)
  - nom (varchar 32)
Il est inutile de modifier la structure de cette base de données.


------------------------------------------------------------------------------
                                  Consigne
------------------------------------------------------------------------------

L'API REST en Python doit être complétée (les fonctions attendues sont déjà
créées), et l'interface de visualisation doit afficher sous forme textuelle
et graphique les données de la base SQLite via l'API exclusivement.
Une ébauche du dashboard de visualisation est fournie avec quelques images
en guise de démonstration. Elle mérite d'être complétée et largement améliorée
graphiquement.

La plateforme mise à disposition vous est dédiée. Vous êtes libres d'ajouter
les extensions VS Code de votre choix et de personnaliser le système, y
compris

  pip install --break-system-packages <module>
  pip install --break-system-packages -r requirements.txt

  sudo apt update
  sudo apt install php8.3-<extension>

à votre convenance.

Pour ouvrir un terminal et exécuter des commandes (celles-ci ou celles pour
exécuter des serveurs de développement), dans le menu en haut de page,
cliquez sur Terminal > New terminal.


------------------------------------------------------------------------------
                 Détails concernant la partie PHP/HTML/Javascript
------------------------------------------------------------------------------

Un serveur de développement PHP peut être lancé via la commande suivante :

  cd PHP
  php -S 127.0.0.1:8082

Le site web devient alors accessible à l'adresse

  https://<url>/<identifiant>/proxy/8082/

Votre code devra être compatible PHP 8. L'utilisation d'un framework PHP est
facultative. Si vous souhaitez en utiliser un, seul Laravel pourra l'être.
Le choix de la librairie graphique pour les graphes est libre. Elle doit
cependant être open-source.
Afin d'être cohérent avec les autres projets que nous développons, la
librairie JS à utiliser est jQuery. Bootstrap peut également être utilisé.
Les autres frameworks comme React, AngluarJS, Vue.js ne peuvent
pas être utilisés pour ce test.


------------------------------------------------------------------------------
                     Détails concernant la partie Python
------------------------------------------------------------------------------

Un serveur de développement Python/Flask peut être lancé via la commande
suivante :

  cd Python/src
  python3 server.py

L'API devient alors accessible à l'adresse

  https://<url>/<identifiant>/proxy/8081/
  https://<url>/<identifiant>/proxy/8081/version

Votre code devra être compatible Python 3 et la structure d'origine devrait
être conservée. Si ce n'est pas le cas, attendez-vous à devoir le justifier :)

La base SQLite se trouve à l'emplacement data/dbInstallations.db


------------------------------------------------------------------------------
                                   Rendu
------------------------------------------------------------------------------

Dans un document séparé que vous inclurez dans le projet, veuillez préciser
quels changements ou quelles améliorations vous proposeriez afin de mieux
suivre les standards de développement PHP et Python (et donc sans les
implémenter).

L'ensemble des développements doit rester sur la plateforme VSCode Online
mise à disposition.

N'hésitez pas à nous faire part de vos commentaires et de tout ce que vous
jugeriez utile de préciser.

Bonne chance !
