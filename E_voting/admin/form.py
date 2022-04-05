from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Email, EqualTo, DataRequired, Length, ValidationError




class AdminRegister(FlaskForm):
	email = StringField(validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email address'})
	password = PasswordField(validators=[DataRequired(), Length(min=1, max=20)], render_kw={'placeholder': 'Password (at least 3-20 characters)'})
	confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'Confirm_Password'})
	submit = SubmitField(label='Sign Up')



class AdminLogin(FlaskForm):
	email = StringField(validators=[DataRequired(), Length(min=1, max=30)], render_kw={'autofocus': True, 'placeholder': 'Plese enter your email'})
	password = PasswordField(validators=[DataRequired()], render_kw={'placeholder': 'Please enter your password'})
	submit = SubmitField(label='Sign In')


