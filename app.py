from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # створюємо  

app = Flask(__name__) # Створюємо веб–додаток Flask
# import secrets
# secrets.token_hex(20)
# https://docs.python.org/3/library/secrets.html7f9fbb1e061d2e5187920e4203c93dcae00fbec8
app.config["SECRET_KEY"] = "7f9fbb1e061d2e5187920e4203c93dcae00fbec8"
# налаштувати базу даних SQLite відносно папки екземпляра програми
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Pizzeria.db"
db.init_app(app)

from routes import *

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу