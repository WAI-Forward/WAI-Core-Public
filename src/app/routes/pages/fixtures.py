# src/app/routes/pages/fixtures.py

from flask import render_template
from . import pages_bp

#@call pages_bp.route("/fixtures")
def fixtures():
    return render_template("pages/fixtures.html")
