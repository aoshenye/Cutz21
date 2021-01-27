"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


class ContactForm(FlaskForm):
    name = StringField(
        'barber_name',
        [DataRequired()]
    )
    email = StringField(
        'comment_x',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    body = TextField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')