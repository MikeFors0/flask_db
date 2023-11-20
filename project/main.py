from flask import Flask, Blueprint, redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from logic import *

db = SQLAlchemy()
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.create_all(app)

@app.route("/")
def index():
    Recipe_all = Recipe.query.all()
    return render_template('base.html', Recipe_all=Recipe_all)


# @app.route("/recipe/<int:id>")
# def recipe_id(id):
    # recipe = Recipe.query.get_or_404(id)
    # return render_template('recipe.html', recipe=recipe)


# @app.route('/Adding_Recipe', methods=["POST", "GET"])
# def Add():
#     if request.method == "POST":
#             name = request.form.get('name')
#             bio = request.form.get('bio')
#             recipe = filtr_recipe(name=name, bio=bio)
#             if type(recipe) != str:
#                 flash("Успешно!")
#             else:
#                 flash(recipe)
#     return render_template('add.html')


# @app.route("/registration", methods=["POST", "GET"])
# def reg():
#     if session.get('user') == None:
#         if request.method == "POST":
#             email = request.form.get('email')
#             password = request.form.get('password')
#             result = add_user(email=email, password=password)
#             if type(result) != str:
#                 flash("Успешно!")
#             else:
#                 flash(result)
#         return render_template('reg.html')
#     return redirect('/lk')


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if session.get('user') == None:
#         if request.method == "POST":
#             email = request.form.get('email')
#             password = request.form.get('password')
#             result = get_user(email=email, password=password)
#             if type(result) == str:
#                 flash(result)
#             session['user'] = result
#             return redirect('/lk')
#         return render_template('login.html')
#     return redirect('/lk')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=7070, debug=True)
    
