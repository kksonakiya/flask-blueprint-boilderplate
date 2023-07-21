from apps import db
from apps.api import blueprint
from flask import jsonify, request
from apps.authentication.models import Users

# app dependency: authentication
from apps.authentication.utils import hash_pass, verify_pass


@blueprint.route("/test")
def test():
    return jsonify(dict(response="Api test route success"))


@blueprint.route("/register", methods=["POST"])
def register():
    username = request.form.get("username").lower()
    password = request.form.get("password")
    hashed_password=hash_pass(password)
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email").lower()
    new_user = Users(
        username=username,
        password=hashed_password,
        firstname=firstname,
        lastname=lastname,
        email=email,
    )
    db.session.add(new_user)
    db.session.commit()
    message = f"User with {username} created successfully."
    response = dict(response=message)
    return jsonify(response)
