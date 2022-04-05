from enum import unique
from flask import flash, abort
from E_voting import db, app
from sqlalchemy.sql import func
from flask_admin import Admin
from flask_login import UserMixin
from E_voting import login_manager
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView #the model view help us to view the data in the database
from flask import flash



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=100))
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    index = db.Column(db.String(length=100))
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    team = db.Column(db.String(length=100),default=0)
    is_admin = db.Column(db.Boolean, default=False)
    mymaster = db.relationship('Courses', backref='author', lazy=True, passive_deletes=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Courses(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    comgrf = db.Column(db.String(length=100))
    computers = db.Column(db.String(length=100))
    inter = db.Column(db.String(length=100))
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)



admin = Admin(app, name='Admin Panel')

class Controller(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.is_admin:
            return current_user.is_authenticated
        else:
            return abort(404)

    def not_auth(self):
        return flash(f'you are not authorized to use the admin dashoard', category='error')
        

admin.add_view(Controller(User, db.session))
admin.add_view(Controller(Courses, db.session))






