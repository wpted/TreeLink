from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField , URLField
from wtforms.validators import DataRequired, Email, EqualTo, Length, url




class LoginForm(FlaskForm):
    email = EmailField(label="User Email",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "User Email"})
    password = PasswordField(label="Password",
                             validators=[DataRequired()],
                             render_kw={"placeholder": "User Password"})
    submit = SubmitField(label="Login")


class RegistrationForm(FlaskForm):
    username = StringField(label="Username",
                           validators=[DataRequired(), Length(6, 10)],
                           render_kw={"placeholder": "Username"})
    email = EmailField(label="Email",
                       validators=[DataRequired(), Email()],
                       render_kw={"placeholder": "User Email"})

    password = PasswordField(label="Password",
                             validators=[DataRequired(), Length(6, 10)],
                             render_kw={"placeholder": "Password"})

    password_confirm = PasswordField(label="Repeat Password",
                                     validators=[DataRequired(),
                                                 EqualTo(password,
                                                         message="Password Must Match")],
                                     render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField(label="Register")


class AddLinkForm(FlaskForm):
    link_name = StringField(label="Link Name",
                           validators=[DataRequired(), Length(4, 40)],
                           render_kw={"placeholder": "Link Name"})

    link_url = URLField(label="Link Name",
                           validators=[DataRequired(), url()],
                           render_kw={"placeholder": "Link URL"})

    add = SubmitField(label="Add Link")