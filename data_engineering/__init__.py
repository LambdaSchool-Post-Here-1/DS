
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from data_engineering.routes.home_routes import home_routes
from data_engineering.routes.predict_routes import predict_routes
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import os
import psycopg2

# URL to heroku postgresql database
DATABASE_URL = "postgres://khqrpuidioocyy:28306f6ac214b8c5ff675ab1e38ed6007d0b810d0a538df3e0db3da0f3cde717@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d1jb037n8m5r20"

# Heroku postgresql credentials
DB_NAME = "d1jb037n8m5r20"
DB_USER = "khqrpuidioocyy"
DB_PASSWORD = "28306f6ac214b8c5ff675ab1e38ed6007d0b810d0a538df3e0db3da0f3cde717"
DB_HOST = "ec2-18-210-214-86.compute-1.amazonaws.com"

# Create engine within heroku postgresql database
myeng = sqlalchemy.create_engine("postgres://khqrpuidioocyy:28306f6ac214b8c5ff675ab1e38ed6007d0b810d0a538df3e0db3da0f3cde717@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d1jb037n8m5r20")

# Instantiate sqlalchemy and migrate
db = SQLAlchemy()
migrate = Migrate()

# Read in dataframe and convert to sqlite table
df = pd.read_csv('data/datasets/cleaned_data.csv')
df = df.dropna()
df = df.drop(columns='Tokens')
df.to_sql('postgresql-shallow-75985', con=myeng, if_exists='replace')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
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


