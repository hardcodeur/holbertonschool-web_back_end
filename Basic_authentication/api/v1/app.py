#!/usr/bin/env python3
"""
Route module for the API.

This module contains the Flask application and the route handling
for the API with appropriate error handling and authentication setup.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.auth import Auth
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

if os.environ.get("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
else:
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler.

    Returns:
        str: A JSON response with a 404 error message.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler.

    Returns:
        str: A JSON response with a 401 error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler.

    Returns:
        str: A JSON response with a 403 error message.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Before request handler.

    This function checks if the request path requires authentication.
    If it does, it verifies the authorization header and handles
    authentication for the API routes.
    """
    if auth is None:
        return

    path_list = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if not auth.require_auth(request.path, path_list):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
