from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("app.config.Config")

    db.init_app(app)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        from .models import urls
        db.create_all()

    return app
