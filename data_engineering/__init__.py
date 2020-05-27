
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from data_engineering.routes.home_routes import home_routes
from data_engineering.routes.predict_routes import predict_routes

# File path for database
DATABASE_URI = "sqlite:///test_db.db" 

# Instantiate sqlalchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(home_routes)
    app.register_blueprint(predict_routes)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)


