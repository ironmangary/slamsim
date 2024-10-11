# forms/league_form.py
# Ver 2024.10.5
# For SlamSim

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class league_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    abbreviation = StringField('Abbreviation', validators=[DataRequired()])
    logo = FileField('Upload File', validators=[
        FileAllowed(['jpg', 'png', 'gif'], 'Images only')  
    ])
    status = RadioField('Status', choices=[('Active', 'Active'), ('Inactive', 'Inactive')], validators=[DataRequired()])
    owner = StringField('Owner')
    headquarters = StringField('Headquarters')
    description = TextAreaField('Description')
    submit = SubmitField('Submit')
    