from application import db

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
 





    





