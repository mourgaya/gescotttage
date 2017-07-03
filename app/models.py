from app import db

# 1 locataire a 0,1 ou plusieurs gites
# 1 locataire a 0,1 ou plusieurs reservation
class Locataires(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    surname = db.Column(db.String(64), index=True, unique=True)
    telephone = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    commentaire = db.Column(db.String(240), index=True, unique=True)
    addresse = db.Column(db.String(240), index=True, unique=True)
    reference = db.Column(db.String(64), index=True, unique=True)	
    ville = db.Column(db.String(64), index=True, unique=True)	
    pays = db.Column(db.String(64), index=True, unique=True)	
    codepostal = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, surname,telephone,email,commentaire=None,addresse=None,reference=None,ville=none,pays=none):
        self.email = email
	self.name=name
	self.surname=surname
	self.telephone=telephone

    def __repr__(self):
        return '<Locataires %r>' % (self.name)

#1 gite a 1 exploitation journaliere
#1 gite a 1 reservation ?
class Gites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    photos = db.Column(db.String(120), index=True, unique=True)
    plan = db.Column(db.String(120), index=True, unique=True)
    contrat = db.Column(db.String(120), index=True, unique=True)
    addresse = db.Column(db.String(120), index=True, unique=True)
    capacity = db.Column(db.Integer, index=True, unique=True)
    latittude = db.Column(db.float, index=True, unique=True)
    longitude = db.Column(db.float, index=True, unique=True)
    prixperdaybas = db.Column(db.Integer, index=True, unique=True)
    prixperdaysweek = db.Column(db.Integer, index=True, unique=True)
    prixper3daysweek = db.Column(db.Integer, index=True, unique=True)
    prixperdayhaut = db.Column(db.Integer, index=True, unique=True)

    def __init__(self,name,photos=None,plan=None,contrat=None,addresse=None,capacity=None,prixperdaysweek=None,prixperdayweek=None,prixperdayshaut=None)
	
    def __repr__(self):
        return '<Gites %r>' % (self.name)
	
# 1 reservation  a 1 locataire
# 1 reservation a 1 ou plusieurs gites
# 1 reservation a 1 ou plusieurs paiement
# 1 reservation a 1 ou plusieurs extras
# 1 reservation a 1 ou plusieurs  contrats 
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, index=True, unique=True)
    nbadultes = db.Column(db.Integer, index=True, unique=True)
    nbenfant = db.Column(db.Integer, index=True, unique=True)
    nblitdoubles = db.Column(db.Integer, index=True, unique=True)
    nblitsimple = db.Column(db.Integer, index=True, unique=True)
    locataire = db.relationship('Locataire', backref='locataires', lazy='dynamic')
    gites = db.relationship('Gites', backref='gites', lazy='dynamic')
    cout = db.Column(db.Integer, index=True, unique=True)
    paiement = deb.relationship()
    events = deb.relationship()
    
# 1 paiement correspond a 1 reservation
class Paiement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, index=True, unique=True)
    createdate = db.Column(db.DateTime, index=True, unique=True)	
    montant = db.Column(db.Float, index=True, unique=True)
    deposit = db.Column(db.Float, index=True, unique=True)
    solde = db.Column(db.Float, index=True, unique=True)	
    depositpaid= db.Column(db.Boolean, index=True, unique=True)	
    soldepaid= db.Column(db.Boolean, index=True, unique=True)	
    extrapaid= db.Column(db.Boolean, index=True, unique=True)	
    

class Extra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantite = db.Column(db.Integer, primary_key=True)
    prixunitaire = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)


# una exploitation journaliere  est associé a 1 gite
class exploitejournalier(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    gites = deb.relationship()
    date = db.Column(db.DateTime, index=True, unique=True)
    ppd = db.Column(db.integer, index=True, unique=True)
    availability = db.Column(db.Boolean, index=True, unique=True)

# un event est associé a  une ou plusieur  exploitation  journaliere
class event(db.model):
    id = db.Column(db.Integer, primary_key=True)
    debutdb.Column(db.DateTime,index=True,Unique=True)
    nbjours = db.Column(db.Integer, index=True, unique=True)
    	

