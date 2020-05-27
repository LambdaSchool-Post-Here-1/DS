
from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

# File path for database
# TODO DATABASE_URI = "sqlite:////_________________

# app_routes = Blueprint("app_routes", __name__)

# Instantiate sqlalchemy
db = SQLAlchemy()

# instantiate flask app
app = Flask(__name__)


# TODO def create_app():
    # app = Flask(__name__)
    # TODO app.config____________
    # TODO db.init_app(app)

    # TODO app.register_blueprint(____routes)
    # TODO app.register_blueprint(____routes)
    
    # return app

# Create home route
@app.route("/")
def index():
    return "HAKUNA MATADA!!!" # Return basic string to ensure things are working

# Create predict route
@app.route('/predict') #, methods=['POST'])
def predict():
    # TODO app.logger.info("/predict beginning...")
    # TODO request_data = request.get_json(force=True)
    # TODO input_text = request_data['text']

    return "So far so good..." # Return basic string to ensure things are working

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)


