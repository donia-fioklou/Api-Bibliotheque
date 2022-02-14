from itertools import count
from os import abort
import os
from tkinter.tix import Tree
from turtle import back

from urllib.parse import quote_plus
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from flask_cors import CORS,cross_origin

load_dotenv()
app=Flask(__name__)
motPasse=quote_plus(os.getenv('password'))
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:{}@localhost:5432/bibliotheque".format(motPasse)
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
CORS(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
    return response

db=SQLAlchemy(app)

class Categorie(db.Model):
    __tablename__="categories"
    id=db.Column(db.Integer,primary_key=True)
    libelle=db.Column(db.String(15),nullable=False,unique=True)
    Livre=db.relationship('Livre',backref='categories',lazy=True)
    def formatcat(self):
        return{
            'id':self.id,
            'libelle':self.libelle }
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    
class Livre(db.Model):
    __tablename__='livres'
    id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.String(20),unique=True,nullable=False)
    titre=db.Column(db.String(50),nullable=False)
    datePub=db.Column(db.Date,nullable=True)
    auteur=db.Column(db.String(30),nullable=False)
    editeur=db.Column(db.String(30),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=True)
    def format(self):
            return{
            'id':self.id,
            'isbn':self.isbn,  
            'titre':self.titre,
            'datePub':self.datePub,
            'auteur':self.auteur,
            'editeur':self.editeur,
            'categorie_id':self.categorie_id
            
        }
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()



db.create_all()
#liste de tout les livres
@app.route('/livres',methods=['GET'])
def listesLivres():
    livres=Livre.query.all()
    livresFormat=[li.format() for li in livres]
    return jsonify({
        'success':True,
        'listesLiivres':livresFormat
    })
#rechercher un livre par son id
@app.route('/livres/<int:id>')
def rechercheId(id):
    livre=Livre.query.get(id)
    if livre is None:
      return  abort(404)
    else:
        return jsonify({
        'success':True,
        'livre':livre.format()
        })
#- Lister la liste des livres d’une catégorie
@app.route('/categories/<int:id>/livres')
def livreParCategorie(id):
    livres=Livre.query.filter_by(categorie_id=id)
    livresFormat=[li.format() for li in livres]
    return jsonify({
        'success':True,
        'listesLiivres':livresFormat
    })
#lister une categorie
@app.route('/categorie')
def listerCategorie():
    categorie=Categorie.query.limit(1).all()
    categorieFormat=[li.formatcat() for li in categorie]
    if categorie is None:
      return  abort(404)
    else:
        return jsonify({
        'success':True,
        'livre':categorieFormat
        })
#lister tout les categories
@app.route('/categories',methods=['GET'])
def listescategories():
    categories=Categorie.query.all()
    categorieFormat=[li.formatcat() for li in categories]
    return jsonify({
        'success':True,
        'listesLiivres':categorieFormat
    })
#chercher une categorie par son id    
@app.route('/categories/<int:id>')
def categorieId(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
      return  abort(404)
    else:
        return jsonify({
        'success':True,
        'livre':categorie.formatcat()
        })
#supprimer un livre
@app.route('/deleteLivre/<int:id>',methods=['DELETE','GET'])
def deleteLivre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify({
            'success':True,
            'nombre livre':Livre.query.count(),
            'livre supprimer':livre.format()
        })
#supprimer une categories
@app.route('/deleteCategorie/<int:id>',methods=['DELETE','GET'])
def deleteCategorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        categorie.delete()
        return jsonify({
            'success':True,
            'nombre livre':Categorie.query.count(),
            'livre supprimer':categorie.formatcat()
        })
        
# modifier les informations d’un livre
@app.route('/modifylivre/<int:id>',methods=['PATCH'])
def modifyLivre(id):
        livre=Livre.query.get(id)
        if livre is None:
            abort(404)
        else:
            body=request.get_json()
            livre.isbn=body.get('isbn')
            livre.titre=body.get('titre')
            livre.datePub=body.get('datePub')
            livre.auteur=body.get('auteur')
            livre.editeur=body.get('editeur')
            livre.categorie_id=body.get('categorie_id')
            livre.update()
            return jsonify({
                'success':True,
                'livreId':id,
                'livre':livre.format()
            })
# Modifier le libellé d’une categorie
@app.route('/modifyCategorie/<int:id>',methods=['PATCH'])
def modifyCategorie(id):
        categorie=Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            body=request.get_json()
            categorie.libelle=body.get('libelle')
            categorie.update()
            return jsonify({
                'success':True,
                'livreId':id,
                'livre':categorie.formatcat()
            })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404
    




    



        
    


    

    