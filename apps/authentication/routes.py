from flask import redirect, render_template, request, url_for, flash
from flask_login import login_user, logout_user
from apps import db
from apps.authentication import blueprint, route_login
from apps.authentication.models import Users

# app dependency: authentication
from apps.authentication.utils import hash_pass, verify_pass


@blueprint.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        hashed_password = hash_pass(password)
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
        flash(message, "success")
        return redirect(url_for(route_login))
    return render_template("register.html", title="Register")


@blueprint.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        get_user = Users.query.filter_by(username=username).first()
        if get_user:
            verify_password = verify_pass(password, get_user.password)
            if verify_password:
                print("Password verified. User logging...")
                login_user(get_user)
                flash("User logged in successfully.", "success")
                return redirect(url_for(route_login))
    return render_template("login.html", title="Login")


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("User logged out.", "danger")
    return redirect(url_for(route_login))
