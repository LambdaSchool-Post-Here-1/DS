from flask import Blueprint, render_template, jsonify
from basilica import Connection
from dotenv import load_dotenv
from data_engineering.training import train_model
import os

predict_routes = Blueprint("predict_routes", __name__)

load_dotenv()

# Load in basilica api key from .env
API_KEY = os.getenv("BASILICA_API_KEY", default='YOU SHALL NOT PASS!')

# Create predict route
@predict_routes.route('/predict') #, methods=['POST'])
def predict():

    # Connect to basilica for embedding text
    basilica_connection = Connection(API_KEY)

    # Instantiate train_model
    classifier = train_model()

    example_text = "My macbook labptop keyboard stopped working. What are the best contacts to deal with this issue?"
    example_embedding = basilica_connection.embed_sentence(example_text, model="reddit")
    prediction = classifier.predict([example_embedding])

    return jsonify(prediction[0]) # Return basic jsonified string to ensure things are working