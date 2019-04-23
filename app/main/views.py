
from flask import (
    render_template, session, redirect, url_for, flash, request, jsonify
)
from . import main
from .forms import RecipeForm
from ..pred_model import PredModel

learning_model = PredModel('wider_model.joblib')


@main.route('/', methods=['GET', 'POST'])
def index():
    form = RecipeForm(request.form)
    pred_cuisine = session.get('pred_cuisine', None)

    if form.validate_on_submit():
        session['last_ingredients'] = form.ingredients.data
        prediction = learning_model.predict(session['last_ingredients'])
        session['pred_cuisine'] = prediction
        print('prediction: ' + prediction)
        return redirect(url_for('.index'))

    if 'last_ingredients' in session:
        form.ingredients.data = session['last_ingredients']
    return render_template(
        "index.html", form=form, pred_cuisine=pred_cuisine)
