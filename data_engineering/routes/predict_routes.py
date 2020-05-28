from flask import Blueprint, render_template, jsonify
from dotenv import load_dotenv
import os

predict_routes = Blueprint("predict_routes", __name__)


# Create predict route
@predict_routes.route('/predict') # methods=['POST']
def predict():

    # Instantiate train_model
    # classifier = train_model()

    # TODO prediction = classifier.predict([user_text])

    return jsonify("We all live in a yellow submarine...") # Return basic jsonified string to ensure things are working

