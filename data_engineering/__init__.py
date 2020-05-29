
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from data_engineering.routes.home_routes import home_routes
from data_engineering.routes.predict_routes import predict_routes
import sqlalchemy
import pandas as pd
import os
import psycopg2


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(home_routes)
    app.register_blueprint(predict_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
