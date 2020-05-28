from flask import Blueprint, render_template, jsonify, request
import os
from data.clean_preprocess import tokenize
import pickle


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

    # def predict(): #define a prediction function
    #     # Get input text from request body
    #     body = request.get_json(force=True)
    #     text = body['text']
    #     # Run through model
    #     knnPickle = 'api/modelknn_pkl.sav'
    #     model, index_df, tfidf = pickle.load(open(knnPickle, 'rb'))
    #     dist, indices = model.kneighbors(tfidf.transform([text]).todense())
    #     recommended_subreddits = [index_df.iloc[n]['subreddit'] for n in indices[0]]
    #     resp = {
    #         'subreddits': uniq(recommended_subreddits)[:3]
    #     }
    #     # give output to sender.
    #     return APP.response_class(
    #         response=json.dumps(resp),
    #         status=200,
    #         mimetype='application/json'
    #     ) (edited) 