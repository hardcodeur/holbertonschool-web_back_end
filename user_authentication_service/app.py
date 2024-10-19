#!/usr/bin/env python3
"""
Flask app for user authentication and password management using Auth class
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()

@app.route("/")
def home() -> str:
    """
    Home route to welcome the user.
    """
    return jsonify({"message": "Bienvenue"})


@app.get("/profile")
def profile() -> str:
    """
    Get the profile of the currently logged in user using session_id from cookie.
    """
    session_id_cookie = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id_cookie)

    if session_id_cookie is None or user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.post("/users")
def users() -> str:
    """
    Register a new user by providing email and password.
    """
    data = request.form
    email = data.get("email")
    password = data.get("password")
    
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 404
    
    return jsonify({"email": user.email, "message": "user created"})


@app.post("/sessions")
def login() -> str:
    """
    Log in a user, create a session, and set session_id cookie.
    """
    data = request.form
    email = data.get("email")
    password = data.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    resp = make_response(jsonify({"email": email, "message": "logged in"}))
    resp.set_cookie('session_id', session_id)

    return resp


@app.delete("/sessions")
def logout() -> str:
    """
    Log out a user by destroying their session and redirect to home.
    """
    session_id_cookie = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id_cookie)

    if session_id_cookie is None or user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect("/")


@app.post("/reset_password")
def get_reset_password_token() -> str:
    """
    Generate a password reset token for the user.
    """
    data = request.form
    email = data.get("email")

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    
    return jsonify({"email": email, "reset_token": reset_token})


@app.put("/reset_password")
def update_password() -> str:
    """
    Update the user's password using the reset token.
    """
    data = request.form
    email = data.get("email")
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
