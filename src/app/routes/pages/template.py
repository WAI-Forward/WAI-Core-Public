# src/app/routes/pages/template.py

"""
This is the ROUTE file for a new page in the Flask app.

🧠 GPT Instructions:
- DO NOT change the import or blueprint setup.
- Only change the route path and the name of the template file being rendered.
- The function name and route should match the page name (e.g., about_page → "/about").

Each route function renders a corresponding HTML template from:
src/app/templates/pages/<page>.html
"""

from flask import render_template
from . import pages_bp  # This is the Blueprint used for all page routes

# 👇 GPT should update this line:
@pages_bp.route("/template")
def template_page():
    """
    This function handles requests to the '/template' URL.

    🔄 GPT should:
    - Rename this function to match the new page (e.g., about_page)
    - Update the route path (e.g., '/about')
    - Update the HTML template filename below (e.g., 'pages/about.html')
    """
    return render_template("pages/template.html")
