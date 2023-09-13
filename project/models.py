from . import db
from datetime import datetime
# from flask_security import UserMixin, RoleMixin

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime,  default=datetime.utcnow)
    # Ingredients = db.relationship('Ingredients', backref='Recipe_all')
    #                        server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Recipes {self.name}>'


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
    

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     default = db.Column(db.Boolean,default=False,index=True)
#     permissions = db.Column (db.Integer) # Значением является целое число, указывающее битовый флаг.
#     users = db.relationship('Users', backref='role', lazy='dynamic')


# user_datastore = SQLAlchemySessionUserDatastore(db.session, Users, Role)
# security = Security(app, user_datastore)

