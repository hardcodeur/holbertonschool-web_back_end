#!/usr/bin/env python3
"""Module of Index views.

This module defines several routes related to the status and stats 
of the API, along with handling unauthorized access.
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """GET /api/v1/status

    Return:
        str: JSON with the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """GET /api/v1/stats

    Return:
        str: JSON with the count of each object in the system
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> str:
    """GET /api/v1/unauthorized

    Abort with a 401 status to indicate unauthorized access.
    """
    abort(401)

@app_views.route('/forbidden/', strict_slashes=False)
def forbidden() -> str:
    """GET /api/v1/forbidden

    Abort with a 403 status to indicate forbidden access.
    """
    abort(403)

