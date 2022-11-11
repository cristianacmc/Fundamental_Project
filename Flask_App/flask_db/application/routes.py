from application import app, db
from application.models import Truffles, Categories
from application.forms import AddTruffle, UpdateTruffle, AddCategory
from flask import render_template, redirect, url_for, request

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/')
@app.route('/home')
def home():
    all_truffles = Truffles.query.join(Categories, isouter=True).all()
    return render_template('home.html', all_truffles=all_truffles)

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
    return render_template('add_truffle.html', form=form)

@app.route('/update/<title>', methods=['GET', 'POST'])
def update(title):
    updateform = UpdateTruffle()
    truffle= Truffles.query.filter_by(title=title).first()
    
    # Prepopulate the form boxes with current values when they open the page.
    if request.method == 'GET':
        updateform.title.data = truffle.title
        updateform.truffle_description.data = truffle.truffle_description
        updateform.category.data= truffle.category_id
        updateform.unit_price.data = truffle.unit_price
        updateform.in_stock.data = truffle.in_stock
        return render_template('update.html', form=updateform)

    # Update the item in the databse when they submit
    else:
        if updateform.validate_on_submit():
            truffle.title = updateform.title.data
            truffle.truffle_description = updateform.truffle_description.data
            truffle.category_id = updateform.category.data
            truffle.unit_price = updateform.unit_price.data
            truffle.in_stock = updateform.in_stock.data
            db.session.commit()
            return redirect(url_for('home'))

@app.route('/delete/<title>', methods=['GET', 'POST'])
def delete(title):
    truffle = Truffles.query.filter_by(title=title).first()
    db.session.delete(truffle)
    db.session.commit()
    return redirect(url_for('home'))

# form add order truffle
@app.route('/add_category', methods = ['GET','POST'])
def add_category():
    # instantiate the DogForm object
    form = AddCategory()
    # checks is the http request is a post request
    if request.method == 'POST':
        # checks if the form passes validation 
        if form.validate_on_submit():
            # adds the dog to the database
            category = Categories(
                category = form.category.data,
            )
            db.session.add(category)
            db.session.commit()
            
            # redirects the user to the home page
            return redirect(url_for('add_category'))
 
    # pass object to Jinja2 template
    return render_template('add_category.html', form=form)

# # form add order
# @app.route('/add_order', methods = ['GET','POST'])
# def add_order():
#     # query OrderTurffle total
#     ot_join = Orders.query.join(OrdersTruffles).all()
#     user_id = ot_join.user_id

#     # instantiate the DogForm object
#     form = AddOrderD()
#     # checks is the http request is a post request
#     if request.method == 'POST':
#         # checks if the form passes validation
#         if form.validate_on_submit():
#             # adds the dog to the database
#             order = Orders(
#                 order_date = form.order_date.data
#             )
#             db.session.add(order)
#             db.session.commit()
#             # redirects the user to the home page
#             return redirect(url_for('add_order'))

#     # pass object to Jinja2 template
#     return render_template('addOrderD.html', form=form, users=user_id)
  
# # form add user 
# /* @app.route('/add_user', methods=['GET', 'POST'])
# def add_user():
#     form = AddUser()
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             user = Users(
#                 forename = form.forename.data,
#                 surname = form.surname.data,
#                 email = form.email.data,
#                 username = form.username.data,
#                 password = form.password.data,
#                 phone = form.phone.data,
#                 address = form.address.data,
#                 dob = form.dob.data
#             )
#             db.session.add(user)
#             db.session.commit()
#             # redirects the user to the home page
#             return redirect(url_for('add_user'))

#     # pass object to Jinja2 template
#     return render_template('AddUser.html', form=form)




