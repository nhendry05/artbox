from flask import render_template, redirect, request, session, url_for, flash, send_from_directory
from flask_bcrypt import Bcrypt
from config import db, bcrypt 
from models import User, Child, Art
from datetime import datetime
#ADDED HERE
import os
from uuid import uuid4
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#END ADD

def main():
    return render_template("main.html")

def register():
    if 'user_id' in session:
        user_id = session['user_id']
        return redirect(url_for('user', user_id=user_id))
    return render_template("register.html")

def register_user():
    validation_check = User.validate_user(request.form)
    if not validation_check:
        return redirect("/register")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['pw'])
        new_user = User(first_name=request.form['fname'], last_name=request.form['lname'], email=request.form['email'], password=pw_hash)
        db.session.add(new_user)
        db.session.commit()
        login = User.query.filter_by(email=request.form["email"]).first()
        session['user_id'] = login.id
        user_id = session['user_id']
        return redirect(url_for('user', user_id=user_id ))

def login():
    if 'user_id' in session:
        user_id = session['user_id']
        return redirect(url_for('user', user_id=user_id))
    return render_template("login.html")

def login_user():
    login_check = User.validate_login(request.form)
    if not login_check:
        return redirect("/login")
    else:
        login = User.query.filter_by(email=request.form["email"]).first()
        if login is None:
            flash("Email is not valid")
            return redirect("/login")
        else:
            print(login.password)
            print(request.form['pw'])
            if bcrypt.check_password_hash(login.password, request.form["pw"]):
                session['user_id'] = login.id
                user_id = session['user_id']
                return redirect(url_for('user', user_id=user_id ))
            else:
                flash("Password is incorrect")
                return redirect("/login")

def user(user_id):
    user_id = session['user_id']
    user_logged_in =  User.query.filter_by(id=user_id).first()
    all_children =  Child.query.filter_by(parent_id=user_id).all()
    return render_template("user.html", user=user_logged_in, all_children=all_children)

def send_cover(filename):
    return send_from_directory("cover", filename)

def new_child(user_id):
    user_id = session['user_id']
    return render_template("add_child.html", user_id=user_id)

def add_child():
    user_id = session['user_id']

    target = os.path.join(APP_ROOT, 'templates/cover')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    for photo in request.files.getlist("cover_photo"):
        print(photo)
        photoname = photo.filename
        destination = "/".join([target, photoname])
        print(destination)
        photo.save(destination)
    
    new_child = Child(name=request.form['child_name'], birthday=request.form['child_birthday'], photo=photoname, parent_id=request.form['parent_id'])
    db.session.add(new_child)
    db.session.commit()


    return redirect(url_for('user', user_id=user_id ))

def edit_child(user_id):
    user_id = session['user_id']
    user_logged_in =  User.query.filter_by(id=user_id).first()
    all_children =  Child.query.filter_by(parent_id=user_id).all()
    print(all_children)
    return render_template("edit_child.html", all_children=all_children, user=user_logged_in)

def editchild():
    user_id = session['user_id']
    child_edit = Child.query.filter_by(name=request.form['child_name']).first()

    target = os.path.join(APP_ROOT, 'templates/cover')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    for photo in request.files.getlist("cover_photo"):
        print(photo)
        photoname = photo.filename
        destination = "/".join([target, photoname])
        print(destination)
        photo.save(destination)

    child_edit.birthday = request.form['child_birthday']
    child_edit.photo = photoname
    db.session.commit()
    user_logged_in =  User.query.filter_by(id=user_id).first()
    return redirect(url_for('user', user_id=user_id))

def childpage(user_id, child_id, child_name):
    user_id = session['user_id']
    child_id = child_id
    all_art =  Art.query.filter_by(child_id=child_id).order_by(Art.creation_date.desc()).all()
    user_logged_in =  User.query.filter_by(id=user_id).first()
    child_name = child_name
    return render_template("child_page.html", user=user_logged_in, child_name=child_name, child_id=child_id, all_art=all_art)

def new_art(user_id):
    user_id = session['user_id']
    user_logged_in =  User.query.filter_by(id=user_id).first()
    all_children =  Child.query.filter_by(parent_id=user_id).all()
    return render_template("add_art.html", user=user_logged_in, all_children=all_children)

def add_art():
    user_id = session['user_id']

    target = os.path.join(APP_ROOT, 'templates/art/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    for art in request.files.getlist("new_art"):
        print(art)
        artname = art.filename
        destination = "/".join([target, artname])
        print(destination)
        art.save(destination)
    

    all_children =  Child.query.filter_by(parent_id=user_id).all()
    child_name = request.form['child_name']
    for child in all_children:
        if child.name == child_name:
            child_id = child.id
    
    new_art = Art(title = request.form['title'], art=artname, creation_date=request.form['art_date'], description=request.form['art_description'], child_id=child_id)
    db.session.add(new_art)
    db.session.commit()
    return redirect(url_for('user', user_id=user_id ))

def artpage(child_id, art_id):
    child_id = child_id
    art_id = art_id
    user_id = session['user_id']
    artwork =  Art.query.filter_by(child_id=child_id).filter_by(id=art_id).first()
    return render_template("art_page.html", user_id=user_id, child_id=child_id, art_id=art_id, artwork=artwork)

def delete_child(child_id):
    user_id = session['user_id']
    child_id = child_id 
    child_to_delete = Child.query.filter_by(id = child_id).filter_by(parent_id = user_id).first()
    db.session.delete(child_to_delete)
    db.session.commit()
    return redirect(url_for('user', user_id=user_id))

def delete_art(child_id, art_id):
    user_id = session['user_id']
    child_id=child_id
    art_id = art_id
    child = Child.query.filter_by(id=child_id).first()
    child_name = child.name
    user_logged_in =  User.query.filter_by(id=user_id).first()
    art_to_delete = Art.query.filter_by(id = art_id).filter_by(child_id = child_id).first()
    db.session.delete(art_to_delete)
    db.session.commit()
    
    return redirect(url_for('childpage', user_id=user_id, child_id=child_id, child_name=child_name))

def logout():
    session.clear()
    return redirect("/")