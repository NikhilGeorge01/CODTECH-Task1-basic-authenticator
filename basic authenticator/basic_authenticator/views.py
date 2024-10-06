from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import app, lm, db
from .forms import LoginForm, SignupForm


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    return render_template("index.html")

@login_required
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Form validated!") 
        user = User.query.filter_by(email=form.email.data).first()  
        if user and user.check_password(form.password.data):  
            login_user(user, form.remember_me.data) 
            flash("Login successful")  
            return redirect(url_for('home'))  
        flash("Incorrect password or email")  
        with app.app_context():
          users = User.query.limit(5).all()
    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():  
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()  
        flash("Registration successful, please log in.")
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)
@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))




