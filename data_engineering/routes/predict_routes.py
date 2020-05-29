from flask import Blueprint, render_template, jsonify, request
import os
from data.clean_preprocess import tokenize
import pickle
import sklearn

predict_routes = Blueprint("predict_routes", __name__)

# Create predict route
@predict_routes.route('/predict', methods=['POST'])
def predict():

    # Load the Model back from file
    with open('finalized_model.sav', 'rb') as file:  
        pickled_ml_model = pickle.load(file)

    user_input = request.get_json(force=True)
    user_text = user_input['text']

    tokenized_text = tokenize(user_text)
    prediction = pickled_ml_model.predict(tokenized_text)


    return jsonify(prediction[0]) # Return basic jsonified string to ensure things are working