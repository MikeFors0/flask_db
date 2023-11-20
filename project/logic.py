from main import db
from flask import flash, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


def add_recipe(name, bio):
    recipe = Recipe(name=name, bio=bio)
    db.session.add(recipe)
    db.session.commit()



def filtr_recipe(name, bio):
    recipe = db.session.query(Recipe).filter(Recipe.name == f'{name}').all()
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


# from flask_security import UserMixin, RoleMixin

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime,  default=datetime.utcnow)
    # Ingredients = db.relationship('Ingredients', backref='Recipe_all')
    #                        server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Recipe {self.name}>'


# roles_users = db.Table('roles_users', 
#                        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#                        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    # roles = db.relationship('Role', secondary=roles_users, backref='roled')
    # pr = db.relationship('Profiles', backref='users', uselist=False)


    def __repr__(self):
        return f"<users {self.id}>"
    