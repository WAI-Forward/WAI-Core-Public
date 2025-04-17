# src/app/routes/pages/home.py

from flask import render_template
from . import pages_bp

@pages_bp.route("/")
def home():
    return render_template("pages/home.html")