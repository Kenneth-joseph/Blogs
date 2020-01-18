from flask import render_template
from . import main


@main.route('/')
def index():
    title:"hello kent"
    
    return render_template('index.html')


@main.route('/comment')
def comment():

    return render_template('comment.html')
