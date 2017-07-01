from app import db

class Locataires(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    surname = db.Column(db.String(64), index=True, unique=True)
    telephone = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    commentaire = db.Column(db.String(240), index=True, unique=True)
    reference = db.Column(db.String(64), index=True, unique=True)	

    def __init__(self, name, surname,telephone,email):
        self.email = email
	self.name=name
	self.surname=surname
	self.telephone=telephone

    def __repr__(self):
        return '<User %r>' % (self.name)

class Gites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    photos = db.Column(db.String(120), index=True, unique=True)
    plan = db.Column(db.String(120), index=True, unique=True)
    contrat = db.Column(db.String(120), index=True, unique=True)
    adresse = db.Column(db.String(120), index=True, unique=True)
    capacity = db.Column(db.Integer, index=True, unique=True)
    prixunitairebas = db.Column(db.Integer, primary_key=True)
    prixunitaireweek = db.Column(db.Integer, primary_key=True)
    prixunitairehaut = db.Column(db.Integer, primary_key=True)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, index=True, unique=True)
    nbadultes = db.Column(db.Integer, index=True, unique=True)
    nbenfant = db.Column(db.Integer, index=True, unique=True)
    nblitdoubles = db.Column(db.Integer, index=True, unique=True)
    nblitsimple = db.Column(db.Integer, index=True, unique=True)
    locataire = db.relationship('Locataire', backref='locataires', lazy='dynamic')
    gites = db.relationship('Gites', backref='gites', lazy='dynamic')
    debut
    nbjours
    cout = db.Column(db.Integer, index=True, unique=True)
    deposit = db.relationship()
    solde = db.relationship()
    extras = db.relationship()
    events = deb.relationship()
     
  

class Paiement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, index=True, unique=True)
    montant = db.Column(db.Float, index=True, unique=True)
    deposit = db.Column(db.Float, index=True, unique=True)
    solde = db.Column(db.Float, index=True, unique=True)	
    createdate = db.Column(db.DateTime, index=True, unique=True)	
    depositpaid= db.Column(db.Boolean, index=True, unique=True)	
    soldepaid= db.Column(db.Boolean, index=True, unique=True)	
    extrapaid= db.Column(db.Boolean, index=True, unique=True)	


class Extra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantite = db.Column(db.Integer, primary_key=True)
    prixunitaire = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)


class agenda(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    gites = deb.relationship()
    date = db.Column(db.date, index=True, unique=True)
    ppd = db.Column(db.integer, index=True, unique=True)
    availability = db.Column(db.Boolean, index=True, unique=True)
    


