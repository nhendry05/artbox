from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from config import db, bcrypt 
from models import User

def main():
    return render_template("main.html")

def register():
    return render_template("registration.html")

def add_user():
    validation_check = User.validate_user(request.form)
    if not validation_check:
        return redirect("/register")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['pw'])
        new_user = User(first_name=request.form['fname'], last_name=request.form['lname'], email=request.form['email'], password=pw_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/user")

def login():
    return render_template("login.html")

def login_user():
    login_check = User.validate_login(request.form)
    if not login_check:
        return redirect("/login")
    else:
        login = User.query.filter_by(email=request.form["email"]).first()
        print(login.password)
        print(request.form['pw'])
        if bcrypt.check_password_hash(login.password, request.form["pw"]):
            session['user_id'] = login.id
            return redirect("/user")


def user():
    return render_template("index.html")

def logout():
    session.clear()
    return redirect("/")


