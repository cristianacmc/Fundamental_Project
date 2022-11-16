from application import db
from application import app

# Creates all table classes defined
with app.app_context():
    db.drop_all()
    db.create_all()



#export DATABASE_URI="mysql+pymysql://root:9812@127.0.0.1:3306/chocolateshop"
