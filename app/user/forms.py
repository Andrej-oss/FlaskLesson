from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange

class UserForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'name should be 2 - 20')])
    surname = StringField('Surname', [DataRequired(), length(2, 20, 'surname should be 2 - 20')])
    age = IntegerField('Age', [DataRequired(), NumberRange(18, 100, 'age should be 18 -120')])
    city = StringField('City', [DataRequired(), length(2, 40, 'surname should be 2 - 40')])
    save = SubmitField('Save')
