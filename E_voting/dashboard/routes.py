from E_voting import db
from flask import Blueprint
from E_voting .models import User
from flask_login import login_required, current_user
from flask import redirect, render_template, request, flash, url_for



dashbrd = Blueprint('dashbrd', __name__)


@dashbrd.route('/dashboard')
@login_required
def dashboard():
    return render_template('voters.html')


@dashbrd.route('/votedashboard/', methods=['GET', 'POST'])
@login_required
def votedashboard():
    return render_template('votepage.html')


