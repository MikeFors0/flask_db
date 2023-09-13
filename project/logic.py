from .models import Recipes, Users
from . import db
from flask import flash, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash


def add_recipe(name, bio):
    recipe = Recipes(name=name, bio=bio)
    db.session.add(recipe)
    db.session.commit()



def filtr_recipe(name, bio):
    recipe = db.session.query(Recipes).filter(Recipes.name == f'{name}').all()
    if not recipe:
        add_recipe(name, bio)
    else:
        flash("Ошибка: такой рецепт уже есть!")


def add_user(email, password):
    user = db.session.query(Users).filter(Users.email == f'{email}').all()
    if not user:
        user = Users(email=email, password=generate_password_hash(password, method='sha256'))
        # user.roles.append(user, "user")
        db.session.add(user)
        db.session.commit()
    else:
        flash("Ошибка: почта уже используется!")


def get_user(email, password):
    user = Users.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Ошибка: неверные данные!")
        return redirect('/login')
    return redirect('/lk')