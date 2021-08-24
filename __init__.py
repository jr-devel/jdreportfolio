from os import environ
from flask import *
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        db = os.environ.get('FLASK_DATABASE'),
        host_db = os.environ.get('FLASK_DATABASE_HOST'),
        user_db = os.environ.get('FLASK_DATABASE_USER'),
        pass_db = os.environ.get('FLASK_DATABASE_PASSWORD')
    )
    #
    from . import routes
    app.register_blueprint(routes.bp)
    #
    return app