from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from cpabooking.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
  
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")


def validate_email(self, email): # verifying email
    user = User.query.filter_by(email=email.data).first() # same query as the username validation but just with the email field

    if user: # there is a user that already has that email
      raise ValidationError("An account with this email already exists. Please use another email.")


class RegisterForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2,max=20)])

  email = StringField("Email", validators=[DataRequired(), Email()])
  
  house = SelectField(u'House', choices=[("B", "Byron"), ("C", "Churchill"), ("K", "Keller"), ("N", "Nehru"), ("So", "Sonakul"), ("S", "Suriyothai")], validators=[DataRequired()])

  year = SelectField(u'Year group', choices=[(i, i) for i in range(6, 13)], validators=[DataRequired()])

  password = PasswordField("Password", validators=[DataRequired()])
  
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
  
  submit = SubmitField("Sign Up")


def validate_email(self, email): # verifying email
    user = User.query.filter_by(email=email.data).first() # same query as the username validation but just with the email field

    if user: # there is a user that already has that email
      raise ValidationError("An account with this email already exists. Please use another email.")

class BookingForm(FlaskForm):
    # date, no people, time slot
    date = StringField("Date", validators=[DataRequired()])

    no_people = SelectField("No. People", choices=[], validators=[DataRequired()])

    time_slot = SelectField("Time Slot", choices=["Before School", "Break Time", "Lunch", "3-4pm", "4-5pm"], validators=[DataRequired()])
