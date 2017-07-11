from app import db
from datetime import datetime

class Client(db.Model):
    idclient = db.Column(db.Integer, primary_Key=True, unique=True,autoincrement=True)
    email = db.Column(db.String(120),index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64))
    telephone = db.Column(db.String(64), unique=True)
    adresse = db.Column(db.String(240))
    reference=db.Column(db.Integer, db.ForeignKey('Reference.idReference'))
    ville = db.Column(db.String(64))	
    pays = db.Column(db.String(64))	
    codepostal = db.Column(db.Integer)
    commentaires= db.Colum(db.string(400))

    def __init__(self, name,surname,email,telephone=None,adresse=None,reference=None,ville=None,pays=None,codepostal=None,commentaire=None):
        self.name = name
        self.surname = surname
        self.email = email 
        self.telephone = telephone 
        self.adresse = adresse
        self.reference = reference 
        self.ville = ville 
        self.pays = pays
        self.codepostal = codepostal 
        self.commentaire = commentaire 
        self. = 

    def __repr__(self):
        return '<UserName %r>' % self.name


# un client a une réference,
#une reference  peut amener plusieurs  clients
# relation 1-n
# urladmin permet l'acces a l'interface d'administration de la reference (ie  booking, leboncoin)
class Reference(db.Model):
     idReference=db.Column(db.String(60), primary_Key=True,unique=True,autoincrement=True)
     libellereference=db.Column(db.String(64), index=True)
     urladmin=db.Column(db.String(160))
     user=db.Column(db.String(160)
     password=db.Column(db.String(160)
     users= db.relationship('Client', backref='client',lazy='dynamic')
     

# un client peut avoir plusieurs reservations
#mais une reservation n'appartient qu'a un client

# une reservation est  composee de un ou plusieurs reservationsunGite
# une reservation1gite est lie a une Reservation

class Reservation(db.Model):
    idReservation=sb.Column(db.Integer,primary_key=True)
    idClient=(db.Integer(120), foreign_key=True) 
    nbadultes = db.Column(db.Integer)
    datedebut = db.Column(db.DateTime)	
    datefindebut = db.Column(db.DateTime)	
    dateContact = db.Column(db.DateTime)	
    nbenfant = db.Column(db.Integer)
    cout = db.Column(db.Float)
    montantaccompte = db.Column(db.Integer, index=True, unique=True)# 0  accompte non payé
    indicateurpaiment = db.Column(db.Integer, index=True, unique=True)# 1 ok
    montantCaution = db.Column(db.Integer, index=True, unique=True)# 0  accompte non payé
    libprix=(db.String(120), foreign_key=True)
    commentaires= db.Colum(db.string(400))

class Reservation1Gite(db.Model):
    idClient=
    idGites=
    idReservation=
	

#(chaumiere,"http://photo","http://plan","http://agenda",7,1,2)
class Gites(db.Model):
    id_gite= db.Column(db.Integer(64),  primary_key=True)
    name = db.Column(db.String(64),unique=True)
    photos_url = db.Column(db.String(120), unique=True)
    plan_url = db.Column(db.String(120),  unique=True)
    agenda_url = db.Column(db.String(120),  unique=True)
    capacity = db.Column(db.Integer)
    nbsdb = db.Column(db.Integer)
    adresse = db.Column(db.String(120))
    litsup = db.Column(db.integer)
    coeffstanding = db.Column(db.Float)
    

class libPrix(db.Model)
    libelle = db.Column(db.String(120), unique=True)
    prix = db.Column(db.Integer)
    actif = db.Column(db.Boolean)


    def __init__(self,name,photos=None,plan=None,contrat=None,addresse=None,capacity=None,prixperdaysweek=None,prixperdayweek=None,prixperdayshaut=None)
	
    def __repr__(self):
        return '<Gites %r>' % (self.name)



class ReservationExtra(db.Model)
	idClient
	idGite
	idReservation
	idExtra


class Extra(db.Model)
	idExtra
	prix
 	
