from app import db

# Creates all table classes defined
db.drop_all()
db.create_all() 


''''
#export DATABASE_URI="mysql+pymysql://root:9812@127.0.0.1:3306/flask_trainning"
# adding records to Truffles table 
t_1 = Truffles(title='Truffle with zero added sugar 30g', truffle_description='Delicious milk chocolate truffle with zero added sugar. With surprising flavor, ideal for those who have dietary restrictions!', unit_price=2.2)
db.session.add(t_1)
db.session.commit()

# adding records to Users table 
u_1 = Users(forename='Fabio', surname='de Melo', email='demelo@gmail.com', username='demelof', password='1234', phone='123456789', address='123 Fake St.', dob='2022-02-14', orders=1)
u_2 = Users(forename='Jane', surname='Roberts', email='demelo@gmail.com', username='demelof', password='6758', phone='0143258679', address='456 Not Real Ave.', dob='2005-07-15', orders=2)
u_3 = Users(forename='John', surname='Smith', email='jsmith@example.com', username='smithj', password='4321', phone='0123456789', address='789 Imaginary Ln..', dob='2000-10-25', orders=3)
u_4 = Users(forename='Kelsie', surname='Hayter', email='khayter95@mail.org', username='ksernk', password='4109', phone='0123456789', address='135 Made-up Blvd.', dob='1995-02-26', orders=4)
u_5 = Users(forename='Darell', surname='Woods', email='darellwoods@email.co.uk', username='ksernk', password='4109', phone='0123456789', address='135 Made-up Blvd.', dob='2001-11-16', orders=5)
db.session.add(u_1)
db.session.add(u_2)
db.session.add(u_3)
db.session.add(u_4)
db.session.add(u_5)
db.session.commit()


# adding records to Categories table 
c_1 = Categories(title='dairy');
c_2 = Categories(title='dairy-free');
c_3 = Categories(title='sugar-free');
db.session.add(c_1)
db.session.add(c_2)
db.session.add(c_3)
db.session.commit()

# adding records to Orders table
print("***Orders records***")
o_1 = Orders(order_date='2022-10-24', order_truffle=1)
o_2 = Orders(order_date='2022-10-24', order_truffle=2)
o_3 = Orders(order_date='2022-10-24', order_truffle=3)
o_4 = Orders(order_date='2022-10-24', order_truffle=4)
o_5 = Orders(order_date='2022-10-24', order_truffle=5)
db.session.add(o_1)
db.session.add(o_2)
db.session.add(o_3)
db.session.add(o_4)
db.session.add(o_5)
db.session.commit()

# adding ecords to Orders_Truffles 
ot_1 = Orders_Truffles(id=1, order_id=1, truffle_id=1, quantity=1)
ot_2 = Orders_Truffles(id=2, order_id=1, truffle_id=1, quantity=2)
ot_3 = Orders_Truffles(id=3, order_id=1, truffle_id=1, quantity=3)
ot_4 = Orders_Truffles(id=4, order_id=2, truffle_id=1, quantity=3)
ot_5 = Orders_Truffles(id=5, order_id=2, truffle_id=1, quantity=4)
db.session.add(ot_1)
db.session.add(ot_2)
db.session.add(ot_3)
db.session.add(ot_4)
db.session.add(ot_5)
db.session.commit()

print("***Truffles records***")
print(f"Truffle name: {t_1.title}, Description: {t_1.truffle_description}, price: {t_1.unit_price}")

print("***Users records***")
print(f"Name: {u_1.forename} - {u_1.surname} - {u_1.email} - {u_1.username} - {u_1.address} - {u_1.password}")
print(f"Name: {u_2.forename} - {u_2.surname} - {u_2.email} - {u_2.username} - {u_2.address} - {u_2.password}")

print("***Categories records***")
print(f"Categories: {c_1.id}, {c_1.title}")
print(f"Categories: {c_2.id}, {c_2.title}")
print(f"Categories: {c_3.id}, {c_3.title}")

print("***Orders records***")
print(f"Orders: {o_1.id} - {o_1.date}")
print(f"Orders: {o_2.id} - {o_2.date}")
print(f"Orders: {o_3.id} - {o_3.date}")
print(f"Orders: {o_4.id} - {o_4.date}")
print(f"Orders: {o_5.id} - {o_5.date}")

print("***Orders_truffles records***")
print(f"Orders: {ot_1.id} - {ot_1.quantity}")
print(f"Orders: {ot_2.id} - {ot_2.quantity}")
print(f"Orders: {ot_3.id} - {ot_3.quantity}")
print(f"Orders: {ot_4.id} - {ot_4.quantity}")
print(f"Orders: {ot_5.id} - {ot_5.quantity}")
'''