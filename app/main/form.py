from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required


class CommentForm(FlaskForm):
    content=TextAreaField('comment on blog' validator=[Required()])
    submit=SubmitField('comment')

class BlogForm(FlaskForm):
    title = StringField('Title',validator=[Required])
    category = StringField('Category',choices=[('Technology','Technology'),('Music','Music'),('Sports','Sports')],validator = [Required])
    post = TextAreaField('Your blog', validator = [Required])
    submit = SubmitField('share your blog')