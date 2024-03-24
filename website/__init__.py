from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "user.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gfanglag arngalgnal'
    app.secret_key = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../website/{DB_NAME}'
    db.init_app(app)

    with app.app_context():

        from .views import views
        from .auth import auth

        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')

        from .model import User, Note

        create_database(app)

        return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print("Created Database")