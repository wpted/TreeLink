import os
import flask
from flask import Flask, render_template, redirect, url_for
from form import LoginForm, RegistrationForm, AddLinkForm
from flask_sqlalchemy import SQLAlchemy
import datetime as dt

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(10), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     avatar_img = db.Column(db.String(20), default='./static/assets/default_user_img', nullable=False)
#
#     # links = db.relationship("Links", backref='username', lazy=True)
#
#     def __repr__(self):
#         return f"User({self.username}, {self.email})"
#
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password


class Links(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    link_name = db.Column(db.String(200), nullable=False)
    link_url = db.Column(db.String(1000), unique=True, nullable=False)

    # user.id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, link_name, link_url):
        self.link_name = link_name
        self.link_url = link_url

    def __repr__(self):
        return f"Links {self.link_name}"



mock_user = {
    "username": "Lisa",
    "email": "user@gmail.com",
    "password": "qwerty",
}

# mock_links = {
#     "Example": "https://example.com/",
#     "Icon Finder": "https://www.iconfinder.com/"
#
# }


@app.route('/')
@app.route('/home')
def main():
    db.create_all()
    links = db.session.query(Links).all()

    return render_template("main_page.html", user=mock_user, links=links)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        return redirect(url_for('backstage'))
    return render_template("login.html", form=form)


@app.route('/register', methods=["POST", "GET"])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Add New user to db
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # new_user = User(username, email, password, avatar_img)
        # db.session.add(new_user)
        # db.session.commit()
        return redirect(url_for('backstage'))

    return render_template('register.html', form=form)


@app.route('/backstage')
def backstage():
    current_time = dt.datetime.now().hour
    return render_template("backstage.html", user=mock_user, time=current_time)


@app.route('/edit_links', methods=['POST', 'GET'])
def edit_links():
    current_time = dt.datetime.now().hour
    form = AddLinkForm()
    if form.validate_on_submit():
        # mock_links[form.link_name.data] = form.link_url.data
        new_link = Links(form.link_name.data, form.link_url.data)
        db.session.add(new_link)
        db.session.commit()

        return redirect(url_for("main"))

    return render_template("edit_links.html",
                           user=mock_user,
                           time=current_time,
                           form=form,
                           links=db.session.query(Links).all())


@app.route('/insight')
def insight():
    current_time = dt.datetime.now().hour

    return render_template('insight.html', user=mock_user, time=current_time)


@app.route('/settings')
def settings():
    current_time = dt.datetime.now().hour

    return render_template("settings.html", user=mock_user, time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
