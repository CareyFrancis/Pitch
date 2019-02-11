from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
    category_id = SelectField('Select category', choices=[('1', 'Pick Up Lines'), ('2', 'Technology'), ('3', 'Business'),('4','Interview')])
    title = StringField('Title of your Pitch')
    content = TextAreaField('')
    submit = SubmitField('Add Pitch')