# src/app/routes/__init__.py

from flask import Blueprint, redirect, url_for

routes_bp = Blueprint('routes', __name__)

from .pages import pages_bp
routes_bp.register_blueprint(pages_bp)

