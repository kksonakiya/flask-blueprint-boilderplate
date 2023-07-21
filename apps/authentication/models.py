from flask_login import UserMixin
from apps import db, login_manager
from datetime import datetime


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    user = Users.query.filter_by(username=username).first()
    print("request loader: ", user)
    return user


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    password = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
