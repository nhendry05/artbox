from sqlalchemy.sql import func
from config import db
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pass_valid = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*?^])[a-zA-z0-9!@#$%&*?^]+$')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    @classmethod
    def validate_user(cls, user_info):
        is_valid = True
        if len(user_info["fname"]) < 1:
            is_valid = False
            flash("Please provide a first name")
        if len(user_info["lname"]) < 1:
            is_valid = False
            flash("Please provide a last name")
        if not EMAIL_REGEX.match(user_info["email"]):
            is_valid = False
            flash("Please enter a valid email")
        if len(user_info["pw"]) < 8:
            is_valid = False
            flash("Password must be at least 8 characters")
        if not re.search(pass_valid, user_info['pw']):
            is_valid = False
        flash("Password must contain one uppercase, one lowercase and one special character")
        if user_info["pw"] != user_info["pwc"]:
            is_valid = False
            flash("Passwords do not match")
        return is_valid
    @classmethod
    def validate_login(cls, user_info):
        is_valid = True
        if len(user_info["email"]) < 1:
            is_valid = False
        return is_valid

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    birthday = db.Column(db.Integer)
    photo = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
