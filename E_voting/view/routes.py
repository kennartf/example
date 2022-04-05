from flask import Blueprint
from flask import redirect, request, render_template, flash


views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')

