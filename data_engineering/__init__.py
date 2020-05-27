
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from data_engineering.routes.home_routes import home_routes
from data_engineering.routes.predict_routes import predict_routes
import pandas as pd
import sqlite3
import os

# File path for database
DATABASE_URI = os.path.join(os.path.dirname(__file__), "test_db.sqlite3") # "sqlite:///DS/data_engineering/test_db.sqlite3"
os.path.join(os.path.dirname(__file__), "test_db.sqlite3")
DATAFRAME_URI = "data_engineering/reddit_tech(1).csv"

# Instantiate sqlalchemy and migrate
db = SQLAlchemy()
migrate = Migrate()

# Create connection to database
connection = sqlite3.connect(DATABASE_URI)

# Read in dataframe and convert to sqlite table
df = pd.read_csv(DATAFRAME_URI)
df = df.dropna()
df.to_sql('test_db.sqlite3', con=connection, if_exists='replace')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(predict_routes)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

    # print(df.head())
    # print(df.shape)


