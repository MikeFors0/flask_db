from flask import Blueprint, redirect, render_template, request, session, flash
from .logic import filtr_recipe, add_user, get_user
from .models import Recipes, Users



main = Blueprint('main', __name__)

@main.route("/")
def index():
    Recipes_all = Recipes.query.all()
    return render_template('base.html', Recipes_all=Recipes_all)


@main.route("/recipe/<int:id>")
def recipe_id(id):
    recipe = Recipes.query.get_or_404(id)
    return render_template('recipe.html', recipe=recipe)


@main.route('/Adding_Recipe', methods=["POST", "GET"])
def Add():
    if request.method == "POST":
            name = request.form.get('name')
            bio = request.form.get('bio')
            recipe = filtr_recipe(name=name, bio=bio)
            if type(recipe) != str:
                flash("Успешно!")
            else:
                flash(recipe)
    return render_template('add.html')


@main.route("/registration", methods=["POST", "GET"])
def reg():
    if session.get('user') == None:
        if request.method == "POST":
            email = request.form.get('email')
            password = request.form.get('password')
            result = add_user(email=email, password=password)
            if type(result) != str:
                flash("Успешно!")
            else:
                flash(result)
        return render_template('reg.html')
    return redirect('/lk')


@main.route("/login", methods=["POST", "GET"])
def login():
    if session.get('user') == None:
        if request.method == "POST":
            email = request.form.get('email')
            password = request.form.get('password')
            result = get_user(email=email, password=password)
            if type(result) == str:
                flash(result)
            session['user'] = result
            return redirect('/lk')
        return render_template('login.html')
    return redirect('/lk')