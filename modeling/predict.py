"""Makes predictions using trained model."""


import imp
import pickle


tokenize = imp.load_source('tokenize', './data/clean_preprocess.py')

# Load in pickled model.
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

def make_prediction(user_input):
    """Tokenizes texts using custom tokenizer, and makes predictions based upon
       model as trained in train_model.py"""

    tokenized_text = tokenize(user_input)
    prediction = model.predict(tokenized_text)

    return prediction
