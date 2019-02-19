from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Creating user

class User(UserMixin,db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255),unique =True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255)) 
    profile_pic_path = db.Column(db.String(),nullable='False', default='default.png')

    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    
    posts = db.relationship('Posts',backref = 'author',lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User('{self.username}')"
         


class Posts(UserMixin,db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
   
    def save_posts(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Posts ('{self.title} ,{self.date_posted}')"




class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


