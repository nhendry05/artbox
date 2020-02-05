from flask import render_template, redirect, request
from flask_bcrypt import Bcrypt
from config import db
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
        return redirect("/login")

def login():
    return render_template("login.html")

def login_user():
    
    return redirect("/login")


