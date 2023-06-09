import datetime
from flask import render_template,  url_for, request, flash, redirect
from app import app, db
from models import Order, Pizza

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    pizza = Pizza.query.all()
    print(pizza)
    return render_template("index.html", pizzas = pizza)#Результат, що повертається у браузе

@app.route("/order/<item_id>", methods = ["POST" , "GET"]) # Вказуємо url-адресу для виклику функції
def order(item_id):
    pizza = Pizza.query.get(item_id)
    if request.method == "POST":
        new_order = Order(pizza_id=pizza.id,
                          name = request.form['name'],
                          amount = request.form['amount'],
                          phone = request.form['phone'],
                          city = request.form['city'],
                          address = request.form['address'],
                          comment = request.form['comment'],
                          status = "new")
        db.session.add(new_order)
        db.session.commit()
        flash("Замовлення прийнято. Очікуйте кур'єра.", "alert-success")
        return redirect(url_for('index'))

    return render_template("order.html", pizza = pizza)

@app.errorhandler(404)
def error_404(err):
    return render_template('error404.html')
