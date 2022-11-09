from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Email

# forms

class UserCheck:
    def __init__(self, banned, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.
        self.banned = banned
        if not message:
            message = 'Please choose another username' # If no message chosen, then this default message is returned.
        self.message = message

    def __call__(self, form, field):
    # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)


class AddUser(FlaskForm):
    forename = StringField('First Name:', validators = [Length(min=2, max=15)])
    surname = StringField('Surname: ', validators = [Length(min=2, max=15)])
    email = StringField('Email: ', validators=[Email()])
    username = StringField('Username', validators=[
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.
        UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
        Length(min=2,max=15)
        ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm password')
    phone = StringField('Phone: ', validators = [Length(max=10)])
    address = StringField('Address: ', validators=[DataRequired()])
    dob = DateField('Date of birth(y-m-d): ', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class AddTruffle(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    truffle_description = StringField('Description: ', validators=[DataRequired()])
    category = SelectField("Category Type", choices=[
        ("dairy", "Dairy"), 
        ("dairy-free", "Dairy Free"), 
        ("sugar free", "sugar Free")
    ])
    submit = SubmitField("Submit")
    unit_price = StringField('Price: ', validators=[DataRequired()])
    in_stock = IntegerField('Stock: ', validators=[DataRequired()])
    #add_image 

class AddOrderD(FlaskForm):
    order_date = DateField('Date:', validators=[DataRequired()])
    user_id = SelectField("user_id")
   
class AddOrderT(FlaskForm):
    #user_id = 
    quantity = IntegerField('Quantity: ', validators=[DataRequired()])
    #truffle_id
