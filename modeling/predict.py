"""Makes predictions using trained model."""

from train_model import nlp_model
from data.clean_preprocess import tokenize


model = nlp_model()


def make_prediction(user_input):
    """Tokenizes texts using custom tokenizer, and makes predictions based upon
       model as trained in train_model.py"""

    model = model.self

    tokenized_text = tokenize(user_input)
    prediction = model.predict(tokenized_text)

    return prediction
