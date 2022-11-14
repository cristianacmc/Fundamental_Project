from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class AddTruffle(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(min=2,max=100)])
    truffle_description = StringField('Description: ', validators=[DataRequired(), Length(min=2,max=400)])
    category = SelectField("Category Type", choices=[
        (1, "Dairy"), 
        (2, "Dairy Free"), 
        (3, "Sugar Free")
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
        (3, "Sugar Free")
    ])
    unit_price = StringField('Price: ', validators=[DataRequired()])
    in_stock = IntegerField('Stock: ', validators=[DataRequired()])
    submit = SubmitField("Update")

class AddCategory(FlaskForm):
    category = StringField('Category:', validators=[DataRequired(), Length(min=2,max=30)])

class UpdateCategory(FlaskForm):
    category = StringField('category:', validators=[DataRequired(), Length(min=2,max=30)])
 