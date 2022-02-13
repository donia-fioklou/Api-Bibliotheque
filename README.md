# Api-Bibliotheque
## Motivations
Cette API permet de gérer les tables livres et categories créées dans la base de données.
## Commencer

### Installation des dépendances

#### Python 3.9.7
#### pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)
Si vous n'avez pas python installé, merci de suivre cet URL pour l'installer 
[python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
#### Virtual Enviornment

Vous devez installer le package dotenv en utilisant la commande pip install python-dotenv 

#### Dépendances PIP

Exécuter la commande ci dessous pour installer les dépendences
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```
ceci va installer tout les dependances du fichier requirment.txt
##### Dépendances clés

- [Flask](http://flask.pocoo.org/) est un framework de microservices backend léger.
-  Flask est nécessaire pour traiter les demandes et les réponses.
- [SQLAlchemy](https://www.sqlalchemy.org/) est la boîte à outils Python SQL et ORM que nous utiliserons pour gérer la base de données postgres. Vous travaillerez principalement dans App.py
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#)  est l’extension que nous utiliserons pour gérer les demandes d’origine croisée de notre serveur frontal.
##Exécution du serveur
À partir du répertoire 'MiniProjet', assurez-vous d’abord que vous travaillez à l’aide de votre environnement virtuel créé.
Pour exécuter le serveur sous Linux ou Mac, exécutez :
```bash
export FLASK_APP=App.py
export FLASK_ENV=development
flask run
```
Pour exécuter le serveur sous Windows, exécutez :
```bash
set FLASK_APP=App.py
set FLASK_ENV=development
flask run
```
Définir la variable 'FLASK_ENV' sur 'developpement' détectera les modifications de fichiers et redémarrera automatiquement le serveur.
définir la variable 'FLASK_APP' sur App.py
## RÉFÉRENCE API
Commencer

URL de base : à l'heure actuelle, cette application ne peut être exécutée que localement et n'est pas hébergée en tant qu'URL de base. L'application principale est hébergée par défaut, http://localhost:5000 ; qui est défini comme proxy dans la configuration frontale.


