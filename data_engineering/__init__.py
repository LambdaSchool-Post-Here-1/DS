
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from data_engineering.routes.home_routes import home_routes
from data_engineering.routes.predict_routes import predict_routes
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

# File path for database
DATABASE_URL = os.getenv("DATABASE_URL")

# Instantiate sqlalchemy and migrate
db = SQLAlchemy()
migrate = Migrate()

# Create connection to database
connection = sqlite3.connect(DATABASE_URL)

# Read in dataframe and convert to sqlite table
df = pd.read_csv('data/datasets/cleaned_data.csv')
df = df.dropna()
df = df.drop(columns='Text')
df.to_sql('test_db.sqlite3', con=connection, if_exists='replace')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URL'] = DATABASE_URL
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


