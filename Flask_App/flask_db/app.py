from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    address = db.Column(db.String(200))
    dob = db.Column(db.DateTime, nullable=False)
    orders = db.relationship('Orders', backref='customer', lazy=True)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_date = db.Column(db.DateTime, nullable=False)
    order_truffle = db.relationship('OrdersTruffles', backref='order_t')

class OrdersTruffles(db.Model):        
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    truffles_id = db.relationship('Truffles', backref='order_truffle')
    quantity = db.Column(db.DateTime, nullable=False)
    #truffle_items = db.relationship('Truffles', backref='order_t_id')

class Truffles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    title = db.Column(db.String(100), nullable=False)
    truffle_description = db.Column(db.String(400), nullable = False)
    unit_price = db.Column(db.Float)
    in_stock = db.Column(db.Integer)    
    #orderTId = db.Column(db.Integer, db.ForeignKey('ordersTruffles.id'))
    #category = db.column(db.Integer, db.ForeignKey('categories.id'))
    truffle_orders = db.relationship('OrdersTruffles', backref='order_t_id')

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    truffles = db.relationship('Truffles', backref='category')


if __name__=='__main__':
    app.run(debug=True)