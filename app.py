from features.resources import add_api_resources
from flask import Flask
from flask_cors import CORS

from features.repo import db


def create_flask_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    CORS(app)
    db.init_app(app)
    db.app = app
    add_api_resources(app)
    return app


if __name__ == "__main__":
    flask_app = create_flask_app()
    with flask_app.app_context():
        flask_app.run()
