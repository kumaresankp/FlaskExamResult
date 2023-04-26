from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,DecimalField,FloatField,DateField,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError,NumberRange
from flask_wtf.file import FileAllowed
from Result.models import User


class AdminForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class MarksForm(FlaskForm):
    semester = SelectField('Semester', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')])
    exam_type = SelectField('Exam Type', choices=[('cat1', 'CAT-1'), ('cat2', 'CAT-2'), ('model', 'Model Exam')])
    marks_file = FileField('Marks File', validators=[DataRequired(), FileAllowed(['xlsx', 'csv'], 'Only .xlsx or .csv files allowed!')])
    submit = SubmitField('Upload Marks')


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    Regno = StringField('Register Number',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_regno(self,Regno):
        user = User.query.filter_by(Regno=Regno.data).first()
        if user:
            raise ValidationError("Username already Exists")



    def validate_regno(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is  already Taken")




class LoginForm(FlaskForm):
    Regno = StringField('Register Number',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')