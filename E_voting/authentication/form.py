from flask_wtf import FlaskForm
from E_voting .models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Email, EqualTo, Length, ValidationError, DataRequired
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField, TextAreaField




class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=5, max=20)],  render_kw={'placeholder': 'Username (at least 5-20 characters)'})
    email = StringField(validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email address'})
    index = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Index number'})
    password = PasswordField(validators=[DataRequired(), Length(min=3, max=20)], render_kw={'placeholder': 'Password (at least 3-20 characters)'})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'Confirm_Password'})
    submit = SubmitField(label='Sign Up')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exist! Please try a different username')


    def validate_index(self, index):
        user = User.query.filter_by(index=index.data).first()
        if user:
            raise ValidationError('That index number already exist! Please try a different index num.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exist Please choose different one')



class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Email address'})
    password = PasswordField(validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField(label='Log In')



