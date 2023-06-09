from app import db

class Pizza(db.Model):
    __tablename__ = "pizza"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String)
    price = db.Column(db.Integer)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    amount = db.Column(db.Integer, default = 1)
    phone = db.Column(db.String)
    city =  db.Column(db.String)
    address = db.Column(db.String)
    comment =  db.Column(db.Text)
    status = db.Column(db.String)
