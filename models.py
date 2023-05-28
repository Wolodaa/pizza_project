from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "user" # ім'я таблиці

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    orders = db.relationship('Order', backref='order', lazy=True)

    #Метод repr використовується для відображення об'єкта у зручному для читача форматі.
    def __repr__(self):
        return f"User: {self.username}"

    def set_password(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)
   
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Pizza(db.Model):
    __tablename__ = "pizza"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String)
    price = db.Column(db.Integer)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    address = db.Column(db.String)
    status = db.Column(db.String)
