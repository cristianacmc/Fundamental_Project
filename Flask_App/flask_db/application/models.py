from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_login import UserMixin
from application import db

# class Users(db.Model):
#     __tablename__="users"
#     id = db.Column(db.Integer, primary_key=True)
#     forename = db.Column(db.String(40), nullable=False)
#     surname = db.Column(db.String(40), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     phone = db.Column(db.String(16), nullable=False)
#     address = db.Column(db.String(200))
#     dob = db.Column(db.DateTime, nullable=False)
#     orders = db.relationship('Orders', backref='customer', lazy=True)
#     ordersT = db.relationship('OrdersTruffles', backref='customer', lazy=True)

# class Orders(db.Model):
#     __tablename__="orders"
#     id = db.Column(db.Integer, primary_key=True)
#     order_date = db.Column(db.DateTime, nullable=False)
#     orderTruffles = db.relationship('OrdersTruffles', backref='order_t')

# class OrdersTruffles(db.Model):        
#     __tablename__="orderstruffles"
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
#     truffle_id = db.relationship('Truffles', backref='order_truffle')
#     quantity = db.Column(db.Integer, nullable=False)

class Categories(db.Model):
    __tablename__="categories"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20))
    truffle_id = db.relationship('Truffles', backref='order_truffle')

    
class Truffles(db.Model):
    __tablename__="truffles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    truffle_description = db.Column(db.String(500), nullable = False)
    unit_price = db.Column(db.Float)
    in_stock = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
 





    





