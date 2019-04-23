from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    ingredients = StringField(
        'Enter ingredients', widget=TextArea(), validators=[DataRequired()],
        render_kw={"rows": 15, "cols": 11})
    submit = SubmitField('Submit')
