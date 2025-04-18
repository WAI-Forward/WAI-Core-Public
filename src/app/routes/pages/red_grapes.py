from flask import render_template
from . import pages_bp

@pages_bp.route("/red_grapes")
def red_grapes():
    return render_template("pages/red_grapes.html")
