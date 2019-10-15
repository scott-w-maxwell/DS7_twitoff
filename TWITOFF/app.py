"""Main application for twitoff"""


#import flask package. flash makes app objects.
from flask import Flask, render_template 

def create_app():
    """creates and configures an instance of a flask app"""
    app = Flask(__name__)
    #routes determine location
    @app.route("/")

    # app.config['SQLALCHEMY_DATABASE_URL']
    # DB.init_app(app)
    def root():
        return "Welcome to the App"
    return app

