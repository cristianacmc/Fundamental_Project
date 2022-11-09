from application import app, db
from application.models import Users, Orders, OrdersTruffles, Truffles
from application.forms import AddUser, AddTruffle, AddOrderD, AddOrderT
from flask import Blueprint, render_template
from flask import Flask, request, redirect, url_for
from flask_login import login_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    all_truffles = Truffles.query.all()
    return render_template('home.html', all_truffles=all_truffles)

@app.route('/about')
def aboutPage():
    return render_template('about.html')
    
@app.route('/cart')
def cart():
    return render_template('cart.html')

# form add user 
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUser()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users(
                forename = form.forename.data,
                surname = form.surname.data,
                email = form.email.data,
                username = form.username.data,
                password = form.password.data,
                phone = form.phone.data,
                address = form.address.data,
                dob = form.dob.data
            )
            db.session.add(user)
            db.session.commit()
            # redirects the user to the home page
            return redirect(url_for('add_user'))

    # pass object to Jinja2 template
    return render_template('AddUser.html', form=form)
            

# form add truffle
@app.route('/add_truffle', methods = ['GET','POST'])
def add_truffle():
    # instantiate the DogForm object
    form = AddTruffle()
    # checks is the http request is a post request
    if request.method == 'POST':
        # checks if the form passes validation
        if form.validate_on_submit():
            # adds the dog to the database
            truffle = Truffles(
                title = form.title.data,
                truffle_description = form.truffle_description.data,
                unit_price = form.unit_price.data,
                in_stock = form.in_stock.data
            )
            db.session.add(truffle)
            db.session.commit()
            # redirects the user to the home page
            return redirect(url_for('add_truffle'))

    # pass object to Jinja2 template
    return render_template('AddTruffle.html', form=form)

# form add order
@app.route('/add_order', methods = ['GET','POST'])
def add_order():
    # query OrderTurffle total
    ot_join = Orders.query.join(OrdersTruffles).all()
    user_id = ot_join.user_id

    # instantiate the DogForm object
    form = AddOrderD()
    # checks is the http request is a post request
    if request.method == 'POST':
        # checks if the form passes validation
        if form.validate_on_submit():
            # adds the dog to the database
            order = Orders(
                order_date = form.order_date.data
                
            )
            db.session.add(order)
            db.session.commit()
            # redirects the user to the home page
            return redirect(url_for('add_order'))

    # pass object to Jinja2 template
    return render_template('addOrderD.html', form=form, users=user_id)

# form add order truffle
@app.route('/add_order_truffle', methods = ['GET','POST'])
def add_order_T():
    # query list of truffles from db
    get_truffles = OrdersTruffles.query.join(Truffles).all()
    # instantiate the DogForm object
    form = AddOrderT()
    # checks is the http request is a post request
    if request.method == 'POST':
        # checks if the form passes validation
        subtotal = get_truffles.unit_price * get_truffles.quantity
        if form.validate_on_submit():
            # adds the dog to the database
            order = Orders(
                order_date = form.order_date.data,
                quantity = form.quantity.data
            )
            db.session.add(order)
            db.session.commit()
            # redirects the user to the home page
            return redirect(url_for('add_order_truffle'))

    # pass object to Jinja2 template
    return render_template('addOrderT.html', form=form, get_truffles = get_truffles, subtotal=subtotal)


