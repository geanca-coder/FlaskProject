from market import app
from flask import render_template , url_for, redirect, flash, get_flashed_messages
from market.Models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import  login_user, logout_user
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email=form.email_address.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))
    if form.errors != {}: #if there are errors in the validations field
        for i in form.errors.values():
            flash(f'Error{i}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attemptedUser = User.query.filter_by(username=form.username.data).first()
        if attemptedUser and attemptedUser.check_password(attempted_password=form.password.data):
            login_user(attemptedUser)
            flash(f'Succes! You are logged in as: {attemptedUser.username}', category='succes')
            return redirect(url_for('market_page'))
        else:
            flash('User or password are incorrect', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home_page'))
