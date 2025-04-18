# src/app/routes/pages/__init__.py

from flask import Blueprint, redirect, url_for

pages_bp = Blueprint('routes', __name__)

from . import *
