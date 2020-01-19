from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required


class CommentForm(FlaskForm):
    content=TextAreaField('comment on blog' validator=[Required()])
    submit=SubmitField('comment')