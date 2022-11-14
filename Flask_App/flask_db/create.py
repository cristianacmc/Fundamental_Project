from application import db

# Creates all table classes defined
db.drop_all()
db.create_all() 


#export DATABASE_URI="mysql+pymysql://root:9812@127.0.0.1:3306/chocolateshop"
