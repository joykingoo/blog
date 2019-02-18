from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Posts
from .forms import PostsForm,UpdateProfile
from .. import db,photos
from flask_login import login_user, logout_user, login_required, current_user
import datetime
import requests
import json




# Views
@main.route('/')
def index():

    posters=Posts.query.all()
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Blog'

    lily = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()

    form = PostsForm()
    return render_template('index.html',form = form,title=title, posts=posters, lily=lily)
    

@main.route('/new_post', methods = ['GET','POST'])

def new_post():
    form = PostsForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        add_post = Posts(title=title,content=content,author=current_user)
        add_post.save_posts()
        flash("Your post has been created!" ,"success")
        return redirect(url_for('main.index'))
    return render_template('new_post.html',form=form, legend='Create Post')


@main.route('/post/<int:post_id>', methods = ['GET','POST'])

def post(post_id):
    post =Posts.query.get(post_id)
    form = PostsForm()
    title = form.title.data
    content = form.content.data
    
    return render_template('post.html',form=form, title=title , post=post, content=content)


@main.route('/post/<int:post_id>/update', methods = ['GET','POST'])
@login_required
def update_post(post_id):
    post =Posts.query.get(post_id)
    if post.author != current_user:
        abort(403)
        
    form = PostsForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('You have successfully updated blog')
        return redirect(url_for('main.post', post_id=post.id))

    elif request.method =='GET':
        title=post.title
        form.title.data = post.title
        form.content.data =post.content
        return render_template('new_post.html',form=form, title=title ,legend='Update Post',post=post)


@main.route("/post/<int:post_id>/delete", methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))


@main.route('/post/<post_id>/add/comment', methods = ['GET','POST'])
def comment(post_id):

   post = Post.query.filter_by(id = post_id).first()
   form = CommentForm()

   if form.validate_on_submit():
       body = form.body.data
       author = form.author.data

       new_comment = Comment(body=body,author=author)
       new_comment.save_comment()

       return redirect(url_for("main.read_post",post_id = post_id))
   return render_template("comment.html", form = form, post = post)



@main.route('/<int:post_id>/comments')
def show_comments(post_id):

   post = Post.query.filter_by(id = post_id).first()

   comments = Comment.get_comments(id)

   return render_template('show_comments.html',comments= comments,post =post)

@main.route('/<int:post_id>/comments/delete')
@login_required
def delete_comment(post_id):
   comment = Comment.query.filter_by(post_id = post_id).first()
   post_id = comment.post.id

   db.session.delete(comment)
   db.session.commit()
   return redirect(url_for('main.show_comments',post_id = post_id))

@main.route('/subscribe',methods=["GET","POST"])
def subscribe():
   form=SubscribeForm()

   if form.validate_on_submit():
       subscriber = Subscribe(name=form.name.data,email=form.email.data)
       db.session.add(subscriber)
       db.session.commit()

       mail_message("Welcome to Dee-blog","email/subscribe_user",subscriber.email,subscriber=subscriber)

       return redirect(url_for('main.blog'))
       title = 'Subscribe'
   return render_template('sub.html',subscribe_form=form)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

