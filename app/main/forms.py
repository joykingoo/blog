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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')