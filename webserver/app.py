from flask import Flask, render_template, Blueprint, redirect, url_for, flash, request, session
from flask_login import LoginManager, UserMixin, login_required
from jinja2 import Template
from snek import *

app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = 'configure strong secret key here'
app.jinja_env.globals.update(get_temp=get_temp)
app.jinja_env.globals.update(get_humidity=get_humidity)

auth = Blueprint("auth", __name__)
main = Blueprint("main", __name__)
app.register_blueprint(auth)
app.register_blueprint(main)

login_manager = LoginManager()
login_manager.init_app(app)

password = "root"

class User(UserMixin):
    user_database = {"JohnDoe": ("JohnDoe", "John"),
               "JaneDoe": ("JaneDoe", "Jane")}

    def __init__(self, username, password):
        self.id = username
        self.password = password

    @classmethod
    def get(cls,id):
        return cls.user_database.get(id)

@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":") # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                return user
    return None

@app.route("/status")
def status_lamp():
    if not session.get('root'):
        return redirect(url_for("login"))
    try:
        val = lamp_status()
    except Exception as e:
        return f"Failed: '{e}'", 500
    return str(val), 200

@app.route("/toggle_lamp")
def toggle_l():
    if not session.get('root'):
        return redirect(url_for("login"))
    try:
        val = toggle_lamp()
    except Exception as e:
        return f"Failed: '{e}'", 500
    return str(val), 200

@app.route("/buzz")
def buzzz():
    if not session.get('root'):
        return redirect(url_for("login"))
    try:
        buzz()
    except Exception as e:
        return f"Failed: '{e}'", 500
    return "buzzed", 200

@app.route("/profile")
def profile():
    if not session.get('root'):
        return redirect(url_for("login"))
    return render_template("profile.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop('root', None)
    return render_template("logout.html")

@app.route("/login", methods=["POST"])
def login_post():
    if password == request.form.get("password"):
        session['root'] = True
        return redirect(url_for("profile"))
    return redirect(url_for("login"))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    setup()
    app.run(port=80, host='0.0.0.0')
    #  app.run(debug=True, port=80, host='0.0.0.0')
