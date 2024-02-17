from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "grah grah" # not so secret for now ig

    return app
