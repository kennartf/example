from flask import Blueprint
from E_voting import db, bcrypt
from E_voting .models import User, Controller
from flask import get_flashed_messages
from .form import RegisterForm, LoginForm
from flask import flash, redirect, render_template, request, url_for, request
from flask_login import login_user, logout_user, current_user, login_required


authent = Blueprint('authent', __name__)


@authent.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, index=form.index.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully', category='success')
        return redirect(url_for('authent.login'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Registration unsuccessful {err_msg}', category='error')
    return render_template('signup.html', form=form)
 


@authent.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'Success! You are logged in as {user.email}', category='success')
            return redirect(url_for('dashbrd.dashboard'))
        else:
            flash('Login Uncessful. Please check email and password', category='error')
    return render_template('login.html', form=form)



@authent.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfuly', category='success')
    return redirect(url_for('views.home'))
    return render_template('home.html')
