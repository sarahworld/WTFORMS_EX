from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import URL, NumberRange, InputRequired, Optional, Length

class AddPetForm(FlaskForm):
    """Form for addig pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')])
    photo_url = StringField("Photo", validators=[Optional(), URL(message="url required")])
    age = IntegerField("age",validators=[NumberRange(min=0, max=30, message="Age should be between 0 and 30")])
    notes = StringField("Pet details")
    is_available = BooleanField("is_available")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo", validators=[Optional(), URL(message="url required")])
    notes = TextAreaField("Pet details", validators=[Optional(), Length(min=10)])
    is_available = BooleanField("is_available")