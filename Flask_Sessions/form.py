from flask_wtf import FlaskForm
# from wtforms.form import Form
from wtforms import(
    StringField,
    SelectField,
    PasswordField,
    SubmitField,
    BooleanField,
    DateField
)

from wtforms.validators import(
    DataRequired,
    length,
    email,
    optional,
    equal_to
)

class Signupform(FlaskForm):
    username=StringField(
        "Username",
        validators=[DataRequired(),length(2,30)]
    )
    email= StringField(
        "Email",
        validators=[DataRequired(),email()]
    )
    gender= SelectField(
        "Gender",
        choices=["M","F","O"],
        validators=[optional()]
    )
    DOB= DateField(
        "Date of Birth",
        validators=[optional()]
    )
    Password = PasswordField(
        "Password",
        validators=[DataRequired(),length(5,20)]

    )
    confirm_pass= PasswordField(
        "confirm_password",
         validators=[DataRequired(),length(5,20),equal_to("Password")]

    )
    submit= SubmitField(
        "Signup"
    )
class loginform(FlaskForm):
    username= StringField(
        "username",
        validators=[DataRequired(),length(3,20)]
    )
    Password = PasswordField(
        "Password",
        validators=[DataRequired(),length(5,20)])

    submit = SubmitField("Login")
