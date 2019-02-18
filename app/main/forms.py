from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email

# from .models import User

class PostsForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content= TextAreaField('Content',validators=[Required()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):

   body = TextAreaField('comment', validators=[Required()])
   author = TextAreaField('By', validators=[Required()])
   submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
   name = StringField("Your Name")
   email = StringField("Email")
   submit= SubmitField('Subscribe')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')