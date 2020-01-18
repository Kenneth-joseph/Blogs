from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique= True,nullable=False)
    username =db.Column(db.String(255),unique =True,nullable=False)
    password_hash = db.Column(db.String(),unique=True)
    # blog=db.relationship('Blog', backref='us')
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.add(self)
        db.session.commit()

    def __repr__ (self):
        return f'User{self.username}'
        
class Blog(db.Model):
    __tablename__ = 'blog'

    id=db.Column(db.Integer,primary_key=True)
    post= db.Column(db.String(255),nullable= False)
    title = db.Column(db.String(255),nullable= False)
    time=db.Column(db.DateTime,default=datetime.utcnow)
    category= db.Column(db.String(255),nullable=False)
    user_id= db.Coloumn(db.Integer,db.ForeignKey('users.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def __repr__ (self):
        return f'blog{self.post}'

class Comment(db.Model):
    __tablename__ = 'comment'

    id=db.Column(db.Integer,primary_key=True)
    
