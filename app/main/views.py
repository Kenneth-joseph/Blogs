from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Comment,Blog
from .. import db



@main.route('/')
def index():
    title:"hello kent"
    
    return render_template('index.html')


@main.route('/comment')
@login_required
def comment():


    return render_template('comment.html')



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id=user_id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
