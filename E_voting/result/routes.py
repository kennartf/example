import random
from flask import Blueprint
from flask_login import current_user
from E_voting. models import User
from flask import render_template, redirect, flash
from E_voting import db

result_display = Blueprint('result_display', __name__)



def generate_id(sys_user):
    all_members = User.query.all()
    if len(all_members)  > 30:
        return "limit"
    else:
        myrandom = random.randint(1, 17)
        members = User.query.filter_by(team=str(myrandom)).all()
        if len(members) < 1:
            if sys_user.team == str(0):
                sys_user.team = myrandom
                db.session.commit()
                return sys_user.team
            user = sys_user 
        else:
            return sys_user.team
            if len(all_members) == 30:
                return sys_user.team
            else:
                flash('You have reach the limited number', category='error')
                generate_id(sys_user)



@result_display.route('/showresult', methods=['GET', 'POST'])
def showresult():
    user = current_user 
    sys_user = User.query.get(user.id)
    myrandom = generate_id(sys_user)
    members = User.query.filter_by(team=str(myrandom)).all()
    if user:
        flash('From X-CODERS)): thanks for your vote', category='success')
    return render_template('result.html', myrandom=myrandom, user=user, members=members)
    
