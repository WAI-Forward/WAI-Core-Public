# src/app/__init__.py

import secrets

from flask import Flask
from .context import register_context

def create_app():
    app = Flask(__name__)

    app.secret_key = secrets.token_hex(24)

    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    register_context(app)

    return app

