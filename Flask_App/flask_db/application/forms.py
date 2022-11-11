from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Email

# forms
# class AddUser(FlaskForm):
#     forename = StringField('First Name:', validators = [Length(min=2, max=15)])
#     surname = StringField('Surname: ', validators = [Length(min=2, max=15)])
#     email = StringField('Email: ', validators=[Email()])
#     username = StringField('Username', validators=[
#         DataRequired(),
#         # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.
#         UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
#         Length(min=2,max=15)
#         ])
#     password = PasswordField('Password', validators=[
#         DataRequired(),
#         EqualTo('confirm_password')
#     ])
#     confirm_password = PasswordField('Confirm password')
#     phone = StringField('Phone: ', validators = [Length(max=10)])
#     address = StringField('Address: ', validators=[DataRequired()])
#     dob = DateField('Date of birth(y-m-d): ', validators=[DataRequired()])
#     submit = SubmitField('Sign up')

class AddTruffle(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(min=2,max=100)])
    truffle_description = StringField('Description: ', validators=[DataRequired(), Length(min=2,max=400)])
    category = SelectField("Category Type", choices=[
        ("dairy", "Dairy"), 
        ("dairy-free", "Dairy Free"), 
        ("sugar free", "sugar Free")
    ])
    unit_price = StringField('Price: ', validators=[DataRequired()])
    in_stock = IntegerField('Stock: ', validators=[DataRequired()])
    submit = SubmitField("Submit")

class UpdateTruffle(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(min=2,max=100)])
    truffle_description = StringField('Description: ', validators=[DataRequired(), Length(min=2,max=400)])
    category = SelectField("Category Type", choices=[
        (1, "Dairy"), 
        (2, "Dairy Free"), 
        (3, "sugar Free")
    ])
    unit_price = StringField('Price: ', validators=[DataRequired()])
    in_stock = IntegerField('Stock: ', validators=[DataRequired()])
    submit = SubmitField("Update")

# class AddOrderT(FlaskForm):
#     #user_id = 
#     quantity = IntegerField('Quantity: ', validators=[DataRequired()])
#     #truffle_id

# class AddOrderD(FlaskForm):
#     order_date = DateField('Date:', validators=[DataRequired()])
#     user_id = SelectField("user_id")

class AddCategory(FlaskForm):
    category = StringField('Category:', validators=[DataRequired(), Length(min=2,max=30)])
