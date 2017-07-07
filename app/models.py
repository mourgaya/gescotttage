from app import db

class Client(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    surname = db.Column(db.String(64), unique=True)
    telephone = db.Column(db.String(64), unique=True)
    adresse = db.Column(db.String(240),  unique=True)
    reference = db.Column(db.String(64), index=True, unique=True)	
    ville = db.Column(db.String(64), unique=True)	
    pays = db.Column(db.String(64), unique=True)	
    codepostal = db.Column(db.Integer)

    def __init__(self, name, surname,telephone,email,commentaire=None,addresse=None,reference=None,ville=none,pays=none):
        self.email = email
	self.name=name
	self.surname=surname
	self.telephone=telephone

    def __repr__(self):
        return '<Locataires %r>' % (self.name)

class Reservation(db.Model):
    email = db.Column(db.String(120), foreign_key=True)
    gites = db.relationship('Gites', backref='gites', lazy='dynamic')
    nbadultes = db.Column(db.Integer, index=True, unique=True)
    datedebut = db.Column(db.DateTime, index=True, unique=True)	
    datefindebut = db.Column(db.DateTime, index=True, unique=True)	
    nbenfant = db.Column(db.Integer, index=True, unique=True)
    cout = db.Column(db.Integer, index=True, unique=True)
    montantaccompte = db.Column(db.Integer, index=True, unique=True)# 0  accompte non payé
    indicateurpaiment = db.Column(db.Integer, index=True, unique=True)# 1 ok

#(resa1,chaumiere,extra)
class Planninggite(db.Model):
    Reservation= foreign
    Gite= foreign
    extra= foreign

#(chaumiere,"http://photo","http://plan","http://agenda",7,1,2)
class Gites(db.Model):
    id_gite= db.Column(db.Integer(64),  primary_key=True)
    name = db.Column(db.String(64),unique=True)
    photos_url = db.Column(db.String(120), unique=True)
    plan_url = db.Column(db.String(120),  unique=True)
    agenda_url = db.Column(db.String(120),  unique=True)
    capacity = db.Column(db.Integer)
    nbsdb = db.Column(db.Integer)
    adresse = db.Column(db.String(120), index=True, unique=True)
    litsup = db.Column(db.integer)
    coeffstanding = db.Column(db.Float)
    


class Tarif(db.Model)
    gite = db.Column(db.String(64), primary_key=True)
    libelle = db.Column(db.String(120), unique=True)
    prix = db.Column(db.Integer)
    actif = db.Column(db.Boolean)


    def __init__(self,name,photos=None,plan=None,contrat=None,addresse=None,capacity=None,prixperdaysweek=None,prixperdayweek=None,prixperdayshaut=None)
	
    def __repr__(self):
        return '<Gites %r>' % (self.name)



class Prixref(db.Model)
    id  =
    name =
    value =
    usecoeff =

