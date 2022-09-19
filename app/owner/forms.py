from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class RegisterOwner(Form):
    name = StringField('Name', [DataRequired(), length(2, 30, 'name must be 2-30')])
    age = IntegerField('Age', [DataRequired(), NumberRange(18, 100, 'age must be 18-100')])
    city = StringField('City', [DataRequired(), length(2, 30, 'city must be 2-30')])
    save = SubmitField('Save')


class RegisterPet(Form):
    name = StringField('Name', [DataRequired(), length(2, 30, 'name must be 2-30')])
    age = IntegerField('Age', [DataRequired(), NumberRange(18, 100, 'age must be 0-30')])
    animal_type = StringField('Animal type', [DataRequired(), length(2, 30, 'type must be 2-30')])
    save = SubmitField('Save')
