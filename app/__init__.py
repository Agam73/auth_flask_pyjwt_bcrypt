from flask import Flask
from .config import Config
from .extensions import db
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(bp)

    return app
