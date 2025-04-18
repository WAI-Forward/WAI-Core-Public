# src/app/routes/pages/team_stats.py

from flask import render_template
from . import pages_bp

#@call pages_bp.route("/team_stats")
def team_stats():
    return render_template("pages/team_stats.html")
