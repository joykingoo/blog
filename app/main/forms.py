from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
# from .models import User

class PostsForm(FlaskForm):
    title = StringField('Post Title', validators=[Required()])
    post = TextAreaField('Add Post',validators=[Required()])
    submit = SubmitField('Submit')


# class CommentForm(FlaskForm):

#     title = StringField('Review title',validators=[Required()])
#     comment = TextAreaField('Pitch review', validators=[Required()])
#     submit = SubmitField('Submit')



# class FeedbackForm(FlaskForm):

#     title = StringField('Feedback title',validators=[Required()])

#     feedback = TextAreaField('Add feedback', validators=[Required()])

#     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')