from operator import index
from flask import Blueprint
from E_voting import db, bcrypt
from E_voting. models import User
from .form import AdminLogin, AdminRegister
from flask import flash, redirect, render_template, request, url_for, request
from flask_login import login_user, logout_user, current_user, login_required



admin_panel = Blueprint('admin_panel', __name__)



@admin_panel.route('/captains0017/<int:post_id>', methods=['GET', 'POST'])
@login_required
def masterpage2(post_id):
    user = current_user
    members = User.query.all()
    return render_template('mpage.html', user=user, members=members, post_id=post_id)




@admin_panel.route('/p4ssw0rdHTU2022/<int:post_id>', methods=['GET', 'POST'])
def adminsig(post_id):
    form = AdminRegister()
    if form.validate_on_submit():
        pass_hass = bcrypt.generate_password_hash(form.password.data)
        user = User(email=form.email.data, password=pass_hass,  is_admin=True)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully', category='success')
        # return redirect(url_for(''))
    return render_template('adminsignup.html', form=form, post_id=post_id)
    



@admin_panel.route('/p4ssw0rdHTU2021/<int:post_id>', methods=['GET', 'POST'])
def masterpage(post_id):
    form = AdminLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'Success! You are logged in as {user.email}', category='success')
            return redirect(url_for('admin.index'))
        else:
            flash('Login Uncessful. Please check email and password', category='error')
    return render_template('adminlogin.html', form=form, post_id=post_id)
    


@admin_panel.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfuly', category='success')
    return redirect(url_for('views.home'))
    return render_template('home.html')
